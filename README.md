# Python RMI Lab

This is how to run our python rmi lab.

## Files

* `product.py` - the interface / abstract class
* `server.py` - the server that hosts the objects
* `client.py` - the client that connects and calls the methods

## How to Run

First install Pyro5:

```
pip install Pyro5
```

Open 2 terminals.

Terminal 1 - run the server first:

```
python server.py
```

Terminal 2 - then run the client:

```
python client.py
```

You should see this in the client:

```
Name: Laptop
Description: Lenovo laptop
Price: 800000.0
```

To stop the server, just press `Ctrl + C`.
