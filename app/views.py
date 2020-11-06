# -*- coding: UTF-8 -*-
from django.shortcuts import render
from socket import *


# Create your views here.
def index(request):
    result = ""
    return render(request, "index.html", {"result": result})


def ocr(request):
    tcp_client_socket = socket(AF_INET, SOCK_STREAM)
    tcp_client_socket.connect(('localhost', 9000))
    img = request.FILES.get("img")
    data = img.read()
    tcp_client_socket.send(data)
    # 此处与udp不同，客户端已经知道消息来自哪台服务器，不需要用recvfrom了
    recv_data = tcp_client_socket.recv(1024)
    result = recv_data.decode('utf-8')
    tcp_client_socket.close()
    return render(request, "index.html", {"result": result})
