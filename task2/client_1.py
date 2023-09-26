import socket
import pickle
import time

SERVER_IP = "localhost"
SERVER_PORT = 5555

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

msg = "Hello there!"

while True:
    client_socket.sendto(pickle.dumps(msg), (SERVER_IP, SERVER_PORT))
    rec_msg = client_socket.recv(1024)
    rec_msg = pickle.loads(rec_msg)
    print(f'[HEARTBEAT ACKNOWLEDGEMENT] {rec_msg}')
    # wait for a second
    time.sleep(1)


client_socket.close()