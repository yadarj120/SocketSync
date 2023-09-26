import socket
import pickle

SERVER_IP = "localhost"
SERVER_PORT = 5555

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((SERVER_IP, SERVER_PORT))

def handle_com():
    while True:
        msg, client_address = server_socket.recvfrom(1024)
        ac_msg = pickle.loads(msg)
        print(f'[HEARTBEAT RECEIVED] {ac_msg}')
        sen_msg = 'Heartbeat acknowledgement'
        server_socket.sendto(pickle.dumps(sen_msg), client_address)

handle_com()

server_socket.close()