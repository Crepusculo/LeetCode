# -*- coding: utf-8 -*-
import urllib
import urllib2
import time
import re

url = "http://10.3.8.211"
url_test = "http://www.baidu.com"
while True:

    flow3 = '.'
    try:
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        lines = response.readlines()
        for line in lines:
            result = re.findall('flow=\'(.*?) ', line)
            if result.__len__() > 0:
                flow = int(result[0])
                flow0 = flow % 1024
                flow1 = flow - flow0
                flow0 = flow0 * 1000
                flow0 = flow0 - flow0 % 1024
                if flow0 / 1024 < 10:
                    flow3 = '.00'
                elif flow0 / 1024 < 100:
                    flow3 = '.0'
                part = []
                part.append("Used internet traffic : ")
                part.append(flow1 / 1024)
                part.append(flow3)
                part.append(flow0 / 1024)
                part.append(" MByte")
                printout = ""
                for each in part:
                    printout += str(each)
                print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), printout

    except urllib2.URLError, e:
        if hasattr(e, "code"):
            print e.code
        if hasattr(e, "reason"):
            print e.reason
    time.sleep(5)
