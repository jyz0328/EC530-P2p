
#python3 app.py for 2 terminals
import socket
from socket import AF_INET, SOCK_STREAM

def display_local_info():
    """显示本机的主机名和建议的端口号"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as temp_socket:
        temp_socket.bind(('localhost', 0))
        host_name, port_name = temp_socket.getsockname()
        print("当前主机名:", host_name)
        print("当前使用的端口号", port_name)
    
    return host_name,port_name  # 返回这个端口号以便后续使用

def send_message(ip_address, port, message):
    """向指定的IP地址和端口发送消息"""
    client_socket = socket.socket(AF_INET, SOCK_STREAM)
    try:
        client_socket.connect((ip_address, int(port)))
        client_socket.sendall(message.encode())
        print("消息已发送")
    finally:
        client_socket.close()

def receive_messages(address,port):
    """在指定端口接收消息"""
    server_socket = socket.socket(AF_INET, SOCK_STREAM)
    server_socket.bind((address, int(port)))
    server_socket.listen(1)
    print(f"等待在端口 {address, port} 上接收消息...")
    client_socket, addr = server_socket.accept()
    data = client_socket.recv(1024)
    if data:
        print(f"从 {addr} 处收到消息: {data.decode()}")
    client_socket.close()
    server_socket.close()

def user_interaction():
    """用户交互：展示本机信息，选择连接或等待接收消息"""
    local_address, local_port = display_local_info()  # 获取建议端口号并保存
    #也想展示local ip address
    print("1. Connect and send message")
    print("2. Waiting to receive messages")
    choice = input("Do you want to connect or wait? (1/2): ")
    if choice == '1':
        ip_address = input("输入目标IP地址: ")
        port = input("请输入端口号: ")
        message = input("输入要发送的消息: ")
        send_message(ip_address, port, message)
    elif choice == '2':
        print('Waiting for a connection...')
        receive_messages(local_address,local_port)  # 使用之前显示的端口号进行监听

if __name__ == '__main__':
    user_interaction()
