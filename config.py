#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Author: reber
@Mail: reber0ask@qq.com
@Date: 2019-12-28 18:16:50
@LastEditTime : 2020-01-23 12:42:39
'''

import pathlib


root_abspath = pathlib.Path(__file__).parent.resolve()  #绝对路径
log_file_path = root_abspath.joinpath("log")
masscan_path = root_abspath.joinpath("masscan")

# log_level = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
log_level = "INFO"

nmap_min_hostgroup = 50
nmap_min_parallelism = 100

wooyun_top100_web_port = [8080,80,81,8081,7001,8000,8088,8888,9090,8090,88,8001,
    82,9080,8082,8089,9000,8443,9999,8002,89,8083,8200,8008,90,8086,801,8011,8085,
    9001,9200,8100,8012,85,8084,8070,7002,8091,8003,99,7777,8010,443,8028,8087,83,
    7003,10000,808,38888,8181,800,18080,8099,8899,86,8360,8300,8800,8180,3505,7000,
    9002,8053,1000,7080,8989,28017,9060,888,3000,8006,41516,880,8484,6677,8016,84,
    7200,9085,5555,8280,7005,1980,8161,9091,7890,8060,6080,8880,8020,7070,889,8881,
    9081,8009,7007,8004,38501,1010]
common_port = [21,22,23,25,53,69,80,81,82,83,84,85,86,87,88,89,110,111,135,139,143,
    161,389,443,445,465,513,873,993,995,1080,1099,1158,1433,1521,1533,1863,2049,2100,
    2181,3128,3306,3307,3308,3389,3690,5000,5432,5900,5985,5986,6379,7001,8000,8001,
    8002,8003,8004,8005,8006,8007,8008,8009,8010,8011,8012,8013,8014,8015,8016,8017,
    8018,8019,8020,8021,8022,8023,8024,8025,8026,8027,8028,8029,8030,8031,8032,8033,
    8034,8035,8036,8037,8038,8039,8040,8041,8042,8043,8044,8045,8046,8047,8048,8049,
    8050,8051,8052,8053,8054,8055,8056,8057,8058,8059,8060,8061,8062,8063,8064,8065,
    8066,8067,8068,8069,8070,8071,8072,8073,8074,8075,8076,8077,8078,8079,8080,8081,
    8082,8083,8084,8085,8086,8087,8088,8089,8090,8168,8888,9000,9080,9090,9200,9300,
    9418,11211,27017,27018,27019,50060]
