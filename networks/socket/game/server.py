import socket
import threading
import pickle
from collections import deque

class GameRoom:
    def __init__(self, name, admin):
        self.name = name
        self.admin = admin
        self.players = {}
        self.used_cities = set()
        self.scores = {}
        self.current_player = None
        self.last_char = None
        self.lock = threading.Lock()
        self.command_queue = deque()

    def add_player(self, player_name, conn):
        with self.lock:
            self.players[player_name] = conn
            self.scores[player_name] = 0
            if len(self.players) == 1:
                self.current_player = player_name

    def remove_player(self, player_name):
        with self.lock:
            if player_name in self.players:
                del self.players[player_name]
                del self.scores[player_name]

    def is_valid_city(self, city):
        city = city.lower().strip()
        if not city:
            return False
        if city in self.used_cities:
            return False
        if self.last_char and city[0] != self.last_char:
            return False
        return True  # В реальном приложении добавить проверку существования города

    def process_turn(self, player_name, city):
        with self.lock:
            if player_name != self.current_player:
                return False, "Сейчас не ваш ход"
            if not self.is_valid_city(city):
                return False, "Неверный город"
            
            self.used_cities.add(city.lower())
            self.last_char = city[-1].lower() if city[-1].lower() != 'ь' else city[-2].lower()
            self.scores[player_name] += 1
            
            players = list(self.players.keys())
            next_index = (players.index(player_name) + 1) % len(players)
            self.current_player = players[next_index]
            
            return True, f"Принято: {city}. Очков: {self.scores[player_name]}"

class GameServer:
    def __init__(self, host='localhost', port=5555):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.rooms = {}
        self.lock = threading.Lock()

    def start(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"Сервер запущен на {self.host}:{self.port}")
        
        while True:
            conn, addr = self.server_socket.accept()
            threading.Thread(target=self.handle_client, args=(conn, addr)).start()

    def handle_client(self, conn, addr):
        current_room = None
        player_name = None
        
        try:
            while True:
                data = self.receive_data(conn)
                if not data:
                    break

                command = data.get('command')
                args = data.get('args', [])

                if command == 'join':
                    room_name, player = args
                    success, message = self.join_room(room_name, player, conn)
                    if success:
                        current_room = room_name
                        player_name = player
                    self.send_response(conn, {'status': success, 'message': message})

                elif command == 'create':
                    room_name, player = args
                    success, message = self.create_room(room_name, player, conn)
                    if success:
                        current_room = room_name
                        player_name = player
                    self.send_response(conn, {'status': success, 'message': message})

                elif command == 'city':
                    city = args[0]
                    room = self.rooms.get(current_room)
                    if room and player_name:
                        success, message = room.process_turn(player_name, city)
                        self.broadcast(room, f"{player_name}: {city}\n{message}")
                        self.send_response(conn, {'status': success, 'message': message})

                elif command == 'ban':
                    target_player = args[0]
                    room = self.rooms.get(current_room)
                    if room and player_name == room.admin:
                        self.ban_player(room, target_player)
                        self.broadcast(room, f"Игрок {target_player} забанен")

                elif command == 'exit':
                    if current_room and player_name:
                        self.leave_room(current_room, player_name)
                    break

        finally:
            conn.close()
            if current_room and player_name:
                self.leave_room(current_room, player_name)

    def join_room(self, room_name, player_name, conn):
        with self.lock:
            if room_name not in self.rooms:
                return False, "Комната не найдена"
            if player_name in self.rooms[room_name].players:
                return False, "Имя уже занято"
            
            self.rooms[room_name].add_player(player_name, conn)
            return True, f"Присоединились к комнате {room_name}"

    def create_room(self, room_name, player_name, conn):
        with self.lock:
            if room_name in self.rooms:
                return False, "Комната уже существует"
            
            self.rooms[room_name] = GameRoom(room_name, player_name)
            self.rooms[room_name].add_player(player_name, conn)
            return True, f"Комната {room_name} создана"

    def leave_room(self, room_name, player_name):
        with self.lock:
            if room_name in self.rooms:
                self.rooms[room_name].remove_player(player_name)
                if not self.rooms[room_name].players:
                    del self.rooms[room_name]

    def ban_player(self, room, target_player):
        with self.lock:
            if target_player in room.players:
                room.remove_player(target_player)
                room.players[target_player].send(pickle.dumps({
                    'message': 'Вас исключили из комнаты'
                }))

    def broadcast(self, room, message):
        with self.lock:
            for player, conn in room.players.items():
                try:
                    self.send_response(conn, {'message': message})
                except:
                    continue

    def send_response(self, conn, data):
        conn.sendall(pickle.dumps(data))

    def receive_data(self, conn):
        try:
            return pickle.loads(conn.recv(4096))
        except:
            return None

if __name__ == "__main__":
    server = GameServer()
    server.start()