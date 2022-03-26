import socket
import _thread
import sys

localhost = 'localhost'
ipv4 = socket.gethostbyname(socket.gethostname())
internet_server = ''

server = localhost
port = 5050

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    print(str(e))


s.listen(6)
print('Server started')

def threaded_client(conn):
    reply = ''
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode('utf-8')

            if not data:
                print('Player disconnected')
                break
            conn.sendall(str.encode(reply))
        except:
            break
    print('Either player disconnected or error happened')
    conn.close()

while True:
    conn, addr = s.accept()
    print('New player connected')

    _thread.start_new_thread(threaded_client, (conn,))