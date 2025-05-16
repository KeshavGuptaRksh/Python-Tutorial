
'''
Structural Patterns: Concerned with object composition

Adapter, Decorator, Facade, Composite, Proxy
'''
class EuropeanSocket:
    def voltage(self):
        return 230

class USASocket:
    def voltage(self):
        return 120

class SocketAdapter:
    def __init__(self, socket):
        self.socket = socket
    
    def voltage(self):
        return f"Adapted {self.socket.voltage()}V"

euro_socket = EuropeanSocket()
adapter = SocketAdapter(euro_socket)
print(adapter.voltage())  # Adapted 230V