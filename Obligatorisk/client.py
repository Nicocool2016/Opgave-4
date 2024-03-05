from socket import *

def main():
    server_name = "localhost"
    server_port = 12000
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect((server_name, server_port))

    try:
        command = input("Enter command (Random/Add/Subtract): ")
        client_socket.send(command.encode())

        response = client_socket.recv(1024).decode()
        print(response)

        numbers = input("Enter two numbers separated by space: ")
        client_socket.send(numbers.encode())

        result = client_socket.recv(1024).decode()
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        client_socket.close()