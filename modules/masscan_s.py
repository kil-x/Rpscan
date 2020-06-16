#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Author: reber
@Mail: reber0ask@qq.com
@Date: 2020-06-11 16:41:42
@LastEditTime : 2020-06-17 00:19:28
'''

import os
import demjson
import tempfile
from libs.data import config
from subprocess import Popen, STDOUT, PIPE


class MasscanScan(object):
    """端口扫描"""

    def __init__(self):
        super(MasscanScan, self).__init__()
        self.open_list = dict()
        self.logger = config.logger

    def masscan_scan(self):
        '''masscan 探测端口'''

        tmpfd1, target_file = tempfile.mkstemp(
            prefix='tmp_port_scan_target_', suffix='.txt', text=True)
        tmpfd2, result_file = tempfile.mkstemp(
            prefix='tmp_port_scan_result_', suffix='.txt', text=True)

        with open(target_file, "w") as f:
            f.write("\n".join(config.target_host))

        try:
            command = "{} -sS -v -Pn -n -p{} -iL {} -oJ {} --randomize-hosts --rate={}"
            command = command.format(config.masscan, config.ports, target_file, result_file, config.rate)
            self.logger.info(command)
            p = Popen(command, shell=True, stderr=STDOUT) # stdout=PIPE, 
            # print("状态：", p.poll())
            # print("开启进程的pid", p.pid)
            # print("所属进程组的pid", os.getpgid(p.pid))
            # time.sleep(90)
            masscan_output, masscan_err = p.communicate()
        except KeyboardInterrupt:
            os.remove(target_file)
            os.remove(result_file)
            time.sleep(11)
            os.remove("paused.conf")
            # os.killpg(os.getpgid(p.pid), 9)
            self.logger.error("User aborted.")
            exit(0)
        else:
            try:
                lines = list()
                with open(result_file, "r") as f_obj:
                    for line in f_obj.readlines():
                        lines.append(line.strip())

                for line in lines[1::2]:
                    result = demjson.decode(line)
                    ip = result.get("ip")
                    port = result.get("ports")[0].get("port")
                    status = result.get("ports")[0].get("status")
                    self.logger.info("{:<17}{:<7}{}".format(ip, port, status))

                    if ip in self.open_list:
                        self.open_list[ip].append(port)
                    else:
                        self.open_list[ip] = [port]
            except Exception as e:
                self.logger.error(e)
            finally:
                os.remove(target_file)
                os.remove(result_file)

    def run(self):
        self.logger.info("[*] Start masscan port scan...")
        self.masscan_scan()

        return self.open_list