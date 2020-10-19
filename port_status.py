import socket
import sys #to receive arguement
import time # to calculate how much time taken to scan
import threading

usage = "python3 port_status.py TARGET START_PORT END_PORT"#four arguements are here 1.port_status.py 2.TARGET 3.START_PORT 4.END_PORT

print("-"*70)
print("Python Simple Port Scanner")
print("-"*70)

if(len(sys.argv)!=4):
    print(usage)
    sys.exit()

try:
    target = socket.gethostbyname(sys.argv[1])#convert host name to ip address nd get stored in target variable i.e [1]
except socket.gaierror:
    print("Name resolution error")
    sys.exit()

start_port = int(sys.argv[2])
end_port = int(sys.argv[3])

print("Scanning target",target)

def scan_port(port):
    #print("Scanning port: ",port)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# for TCP - SOCK_STREAM
    conn = s.connect_ex((target, port))
    s.settimeout(2)
    if (not conn):
        print("Port {} is open".format(port))
    s.close()

for port in range(start_port, end_port+1):#+1 coz we hav to go till last integer

    thread = threading.Thread(target = scan_port, args =(port,))
    thread.start()
    
