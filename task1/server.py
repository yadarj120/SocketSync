import socket
import pickle

SERVER_IP = "localhost"
SERVER_PORT = 5555

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((SERVER_IP, SERVER_PORT))

msg, client_address = server_socket.recvfrom(1024)
ac_msg = pickle.loads(msg)
print(f'[RECEIVED] {ac_msg}')
server_socket.sendto(msg, client_address)

server_socket.close()