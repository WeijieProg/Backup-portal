class Connection:
    def __init__(self, ip="", port=""):
        self.__ip = "0.0.0.0"
        self.__port = "0"

    def get_ip(self):
        return self.__ip

    def get_port(self):
        return self.__port

    def set_ip(self, ip):
        self.__ip = ip

    def set_port(self, port):
        self.__port = port
