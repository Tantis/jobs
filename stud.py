#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Copyright (c) 2015 yu.liu <showmove@qq.com>
# All rights reserved

import requests
import json

if __name__ == "__main__":

    with open('access.log', 'r') as f:
        pline = f.readlines()
    url = "https://api.map.baidu.com/location/ip?ak=Ay7G6RvYQMQxBGujnpLdxb93&coor=bd09ll&ip={0}"
    pox = []
    for item in pline:
        #print(item.split('ip:')[1])
        r = requests.get(url.format(item.split('ip:')[1].strip()))
        pox.append({item.split('ip:')[1].strip(): r.json()})

    with open('addr.log', 'a') as f:
        f.write(json.dumps(pox))
