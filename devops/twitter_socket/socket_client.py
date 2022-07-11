import socket
import json
if __name__ == '__main__':
    try:
        HOST = '127.0.0.1'
        PORT = 5555
        tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        dest = (HOST, PORT)
        tcp.connect(dest)
        msg = ''
        while not 'lula' in msg :
            msg_temp = tcp.recv(4096*4)
            #msg = json.loads(msg_temp)
            print(msg_temp)
        tcp.close()
    except Exception as e:
        print('parou')
        print(e)
    finally:
        tcp.close()