#importing Driver Class
import Driver

class Device:
    """Driver Class"""
    def __init__(self, Driver):
        self.driver = Driver

    def initialize(self):
        print("Initializing device...")
        self.driver.connect()

    def shutdown(self):
        print("Shutting down device...")
        self.driver.disconnect()

    def send_command(self, command):
        self.driver.send(command)
        response = self.driver.receive()
        return response == command
