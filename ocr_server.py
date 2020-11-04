from abc import ABC

from twisted.internet import reactor
from twisted.internet.protocol import Factory
from twisted.protocols.basic import LineReceiver
import easyocr
import logging

logging.basicConfig(filename='ocr.log', filemode='a', level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def server(port):
    class SimpleReceiver(LineReceiver, ABC):
        def connectionMade(self):
            logger.info('Got connection from', self.transport.client)

        def connectionLost(self, reason):
            logger.info(self.transport.client, 'disconnected')

        def dataReceived(self, line):
            logger.info("=========Received data=========")
            reader = easyocr.Reader(['ch_sim', 'en'])  # need to run only once to load model into memory
            result = reader.readtext(line, detail=0)
            str = '';
            for item in result:
                str = str + item
            self.sendLine(str.encode())
            logger.info("=========Send response=========")

    factory = Factory()
    factory.protocol = SimpleReceiver
    reactor.listenTCP(port, factory)
    logger.info("TCP server started on port(s): %s ..." % (port))
    reactor.run()


if __name__ == '__main__':
    server(9000)
