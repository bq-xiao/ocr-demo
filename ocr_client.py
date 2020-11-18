#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys, getopt
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
    file.close()
    logger.info("Start time: %s", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    tcp_client_socket.send(content)
    # 此处与udp不同，客户端已经知道消息来自哪台服务器，不需要用recvfrom了
    recv_data = tcp_client_socket.recv(10240)
    if recv_data:
        logger.info("Got response: %s", recv_data.decode('utf-8'))
    else:
        logger.warning("Response is blank!!")
    logger.info("End time: %s", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    tcp_client_socket.close()


def main(argv):
    host = ''
    port = 0
    image = ''
    if len(argv) == 0:
        print('usage: ocr_client.py -h <host> -p <port> -i <image>')
        sys.exit(1)
    try:
        # options 后的冒号 : 表示如果设置该选项，必须有附加的参数，否则就不附加参数
        opts, args = getopt.getopt(argv, "?h:p:i:", ["host=", "port=", "image="])
    except getopt.GetoptError:
        print('usage: ocr_client.py -h <host> -p <port> -i <image>')
        sys.exit(2)
    if len(opts) == 0:
        print('usage: ocr_client.py -h <host> -p <port> -i <image>')
        sys.exit(3)
    for opt, arg in opts:
        if opt == '?':
            print('usage: ocr_client.py -h <host> -p <port> -i <image>')
            sys.exit()
        elif opt in ("-h", "--host"):
            host = arg
        elif opt in ("-p", "--port"):
            port = arg
        elif opt in ("-i", "--image"):
            image = arg
        else:
            print('usage: ocr_client.py -h <host> -p <port> -i <image>')
            sys.exit(4)
    if len(host) == 0:
        print('usage: ocr_client.py -h <host> -p <port> -i <image>')
        sys.exit(5)
    if int(port) == 0:
        print('usage: ocr_client.py -h <host> -p <port> -i <image>')
        sys.exit(6)
    if len(image) == 0:
        print('usage: ocr_client.py -h <host> -p <port> -i <image>')
        sys.exit(7)
    client(host, int(port), image)


if __name__ == '__main__':
    main(sys.argv[1:])
