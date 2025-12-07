import paramiko

class Node:
    def __init__(self, ip: str, id: int):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(hostname=ip, port=22,
                         username='kangqihan', password='kangqihan110')
        self.ip = ip
        self.id = id