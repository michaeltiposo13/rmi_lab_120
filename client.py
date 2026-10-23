import Pyro5.api

def main():
    try:
        # Lookup the laptop object directly using Pyro's URI format on port 9000
        uri = "PYRO:laptop@127.0.0.1:9000"
        
        # Create a proxy object that acts as the local representation of the remote object
        laptop = Pyro5.api.Proxy(uri)
        
        # Call the remote methods
        laptopName = laptop.getName()
        laptopDescription = laptop.getDescription()
        price = laptop.getPrice()
        
        print(f"Name: {laptopName}")
        print(f"Description: {laptopDescription}")
        print(f"Price: {price}")
        
    except Exception as e:
        print(f"Exception in client side: {e}")

if __name__ == "__main__":
    main()