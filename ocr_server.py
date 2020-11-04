#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys, getopt
import logging
from abc import ABC

import easyocr
from twisted.internet import reactor
from twisted.internet.protocol import ServerFactory
from twisted.protocols.basic import LineReceiver

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def server(port):
    class SimpleServerFactory(ServerFactory):
        reader = None

        def __init__(self, reader):
            self.reader = reader

    class SimpleReceiver(LineReceiver, ABC):
        def connectionMade(self):
            logger.info('Got connection from %s', self.transport.client)

        def connectionLost(self, reason):
            logger.info('%s disconnected', self.transport.client)

        def dataReceived(self, data):
            if type(data) == bytes:
                logger.info("Received data ...")
            else:
                logger.info("Received data:%s", data)

            result = reader.readtext(data, detail=0)
            str = '';
            for item in result:
                str = str + item
            self.sendLine(str.encode())
            logger.info("Send response: %s", str)

    # need to run only once to load model into memory
    reader = easyocr.Reader(['ch_sim', 'en'])
    factory = SimpleServerFactory(reader)
    factory.protocol = SimpleReceiver
    reactor.listenTCP(port, factory)
    logger.info("TCP server started on port(s): %s ..." % (port))
    reactor.run()


def main(argv):
    port = 0
    if len(argv) == 0:
        print('usage: ocr_server.py -p <port>')
        sys.exit(1)
    try:
        opts, args = getopt.getopt(argv, "?hp:", ["port="])
    except getopt.GetoptError:
        print('usage: ocr_server.py -p <port>')
        sys.exit(2)
    if len(opts) == 0:
        print('usage: ocr_server.py -p <port>')
        sys.exit(3)
    for opt, arg in opts:
        if opt == '-h':
            print('usage: ocr_server.py -p <port>')
            sys.exit()
        elif opt in ("-p", "--port"):
            port = arg
        else:
            print('usage: ocr_server.py -p <port>')
            sys.exit(4)
    if int(port) == 0:
        print('usage: ocr_server.py -p <port>')
        sys.exit(5)

    server(int(port))


if __name__ == '__main__':
    main(sys.argv[1:])
