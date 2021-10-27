import socket
import time

HOST = "127.0.0.1" # LOOPBACK IP
INTERFACE = "255.255.255.255"
MULTICAST = "224.0.0.1"
PORT = 50005

import argparse
def parser():
    parser = argparse.ArgumentParser(description="<< socket example:  >>"+
                                     "\n2021.10.27. created by Jess"+
                                     "\nrun in only local pc")
    parser.add_argument("--network", type=str, help="choose server or client")
    parser.add_argument("--L3", type=str, help="choose TCP or UDP")
    return parser.parse_args()

# TCP example, SOCK_STREAM
def run_TCP_server():
    try:
        tcpip_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcpip_sock.bind((HOST, PORT))
        tcpip_sock.listen()
        while True:
            client_socket, client_addr = tcpip_sock.accept() # wait until connect
            msg = client_socket.recv(1024)
            print("[{}] message : {}".format(client_addr,msg))
            
    except KeyboardInterrupt:
        tcpip_sock.close()

def run_TCP_clinet():
    try:
        tcpip_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcpip_sock.bind((HOST, PORT))
        tcpip_sock.connect(HOST)
        while True:
            send_msg = input("send Message: ")
            tcpip_sock.send(send_msg.encode())
            
    except KeyboardInterrupt:
        tcpip_sock.close()
        
# UDP example, SOCK_DGRAM
def run_UDP_server():
    try:
        udpip_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udpip_sock.bind((HOST, PORT))
        while True:
            data, addr = sock.recvfrom(1024)
            data = data.decode().upper()
            udpip_sock.sendto(data.encode(), (HOST,PORT))
        
    except KeyboardInterrupt:
        udpip_sock.close()
    
def run_UDP_client():
    try:
        udpip_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udpip_sock.bind((HOST, PORT))
        while True:
            send_msg = input("send Message: ")
            udpip_sock.sendto(send_msg.encode(),(HOST,PORT))
            recvMsg, addr = sock.recvfrom(1024)
            print(recvMsg.decode())
        
    except KeyboardInterrupt:
        udpip_sock.close()
        
if __name__ == "__main__":
    args = parser()
    
    if args.network == "server":
        if args.L3 == "TCP":
            run_TCP_server()
        elif args.L3 == "UDP":
            run_UDP_server()
            
    elif args.network == "client":
        if args.L3 == "TCP":
            run_TCP_client()
        elif args.L3 == "UDP":
            run_UDP_client()