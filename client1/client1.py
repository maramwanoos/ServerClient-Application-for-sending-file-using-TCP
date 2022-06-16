import socket
import os
from colorama import Fore

def main():
    c_socket=socket.socket()
    socket.timeout(5)
    c_socket.connect(("127.0.0.1",1234))
    files_names=c_socket.recv(1024).decode()
    files=files_names.split("*SEP*")
    print(files)
    try:
        os.mkdir("../Received")
    except:
        pass
    for file in files:
        buffer_size=int(c_socket.recv(1024).decode())
        print("Recieving",Fore.RED,file,Fore.BLUE, buffer_size/10**6,"MB",Fore.RESET)
        data=c_socket.recv(buffer_size)
        path=os.path.join("../Received", file)
        with open(path,"wb") as f:
            f.write(data)
            f.close()
    print(Fore.GREEN,"All Files Recived")
    c_socket.close()

if __name__=="__main__":
    main()