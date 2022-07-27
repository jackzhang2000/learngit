from ruamel.yaml import YAML
#Dataset的视图文件
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from datetime import datetime
import time, os
# Create your views here.
from myadmin.models import Product, Category, Shop, Datasets, DatasetDetail, Annotation

umod = Datasets.objects
ulist = umod.filter()
mywhere = []
ulist = ulist.order_by("-update_at")

class Person(object):

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def hello(self):
        if self.sex == "girl":
            print(f'你好，我叫：{self.name}, 人家是个女孩子啦！')
        else:
            print(f'你好，我叫：{self.name}, 今年 {self.age} 岁')


# 实例化两个人
person_1 = Person('张三', 18, 'boy')
person_2 = Person('小红', 14, 'girl')

# 创建一个yaml对象
yaml = YAML()
# 注册这个 “Person” 类
yaml.register_class(Person)

# 将两个实例化后的对象保存到文件
yaml.dump([person_1, person_2], open('./person.yaml', 'w', encoding='utf-8'))