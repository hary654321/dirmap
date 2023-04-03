#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
@Author: xxlin
@LastEditors: xxlin
@Date: 2019-04-10 13:27:59
@LastEditTime: 2019-05-01 17:57:11
'''

import os
import sys
import json
import requests

def main():
    # Making a get request
    response = requests.get('https://api.github.com')
    
    # print response
    print(response)
    
    print(type(response))
    # print json content
    print(response.json())


if __name__ == "__main__":
    main()
