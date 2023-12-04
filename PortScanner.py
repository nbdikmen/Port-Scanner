import socket

ip = "10.10.10.2" # Target ip address

for port in range(1,65535):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip,port))
        print(str(port), " opened")
    except Exception as e:
        print(str(port), " closed")
    finally:
        s.close()