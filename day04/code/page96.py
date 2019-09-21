# coding=utf-8
import numpy as np

# 每次随机的结果都和第一次的结果相同
np.random.seed(10)
t = np.random.randint(0,20,(3,4))
print(t)