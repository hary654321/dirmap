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


def main():
    appDict = {
    'name': 'messenger',
    'playstore': True,
    'company': 'Facebook',
    'price': 100
    }
    app_json = json.dumps(appDict)
    print(app_json)


if __name__ == "__main__":
    main()
