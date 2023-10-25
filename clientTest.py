import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Please provide the server IP:")
input_server_ip = input()
intput_server_ip = str(input_server_ip)

client.connect((input_server_ip, 8080))

client.sendall('I am CLIENT\n'.encode())
from_server = client.recv(4096)
client.close()
print(from_server)
