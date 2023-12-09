import subprocess
import re

decode_format = "utf-8"
server_ip = "192.168.56.1"


def client(server_ip):
    p = subprocess.Popen(
        ["iperf3", "-c", server_ip, "-i", "1"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    return p.communicate()


def parser(result, error):
    if error:
        print(error)
        return
    result = re.sub("\[.*\]", "", result.strip())
    lines = result.split("\n")
    for line in lines:
        if re.search("^\D*$", line):
            result = re.sub(line, "*", result)
    res_section = result.split("*")[1].strip()
    lines = res_section.split("\n")
    result_dict = []
    for line in lines:
        line_dict = {}
        params = re.split("\s+", line.strip())
        line_dict['Interval'] = params[0]
        line_dict['Transfer'] = params[2]
        line_dict['Bitrate'] = params[4]
        line_dict['Retr'] = params[6]
        line_dict['Cwnd'] = params[7]
        result_dict.append(line_dict)
    return result_dict


result, error = client(server_ip)
parser(result.decode(decode_format), error.decode(decode_format))
