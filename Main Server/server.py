import socket
import threading

# Define server address and port
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 12345
kill = []


# Maintain a list of connected clients
connected_clients = []

def reciever(client_socket):
    while len(kill) == 0:
        returner = client_socket.recv(1024)
        print(returner)

def handle_client(client_socket, client_address):
    connected_clients.append(client_socket)
    print(f"[*] Accepted connection from {client_address[0]}:{client_address[1]}")
    
    while True:
        print(connected_clients)
        recieverThread = threading.Thread(target=reciever, args=(client_socket,))
        recieverThread.start()

        input_server = input("Instructions: ")
        if input_server == "exit":
            kill.append("")
            break
        print(f"[*] Sending message to all clients: {input_server}")
        for client in connected_clients:
            client.sendall(input_server.encode())


    # Close the connection
    client_socket.close()
    connected_clients.remove(client_socket)
    print(f"[*] Connection with {client_address[0]}:{client_address[1]} closed")

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address and port
server_socket.bind((SERVER_HOST, SERVER_PORT))

# Listen for incoming connections
server_socket.listen(5)
print(f"[*] Listening on {SERVER_HOST}:{SERVER_PORT}")

while True:
    
    client_socket, client_address = server_socket.accept()
    
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()

