import socket
import pickle

SERVER_IP = "localhost"
SERVER_PORT = 5555

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

msg = "Hello there!"

client_socket.sendto(pickle.dumps(msg), (SERVER_IP, SERVER_PORT))
rec_msg = client_socket.recv(1024)
rec_msg = pickle.loads(rec_msg)
print(f'[RECEIVED] {rec_msg}')


client_socket.close()