# -*-coding:utf-8-*-
""" 
moke
"""
import unittest
from uiautomator import device as d


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)
        print("测试第一个")


    def test_somethin1(self):
        #self.assertEqual(True, True)
        d.screen.on()
        d(text=u"生活").click()
        print("测试生活")

        d.wait.idle(timeout=1000)
        d(text=u"教育").click()
        print("测试教育")
        d.wait.idle(timeout=1000)
        d(text=u"精选").click()
        print("测试精选")
        d.wait.idle(timeout=1000)


if __name__ == '__main__':
    unittest.main()
