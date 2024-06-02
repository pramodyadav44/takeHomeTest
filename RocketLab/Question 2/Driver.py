from abc import ABC, abstractmethod

"Using Abstraction"

class Driver(ABC):
    """Driver class passing abstraction"""
    
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

    @abstractmethod
    def send(self, data):
        pass

    @abstractmethod
    def receive(self):
        pass

class EthernetDriver(Driver):
    """Ethernet Driver Class"""
    
    def connect(self):
        print("Connecting via Ethernet...")
        

    def disconnect(self):
        print("Disconnecting Ethernet...")
        

    def send(self, data):
        print(f"Sending over Ethernet: {data}")
        

    def receive(self):
        print("Receiving over Ethernet...")
        return "QUICK"

class RS422Driver(Driver):
    """ RS422 Driver Class"""

    def connect(self):
        print("Connecting via RS-422...")
        

    def disconnect(self):
        print("Disconnecting RS-422...")
        

    def send(self, data):
        print(f"Sending over RS-422: {data}")
        

    def receive(self):
        print("Receiving over RS-422...")
        return "FULL"

class RS485Driver(Driver):
    """RS485 Driver Class"""
    
    def connect(self):
        print("Connecting via RS-485...")
    

    def disconnect(self):
        print("Disconnecting RS-485...")
    

    def send(self, data):
        print(f"Sending over RS-485: {data}")
    

    def receive(self):
        print("Receiving over RS-485...")
        return "FULL"
