import socket
import sys

def main():
    ip_port = ('192.168.100.2', 8080)

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ip_port)
    server.listen(5)

    print(f'[{ip_port[0]}] is listening on port {ip_port[1]}...')
    while True:
        try:
            (client_socket, address) = server.accept()
            print(f'[*] IP {address[0]}:{address[1]} conectou-se ao servidor!')
            while True:
                message = client_socket.recv(1024)
                if not message: break
                print(f'[{address[0]}]: {message.decode()}')
            print(f'[{address[0]}] desconectou-se do servidor!')

        except KeyboardInterrupt:
            print("[*] Execução finalizada.")
            break

if __name__ == '__main__':
    main()
    sys.exit(1)
