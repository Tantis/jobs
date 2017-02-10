#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Copyright (c) 2015 yu.liu <showmove@qq.com>
# All rights reserved

import requests
import json
import time
import os

SEEK = 0
if os.path.exists('file_status.pid'):
    with open('file_status.pid', 'r') as seek:
        SEEK = int(seek.read())

if __name__ == "__main__":

    while True:
        with open('access.log', 'r') as f:

            pline = f.readlines()

        seek = len(pline)

        print(seek, SEEK)
        if seek == SEEK:
            time.sleep(30)
            continue

        url = "https://api.map.baidu.com/location/ip?ak=Ay7G6RvYQMQxBGujnpLdxb93&coor=bd09ll&ip={0}"
        pox = []
        if os.path.exists('addr.log'):
            
            with open('addr.log', 'r') as f:
                try:
                    pox = json.load(f)
                except ValueError as err:
                    print(err)

                except Exception as err:
                    print(err)

        for item in pline[SEEK:]:
            # print(item.split('ip:')[1])
            r = requests.get(url.format(item.split('ip:')[1].strip()))
            pox.append({item.split('ip:')[1].strip(): r.json()})

        with open('addr.log', 'w') as f:
            f.write(json.dumps(pox))

        with open('file_status.pid', 'w') as sek:
            sek.write(str(seek))
        SEEK = seek
