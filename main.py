import socket
import threading
from queue import Queue

def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False

def fill_queue(portList):
    for port in portList:
        queue.put(port)

def worker():
    while not queue.empty():
        port = queue.get()
        if portscan(port):
            openPorts.append(port)

target = input("Enter an IP address> ")
queue = Queue()
openPorts = []

startPort = int(input("Enter a port to start the scan at> "))
endPort = int(input("Enter a port to end the scan at> "))

if startPort > endPort:
    startPort, endPort = endPort, startPort

portList = [x for x in range (startPort, endPort)]
fill_queue(portList)

threadList = []

threadAmount = int(input("How many threads do you want to allocate> "))

for thread in range(threadAmount):
    thread = threading.Thread(target=worker)
    threadList.append(thread)

for thread in threadList:
    thread.start()

for thread in threadList:
    thread.join()

if not openPorts:
    print("No open ports")
else:
    for port in openPorts:
        print(f"Port {port} is open!")