import os
import sys

from PyQt6.QtGui import QIcon, QAction
from PyQt6.QtWidgets import (
    QApplication,
    QMenu,
    QSystemTrayIcon,
)

basedir = os.path.dirname(__file__)

app = QApplication(sys.argv)
app.setQuitOnLastWindowClosed(False)

# Create the icon
icon = QIcon(os.path.join(basedir, "icon.png"))

# Create the tray
tray = QSystemTrayIcon()
tray.setIcon(icon)
tray.setVisible(True)

# Create the menu
menu = QMenu()
action = QAction("A menu item")
menu.addAction(action)

# Add a Quit option to the menu.
quit = QAction("Quit")
quit.triggered.connect(app.quit)
menu.addAction(quit)

# Add the menu to the tray
tray.setContextMenu(menu)

app.exec()
