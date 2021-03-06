import socket
from _thread import *
import sys

# 서버에 접속한 클라이언트 목록
client_sockets=[]

# 서버 IP 및 열어줄 포트
HOST = '127.0.0.1'
PORT = 9999

# 쓰레드에서 실행되는 코드
# 접속한 클라이언트마다 새로운 쓰레드가 생성되어 통신
def threaded(client_socket, addr):
    print('>> Connected by :', addr[0], ':', addr[1])

    # 클라이언트가 접속을 끊을 때 까지 반복합니다.
    while True:

        try:

            # 데이터가 수신되면 클라이언트에 다시 전송
            data = client_socket.recv(1024)
            if not data:
                print('>> Disconnected by ' + addr[0], ':', addr[1])
                break

            print('>> Received from ' + addr[0], ':', addr[1], data.decode())

            # 서버에 접속한 클라이언트들에게 채팅 보내기
            # 메세지를 보낸 본인을 제외한 서버에 접속한 클라이언트에게 메세지 보내기
            for client in client_sockets :
                if client != client_socket :
                    client.send(data)
        except ConnectionResetError as e:
            print('>> Disconnected by ' + addr[0], ':', addr[1])
            break
        except ConnectionAbortedError as e:
            print(">> ConnectionAbortedError")
            break
    if client_socket in client_sockets :
        client_sockets.remove(client_socket)
        print('remove client list : ',len(client_sockets))
    client_socket.close()
    
    
# 서버 소켓 생성
print(">> Server Start")
# AF_INET : IPv4를 사용한다는 의미
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# setsockopt(sock,level, optname, optval, optlen))
# setsockopt(소켓의 번호,옵션의 종류, 설정을 위한 소켓 옵션의 번호, 설정 값이 저장된 주소값, optval 버퍼의 크기))
# 소켓 옵션 설정
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST,PORT))
server_socket.listen()


try:
    while True:
        print('>> Wait')
        client_socket, addr = server_socket.accept()
        client_sockets.append(client_socket)
        start_new_thread(threaded, (client_socket, addr))
        print("참가자 수 : ", len(client_sockets))
        
except Exception as e :
    print ('에러는 : ',e)
except KeyboardInterrupt:
    print("KeyboradInterrupt!!! \n shutdown program!!!")
    server_socket.close()
    sys.exit(0)
