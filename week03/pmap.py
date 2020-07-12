#扫描给定网络中存活的主机(通过ping来测试,有响应则说明主机存活)
import argparse
import json
import os
import sys
import subprocess
import socket
import threading
import time

net='192.168.10'
def ping(ip,):
    ret = subprocess.call("ping -c 2 -W 1 %s" % ip,shell=True,stdout=subprocess.PIPE)
    if ret == 0:
        aliveIPList.append(ip)
        return(1)
    elif ret == 1:
        return(0)
            
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
        
def scan(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 进行连接
        s.connect((host, port))
        # 连接成功就添加到开放端口列表
        openPortList.append(port)
    except:
        pass
    
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
        

        
if __name__ == '__main__':
    hostname=socket.gethostname()
    localHost =socket.gethostbyname(hostname)

    parser = argparse.ArgumentParser(description=" argparse of pmap")

    parser.add_argument('-n','--numconcur',help="number of concurrency", default='4',type=int)
    parser.add_argument('-f','--conntype',help="connection type", default='ping',type=str,choices=['ping','tcp'])
    parser.add_argument('-ip','--ip',help="set ip or ip range", default='localHost')
    parser.add_argument('-w','--filename',help="write to a file name", default='result.json')
 
    args = parser.parse_args()

    numconcur = args.numconcur
    conntype = args.conntype
    ip = args.ip
    filename = args.filename






#     while True:
    aliveIPList=[]
    try:
        creatThread(net)
        aliveIPList.sort()
#         print(aliveIPList)
        for aliveIP in aliveIPList:
            print("aliveIP:",aliveIP)
    except:
        print("Input Error！")
    
#     while True:
    openPortList = []
#         inputList = list(input().split())
    inputList = list((aliveIPList[0]+' '+'1000').split())
    print(inputList)
    start = time.time() # 计时开始

    print("Scaning……")
    # 扫描
#         try:
    scanThread(*inputList)
    print(*inputList)
    print("---------------------------")
    # openPortList.sort()
    name_emb = {}
    for openPort in openPortList:
        print(openPort, ": Open")
        key1=int(openPort)
        # name_emb.update(key1='open')
    name_emb=dict.fromkeys(openPortList,'open')
    print(name_emb)


    # name_emb = {'a':'1111','b':'2222','c':'3333','d':'4444'}
        
    output_dir = './'   
    emb_filename = os.path.join(output_dir, 'result.json')
 
    jsObj = json.dumps(name_emb)  
 
    with open(emb_filename, "w") as f:
        f.write(jsObj)
        f.close()

#     except:
#             print("Input Error！-2")
    end = time.time() # 计时结束
    print("time-consuming：%.2fs" %(end - start))
    print("---------------------------")

