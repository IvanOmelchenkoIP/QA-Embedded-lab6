import subprocess

server_ip = "192.168.56.1"

def client(server_ip):
    p = subprocess.Popen(["iperf3", "-c", server_ip, "-i", "1"])
    return 

def parser():
    return