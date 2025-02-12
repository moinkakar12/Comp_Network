import socket

HOST = '12.0.0.2'
PORT = 4300


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(1)
        print('Listening on port {}'.format(PORT))
        conn, addr = s.accept()
        with conn:
            print('Accepted connection from {}'.format(addr))
            while True:
                data = conn.recv(1024)
                if not data:
                    print('Connection closed')
                    break
                name = data.decode().split()[2]
                conn.sendall("Hello, {}".format(name).encode())


if __name__ == '__main__':
    main()
