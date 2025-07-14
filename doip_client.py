import socket
import struct
import logging

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')


class DoIPClient:
    def __init__(self, ip, port=13400):
        self.ip = ip
        self.port = port
        self.sock = None

    def connect(self):
        logging.info(f"Connecting to {self.ip}:{self.port}")
        self.sock = socket.create_connection((self.ip, self.port))
        logging.info("Connected successfully")

    def disconnect(self):
        if self.sock:
            self.sock.close()
            logging.info("Disconnected from ECU")

    def send(self, data: bytes):
        logging.info(f"Sending: {data.hex(' ').upper()}")
        self.sock.sendall(data)

    def receive(self):
        resp = self.sock.recv(4096)
        logging.info(f"Received: {resp.hex(' ').upper()}")
        return resp

    def routing_activation(self, logical_address: int):
        # 02 00 00 0E header + target address
        routing_request = struct.pack(">BBH6xH", 0x02, 0x00, 0x000E, logical_address)
        self.send(routing_request)
        return self.receive()

    def uds_request(self, data: bytes):
        doip_header = b"\x02"
        self.send(doip_header + data)
        return self.receive()
