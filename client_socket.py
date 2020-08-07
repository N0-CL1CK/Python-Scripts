import sys
import socket

def main():
    if (len(sys.argv) == 3):
        ip_port = (sys.argv[1], sys.argv[2])
    elif (len(sys.argv) == 2):
        ip_port = (sys.argv[1], 8080)
    elif (len(sys.argv) == 1):
        ip_port = ('192.168.100.2', 8080)
    else:
        print(f'[*] Examples:')
        print(f'client_socket.py <ip number> <port>')
        print(f'client_socket.py <ip number>')
        print(f'client_socket.py')
        print(f'\n\n[*] Default configs:\nIP => 192.168.100.2\nPORT => 8080')

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ip_port)

    print(f'[*] Conectado com sucesso no HOST [{ip_port[0]}:{ip_port[1]}]')
    print(f'[*] Para se desconectar use CTRL+C')

    try:
        message = input("You => ")
        while message != '\x18':
            client.send(message.encode('utf-8'))
            message = input("You => ")
            
    except KeyboardInterrupt:
        client.close()
        sys.exit(1)


if __name__ == '__main__':
    main()
    sys.exit(1)