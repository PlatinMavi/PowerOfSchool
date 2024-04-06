import socket
import threading
import time

def handle_backproccesing(data,client_socket):
    print(f"Received: {data.decode()}")
    response = "complete"
    time.sleep(3)
    client_socket.sendall(response.encode())
    print("done")
    
# Define server address and port
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 12345

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((SERVER_HOST, SERVER_PORT))
print(f"[*] Connected to {SERVER_HOST}:{SERVER_PORT}")

# Receive messages from server and report back
while True:
    data = client_socket.recv(1024)
    if not data:
        break

    backprocces_Thread = threading.Thread(target=handle_backproccesing, args=(data, client_socket))
    backprocces_Thread.start()

# Close the connection
client_socket.close()
