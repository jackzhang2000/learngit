#Dataset Query View
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.shortcuts import redirect
from django.urls import reverse
from datetime import datetime

from myadmin.models import User, Orders, OrderDetail, Payment, Model, Datasets, DatasetDetail, Annotation

'''
def index(request, pIndex=1):
    message = None
    all_message = Datasets.objects.filter(Dataset_Name='Jasco_Roberts_Bank')
    if all_message:
        message = all_message[0]

    return render(request, 'web/message_form.html', {
        'my_message': message
    })

# Create your views here.
'''

user_list = []
def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
    return render(request, 'index.html')


def dataset_detail(request, pid=0):
    ''' 加载订单详情 '''
    #oid = request.GET.get("oid",0)
    #load the Datasets details
    ob = Datasets.objects.get(ID=pid)
    context = {'dataset': ob}
    print(context)
    #load archive files list
    alist = DatasetDetail.objects.values('ID', 'File_name').filter(Dataset_ID=pid)
    context["archivelist"] = alist
    print(context)
    #load annotation files list (normally only 1 file to 1 dataset)
    if Annotation.objects.filter(Dataset_ID=pid).exists():
        an = Annotation.objects.get(Dataset_ID=pid)
        context["annotation"] = an
    print(context)
    return render(request, "web/detail20220706.html", context)

