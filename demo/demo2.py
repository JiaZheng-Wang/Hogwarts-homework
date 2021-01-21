# @Time    : 2020/11/26 11:36
# @Author  : Sylar
# @Explain : 
# @Software: PyCharm
import chevron
from pathlib2 import Path

step = {"musketeers":
            [{"name": '123', "age": 12},
             {"name": '234', "age": 12},
             ],
        }

with open('file.mustache', 'r') as mustache:
    intersface = chevron.render(mustache, step)
print(intersface)
