# Rportscan

### 功能
* 解析目标 ip

* 识别存活主机

* 端口扫描

  * async tcp 扫描存活主机端口

  * masscan 扫描存活主机端口

* 服务识别

### 安装必要模块
* 安装 nmap [(Download)](https://nmap.org/dist/?C=M&O=D)

* 如果是 win 的话安装 winpcap [(Download)](https://www.winpcap.org/install/default.htm)

* pip3 install -r requirements.txt

### 参数
```
usage: portscan.py [-h] [-i TARGET] [-iL TARGET_FILENAME] [-st {tcp,masscan}]
                   [-t THREAD] [-r RATE] [-c] [-a] [-s]

optional arguments:
  -h, --help           show this help message and exit
  -i TARGET            Target(1.1.1.1 or 1.1.1.1/24 or 1.1.1.1-4)
  -iL TARGET_FILENAME  Target file name
  -st {tcp,masscan}    Port scan type, default is masscan
  -t THREAD            The number of threads, default is 30 threads
  -r RATE              Port scan rate, default is 1000
  -c                   Check host is alive before port scan, default is False
  -a                   Is full port scanning, default is False
  -s                   Whether to get port service, default is False
```

### 使用
```
➜  python3 portscan.py -i 59.108.35.198 -st tcp -c -s
[16:15:34] [INFO] [*] Check Live Host...
[16:15:34] [INFO] all host: 1, live host: 1
[16:15:34] [INFO] [*] PortScan...
[16:15:34] [INFO] start async tcp port scan...
[16:15:34] [INFO] 59.108.35.198    22    open
[16:15:34] [INFO] 59.108.35.198    80    open
[16:15:39] [INFO] [*] Get the service of the port...
[16:15:45] [INFO] 59.108.35.198    22    open    ssh     OpenSSH         6.6.1p1 Ubuntu2ubuntu2.11
[16:15:45] [INFO] 59.108.35.198    80    open    http    Apache httpd    2.4.7
```

### 引用
```
import sys
sys.path.append('/path/to/Rsbrute')

from Rpscan import CheckHostLive
chl = CheckHostLive(ip_list=["59.108.35.243"])
live_host = chl.run()
print(live_host)

from Rpscan import PortScan
ps = PortScan(ip_list=['59.108.35.243'], all_ports=False, rate=2000)
port_open_dict = ps.masscan_scan()
port_open_dict = ps.async_tcp_port_scan()
print(port_open_dict)

from pprint import pprint
from Rpscan import NmapGetPortService
ngps = NmapGetPortService(ip_port_dict={'59.108.35.243': [80, 22]}, thread_num=10)
port_service_list = ngps.run()
pprint.pprint(a)
```