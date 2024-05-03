
#python3 temp.py for 2 terminals
import socket
from socket import AF_INET, SOCK_STREAM

def display_local_info():
    """Display local host and port number."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as temp_socket:
        temp_socket.bind(('localhost', 0))
        host_name, port_name = temp_socket.getsockname()
        print("Local host:", host_name)
        print("Local port:", port_name)
    return host_name, port_name

def send_message(target_host, target_port, message, source_host,source_port=None):
    """Send a message to a target host and port."""
    client_socket = socket.socket(AF_INET, SOCK_STREAM)
    try:
        client_socket.bind((source_host, int(source_port)))  # Bind to the specified source port
        client_socket.connect((target_host, int(target_port)))
        client_socket.sendall(message.encode())
        print("Message has been sent")
    finally:
        client_socket.close()

def receive_messages(local_host, local_port):
    """Receive messages on a specified port."""
    server_socket = socket.socket(AF_INET, SOCK_STREAM)
    server_socket.bind((local_host, int(local_port)))
    server_socket.listen(1)
    print('Waiting for connection...')
    client_socket, addr = server_socket.accept()
    data = client_socket.recv(1024).decode()
    if data:
        print(f"Received message from {addr[0]}:{addr[1]}: {data}")
    client_socket.close()
    server_socket.close()

def user_interaction():
    """User interaction: Show local information, choose to connect or wait for messages."""
    local_host, local_port = display_local_info()
    while True:
        print("\nSelect a choice")
        print("1. Connect and send messages")
        print("2. Wait to receive messages")
        print("3. Exit the program")
        choice = input("Please make selection (1/2/3): ")
        if choice == '1':
            target_host = input("Enter target host: ")
            target_port = input("Enter target port: ")
            message = input("Enter message: ")
            source_host = input("Enter current host: ")
            source_port = input("Enter current port: ")
            send_message(target_host, target_port, message,source_host, source_port)
        elif choice == '2':
            receive_messages(local_host, local_port)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid request. Please input 1, 2, or 3.")

if __name__ == '__main__':
    user_interaction()


