#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
本类用于对比图片相似度
'''

class imgCompare(object):
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

    def get_phone(self):
        return self.phone

    def update_phone(self, newphone):
        self.phone = newphone
        print "手机号更改已更改"

    def get_email(self):
        return self.email


class AddrBook(object):
    '''docstring for AddBook'''
    def __init__(self, name, phone, email, qq):
        self.name = name
        self.info = Info(phone, email, qq)


if __name__ == "__main__":
    Detian = AddrBook('handetian', '18210413001', 'detian@xkops.com', '123456')
    print Detian.info.get_phone()
    Detian.info.update_phone(18210413002)
    print Detian.info.get_phone()
    print Detian.info.get_email()