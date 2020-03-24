import sys

from fbs_runtime.application_context.PyQt5 import ApplicationContext
from win32api import GetSystemMetrics
import win32gui
from PyQt5.QtCore import QProcess
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QPushButton, QLineEdit


class DriverStationFrame(QWidget):

    def _getTopLevelWindows(self):
        """Get all top-level Windows (visible and invisible)"""
        windows = []
        win32gui.EnumWindows(self._enumWindowsCallback, windows)
        return windows

    def _enumWindowsCallback(self, hwnd, windows):
        className = win32gui.GetClassName(hwnd)
        text = win32gui.GetWindowText(hwnd)
        windows.append((hwnd, className, text))

    def __init__(self):
        super().__init__()

        self.process = QProcess()

        # self.launch_button = QPushButton('Launch', self)
        # self.launch_button.clicked.connect(self.on_launch)

        self.resize_button = QPushButton('Resize')
        self.resize_button.clicked.connect(self.on_resize)

        self.dashboard_input = QLineEdit()
        self.dashboard_input.setText("Shuffleboard")
        self.driver_station_input = QLineEdit()
        self.driver_station_input.setText("DriverStation")

        layout = QHBoxLayout()
        layout.addWidget(QLabel('Dashboard Name'))
        layout.addWidget(self.dashboard_input)
        layout.addWidget(QLabel('Driver Station'))
        layout.addWidget(self.driver_station_input)
        # layout.addWidget(self.launch_button)
        layout.addWidget(self.resize_button)
        self.setLayout(layout)
        self.setWindowTitle('Driverstation Frame')
        self.show()

    # def on_launch(self):
    #     print("Launching Sublime")
    #     self.process.start("\"C:\\Program Files\\Sublime Text 3\\sublime_text.exe\"")
    #     print(self.process.processId())

    def on_resize(self):
        windows = self._getTopLevelWindows()
        dashboard = None
        driver_station = None

        for window in windows:
            if window[2] == self.dashboard_input.text():
                dashboard = window
            elif window[2] == self.driver_station_input.text():
                driver_station = window

        print(dashboard)
        print(driver_station)

        print(GetSystemMetrics(0), GetSystemMetrics(1))
        win32gui.MoveWindow(dashboard[0], -8, -32, GetSystemMetrics(0) + 16, GetSystemMetrics(1) - 200, False)
        win32gui.SetForegroundWindow(dashboard[0])
        win32gui.SetForegroundWindow(driver_station[0])


if __name__ == '__main__':
    ctx = ApplicationContext()
    ex = DriverStationFrame()
    ctx.app.exec_()
