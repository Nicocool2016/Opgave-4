from socket import *
import random
import threading

def handle_client(connection_socket):
    try:
        while True:
            command = connection_socket.recv(1024).decode()

            if command.startswith("Random"):
                connection_socket.send("2: Input numbers".encode())
                numbers = connection_socket.recv(1024).decode().split()
                random_number = random.randint(int(numbers[0]), int(numbers[1]))
                connection_socket.send(f"4: {random_number}".encode())
            elif command.startswith("Add"):
                connection_socket.send("2: Input numbers".encode())
                numbers = connection_socket.recv(1024).decode().split()
                sum_result = int(numbers[0]) + int(numbers[1])
                connection_socket.send(f"4: {sum_result}".encode())
            elif command.startswith("Subtract"):
                connection_socket.send("2: Input numbers".encode())
                numbers = connection_socket.recv(1024).decode().split()
                subtract_result = int(numbers[0]) - int(numbers[1])
                connection_socket.send(f"4: {subtract_result}".encode())
            else:
                connection_socket.send("Invalid command".encode())
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        connection_socket.close()

def main():
    server_port = 12000
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind(('localhost', server_port))
    server_socket.listen(5)
    print("The server is ready to receive")

    while True:
        connection_socket, addr = server_socket.accept()
        print(f"Connected to {addr}")
        client_handler = threading.Thread(target=handle_client, args=(connection_socket,))
        client_handler.start()
        
        

