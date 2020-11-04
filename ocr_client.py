import time
from socket import *
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def client(host, port, data):
    tcp_client_socket = socket(AF_INET, SOCK_STREAM)
    tcp_client_socket.connect((host, port))
    file = open(data, 'rb')
    content = file.read()
    logger.info("Start time: %s", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    tcp_client_socket.send(content)
    # 此处与udp不同，客户端已经知道消息来自哪台服务器，不需要用recvfrom了
    recv_data = tcp_client_socket.recv(1024)
    if recv_data:
        logger.info("Got response: %s", recv_data.decode('utf-8'))
    else:
        logger.warning("Response is blank!!")
    logger.info("End time: %s", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    tcp_client_socket.close()


if __name__ == '__main__':
    client('localhost', 9000, 'chinese.jpg')
