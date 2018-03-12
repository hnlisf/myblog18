#!/home/blogenv/bin/python
# -*- coding:utf-8 -*-

import os
import multiprocessing

bind = ['0.0.0.0:9090']
workers = multiprocessing.cpu_count()*2
daemon = True

worker_class = 'gevent'
forward_allow_ips = '*'
keepalive = 6
timeout =65
graceful_timeout = 10
worker_connections = 65535
