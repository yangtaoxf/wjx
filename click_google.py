#coding:utf-8

from pymouse import PyMouse
import time

m = PyMouse()
time.sleep(10)
for i in range(1,1000000):
    m.click(615,690)
    time.sleep(2)