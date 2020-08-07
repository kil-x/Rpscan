#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Author: reber
@Mail: reber0ask@qq.com
@Date: 2019-09-19 09:52:13
@LastEditTime: 2019-12-13 10:38:28
'''

import re
import socket
from IPy import IP

class ParseTarget(object):
    """ParseTarget"""
    def __init__(self):
        super(ParseTarget, self).__init__()
        self.ip_list = list()

    def parse_target(self, targets):
        # ["10.17.1.1/24", "10.17.2.30-55", "10.111.22.12"]

        if isinstance(targets,list):
            for target in targets:
                ips = self.parse_ip(target)
                self.ip_list.extend(ips)
        elif isinstance(targets,str):
            ips = self.parse_ip(targets)
            self.ip_list.extend(ips)

        return self.ip_list

    def parse_ip(self, target):
        # 10.17.1.1/24 or 10.17.2.30-55 or 10.111.22.12

        ip_list = list()
        #校验target格式是否正确
        m1 = re.match(r'\d{1,3}(\.\d{1,3}){3}/(1[6789]|2[012346789]|30)$', target)
        m2 = re.match(r'\d{1,3}(\.\d{1,3}){3}-\d{1,3}$', target)
        m3 = re.match(r'\d{1,3}(\.\d{1,3}){3}$', target)
        if m1:
            tmp_ip_list = list()
            for x in IP(target,make_net=1):
                tmp_ip_list.append(str(x))
            ip_list = tmp_ip_list[1:-1]
        elif m2:
            prev = ".".join(target.split('.')[:3])
            st,sp = target.split('.')[-1].split('-')
            for x in range(int(st),int(sp)+1):
                ip_list.append(prev+"."+str(x))
        elif m3:
            ip_list.append(target)
        else:
            error_msg = "IP {} invalid format".format(target)
            raise Exception(error_msg)

        ips = [ip for ip in sorted(set(ip_list),key=socket.inet_aton)]
        return ips

if __name__ == '__main__':
    pt = ParseTarget()
    print(pt.parse_target("123.123.123.123/29"))
    # print(pt.parse_target(["123.123.123.123/30","1.1.1.1-4"]))