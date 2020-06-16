#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Author: reber
@Mail: reber0ask@qq.com
@Date: 2019-08-24 17:55:54
@LastEditTime : 2020-06-16 13:18:01
'''
import time
from concurrent.futures import ThreadPoolExecutor
# from threading import Lock
from nmap import nmap

from libs.data import config

# lock = Lock()

class NmapGetPortService(object):
    """获取端口运行的服务"""

    def __init__(self, ip_port_dict):
        super(NmapGetPortService, self).__init__()
        self.ip_port_dict = ip_port_dict
        self.thread_num = config.thread
        self.port_service_list = dict()
        self.logger = config.logger
        self.init_thread()
        self.flag = True

    def init_thread(self):
        '''设定线程数量'''
        if len(self.ip_port_dict) < self.thread_num:
            self.thread_num = len(self.ip_port_dict)

    def nmap_get_service(self, ip_port):
        '''nmap 获取端口的 service'''
        if self.flag:
            ip, port = ip_port
            try:
                nm_scan = nmap.PortScanner()
                args = '-p T:'+str(port)+' -Pn -sT -sV -n'
                # args = '-p T:'+str(port)+' -Pn -sT -sV -n --version-all'
                nm_scan.scan(ip, arguments=args)
                # self.logger.info(nm_scan.command_line())

                self.port_service_list[ip] = list()
                port_result = nm_scan[ip]['tcp']
                for port in port_result.keys():
                    state = port_result[port]['state']
                    name = port_result[port]['name']
                    product = port_result[port]['product']
                    version = port_result[port]['version']

                    result = "{:<17}{:<7}{:<10}{:<16}{:<32}{}".format(
                        ip, port, state, name, product, version)
                    # lock.acquire()
                    self.logger.info(result)
                    # lock.release()

                    service_result = dict()
                    service_result['port'] = port
                    service_result['state'] = state
                    service_result['name'] = name
                    service_result['product'] = product
                    service_result['version'] = version
                    self.port_service_list[ip].append(service_result)
            except Exception as e:
                self.logger.error(e)
                pass

    def run(self):
        self.logger.info("[*] Get the service of the port...")
        try:
            with ThreadPoolExecutor(max_workers=self.thread_num) as executor:
                for ip in self.ip_port_dict.keys():
                    ports = map(str, self.ip_port_dict[ip])
                    ports = ",".join(ports)
                    executor.submit(self.nmap_get_service, (ip, ports))
        except KeyboardInterrupt:
            self.logger.error("User aborted.")
            self.flag = False
            exit(0)

        return self.port_service_list
