import socket
import threading
import os
import time

host = "0.0.0.0"
port = 1234
path="E:\\programming network"

def handle_file_send(csock,caddr,files):
    for file in files:
        print(f"Sending to {caddr}>>>",file)
        filename = f"{path}\\{file}"
        filesize=os.path.getsize(filename)
        try:
            csock.send(str(filesize).encode())
            with open(filename,"rb") as f:
                bytes_read=f.read(filesize)
                time.sleep(1)
                csock.sendall(bytes_read)
        except socket.error as err:
            print(err)
    csock.close()
def main():
    server_socket=socket.socket()
    server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    server_socket.bind((host,port))
    server_socket.listen(3)
    print(f"Programming Network Course Files Server is Working at {host}:{port}")
    while True:
        try:
            csock,caddr=server_socket.accept()
            print(f"[*] NEW CLIENT CONNECTED at{caddr}")
            files = os.listdir(path)
            csock.send("*SEP*".join(files).encode())
            th=threading.Thread(target=handle_file_send,args=(csock,caddr,files))
            th.start()
        except socket.error as err:
            print(err)
            break
    server_socket.close()

if __name__=="__main__":
    main()
