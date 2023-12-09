import subprocess

server_ip = "192.168.56.1"


def client(server_ip):
    p = subprocess.Popen(
        ["iperf3", "-c", server_ip, "-i", "1"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    return p.communicate()


def parser():
    return


result, error = client(server_ip)
