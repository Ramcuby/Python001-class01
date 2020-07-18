#扫描给定网络中存活的主机(通过ping来测试,有响应则说明主机存活)
import argparse
import json
import os
import ipaddress
import functools
import sys
import multiprocessing
import subprocess
import shlex
import socket
import threading
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

print_lock = multiprocessing.Lock()

net='192.168.10'
def validate_ip(ip):
    return ipaddress.IPv4Address(ip)

def get_ip_list_in_range(start,end):
    for ips in ipaddress.summarize_address_range(ipaddress.IPv4Address(start),ipaddress.IPv4Address(end)):
        yield from ips

def check_host_with_ping(ip):
    result = subprocess.run(
        shlex.split("ping {ip} -c 3 -t 3".format(ip=str(ip))),
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    if result.returncode == 0:
        with print_lock:
            print(ip)
    # ret = subprocess.call("ping -c 2 -W 1 %s" % ip,shell=True,stdout=subprocess.PIPE)
    # if ret == 0:
    #     aliveIPList.append(ip)
    #     return(1)
    # elif ret == 1:
    #     return(0)
            
def creatThread(net):
    myThread = []
    aliveIPList=[]
    # 创建线程
    for i in range(1, 255):
        ip=net+"."+str(i)
        t = threading.Thread(target=ping, args=(ip,))
        myThread.append(t)
    # 开始线程
    for i in range(len(myThread)):
        myThread[i].start()
    # 结束线程并等待
    for i in range(len(myThread)):
        myThread[i].join()
        
def check_port_with_tcp(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(3)
    if s.connect_ex((str(host),port))==0:
        with print_lock:
            print(port)    
        # 进行连接
        # s.connect((host, port))
        # 连接成功就添加到开放端口列表
        # openPortList.append(port)
    # except:
        # pass
    
def scanThread(host, portMax):
    myThread = []

    # 创建线程
    for i in range(1, int(portMax) + 1):
        t = threading.Thread(target=scan, args=(host, i))
        myThread.append(t)
    # 开始线程
    for i in range(len(myThread)):
        myThread[i].start()
    # 结束线程并等待
    for i in range(len(myThread)):
        myThread[i].join()
        
def main(args):
    if "ping" == args["f"]:
        ip_list = get_ip_list_in_range(*(validate_ip(ip) for ip in args["ip"].split("-")))
        with ProcessPoolExecutor(args["n"]) as pool:
            pool.map(check_host_with_ping,ip_list)
    elif "tcp" == args["f"]:
        with ThreadPoolExecutor(args["n"]) as pool:
            pool.map(functools.partial(check_port_with_tcp,validate_ip(args["ip"])),range(1,1025))
        
        
if __name__ == '__main__':
    # hostname=socket.gethostname()
    # localHost =socket.gethostbyname(hostname)

    parser = argparse.ArgumentParser(prog="pmap",description=" argparse of pmap")

    parser.add_argument("-n",help="number of concurrency", type=int,nargs="?",required=True)
    parser.add_argument("-f",nargs="?",help="connection type", default="ping",choices=["ping","tcp"],required=True)
    parser.add_argument("-ip",help="set ip or ip range", default="localHost",required=True)
    parser.add_argument("-w",help="write to a file name", default="result.json")
    args = parser.parse_args()
    # print(args)
    
    main(vars(args))

# #     while True:
#     aliveIPList=[]
#     try:
#         creatThread(net)
#         aliveIPList.sort()
# #         print(aliveIPList)
#         for aliveIP in aliveIPList:
#             print("aliveIP:",aliveIP)
#     except:
#         print("Input Error！")
    
#     openPortList = []
#     inputList = list((aliveIPList[0]+' '+'1000').split())
#     print(inputList)
#     start = time.time() # 计时开始

#     print("Scaning……")

#     scanThread(*inputList)
#     print(*inputList)
#     print("---------------------------")
#     name_emb = {}
#     for openPort in openPortList:
#         print(openPort, ": Open")
#         key1=int(openPort)
#     name_emb=dict.fromkeys(openPortList,'open')
#     # print(name_emb)
        
#     output_dir = './'   
#     emb_filename = os.path.join(output_dir, filename)
 
#     jsObj = json.dumps(name_emb)  
 
#     with open(emb_filename, "w") as f:
#         f.write(jsObj)
#         f.close()

# #     except:
# #             print("Input Error！-2")
#     end = time.time() # 计时结束
#     print("time-consuming：%.2fs" %(end - start))
#     print("---------------------------")

