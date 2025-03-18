import socket
import pickle
import threading

class GameClient:
    def __init__(self, host='localhost', port=5555):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.running = False
        self.current_room = None

    def connect(self):
        self.sock.connect((self.host, self.port))
        self.running = True
        threading.Thread(target=self.receive_messages).start()

    def receive_messages(self):
        while self.running:
            try:
                data = self.sock.recv(4096)
                if not data:
                    break
                response = pickle.loads(data)
                print("\nСообщение сервера:", response.get('message'))
            except:
                break

    def send_command(self, command, *args):
        data = {
            'command': command,
            'args': args
        }
        self.sock.sendall(pickle.dumps(data))

    def start(self):
        self.connect()
        print("Доступные команды:")
        print("/create <room> <name> - создать комнату")
        print("/join <room> <name> - присоединиться к комнате")
        print("/city <город> - назвать город")
        print("/ban <name> - забанить игрока")
        print("/exit - выход")

        while self.running:
            try:
                user_input = input("> ").strip()
                if not user_input:
                    continue

                if user_input.startswith('/'):
                    parts = user_input[1:].split()
                    command = parts[0].lower()
                    args = parts[1:]

                    if command == 'exit':
                        self.send_command('exit')
                        self.running = False
                        break
                    elif command in ['create', 'join']:
                        if len(args) != 2:
                            print("Неверные аргументы")
                            continue
                        self.send_command(command, args[0], args[1])
                    elif command == 'city':
                        if len(args) != 1:
                            print("Укажите город")
                            continue
                        self.send_command('city', args[0])
                    elif command == 'ban':
                        if len(args) != 1:
                            print("Укажите имя игрока")
                            continue
                        self.send_command('ban', args[0])
                else:
                    print("Неизвестная команда")
            except KeyboardInterrupt:
                self.send_command('exit')
                self.running = False
                break

        self.sock.close()

if __name__ == "__main__":
    client = GameClient()
    client.start()