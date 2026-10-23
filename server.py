# pyrefly: ignore[missing-import]
import Pyro5.api    
from product import Product

@Pyro5.api.expose
class ProductImpl(Product):
    def __init__(self, name, description, price):
        self._name = name
        self._description = description
        self._price = price

    def getName(self):
        return self._name

    def getDescription(self):
        return self._description

    def getPrice(self):
        return self._price

# Equivalent to Server.java
def main():
    try:
        print("Server is running...")
        
        # Create the Pyro daemon
        # Hosting on localhost port 9000 
        daemon = Pyro5.api.Daemon(host="127.0.0.1", port=9000)

        # Create objects from ProductImpl
        p1 = ProductImpl("Laptop", "Lenovo laptop", 800000.0)
        p2 = ProductImpl("Mobile", "MI 9 mobile", 24000.0)
        p3 = ProductImpl("Bag", "Branded bag", 800.0)
        p4 = ProductImpl("Charger", "MI Charger", 230.0)

        # Register the exported objects so the client can look them up by name
        daemon.register(p1, "laptop")
        daemon.register(p2, "ram")
        daemon.register(p3, "bag")
        daemon.register(p4, "charger")

        # Start the request loop to wait for clients
        daemon.requestLoop()

    except Exception as e:
        print(f"Server error: {e}")

if __name__ == "__main__":
    main()