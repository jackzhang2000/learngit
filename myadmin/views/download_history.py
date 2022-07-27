#View of Annotation Management
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.core.paginator import Paginator
from datetime import datetime
# Create your views here.
from myadmin.models import Category, Shop, DatasetDetail, Datasets, Annotation, Model, Download_history

def index(request, pIndex=1):
    '''Browse Info'''
    umod = Download_history.objects
    ulist = umod.filter()
#    ulist = umod.filter(status__lt=9)

    mywhere=[]
    #获取并判断搜索条件
    kw = request.GET.get("keyword", None)
    if kw:
        ulist = ulist.filter(Model_Name__contains=kw)
        mywhere.append('keyword='+kw)
     # 获取、判断并封装状态status搜索条件
    '''status = request.GET.get('status', '')
    if status != '':
        ulist = ulist.filter(status=status)
        mywhere.append("status="+status)
    '''
    ulist = ulist.order_by("-download_time")#对download_time排序

    #执行分页处理
    pIndex = int(pIndex)
    page = Paginator(ulist,10) #以每页10条数据分页
    maxpages = page.num_pages #获取最大页数
    #判断当前页是否越界
    if pIndex > maxpages:
        pIndex = maxpages
    if pIndex < 1:
        pIndex = 1
    list2 = page.page(pIndex) #获取当前页数据
    plist = page.page_range #获取页码列表信息

    #遍历当前菜品分类信息并封装对应的店铺信息, 跨表查询Add info from Datasets table
    '''for vo in list2:
        sob = Datasets.objects.get(ID=vo.Dataset_ID)
        vo.Dataset_Name = sob.Dataset_Name
'''
    context = {"downloadhislist": list2, 'plist': plist, 'pIndex': pIndex, 'maxpages': maxpages, 'mywhere': mywhere}
    return render(request, "myadmin/downloadhis/index.html", context)

def delete(request,cid=0):
    '''执行信息删除'''
    try:
        ob = Category.objects.get(id=cid)
        ob.status = 9
        ob.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {'info':"删除成功！"}
    except Exception as err:
        print(err)
        context = {'info':"删除失败！"}
    return render(request,"myadmin/info.html",context)

from django.http import HttpResponse
import csv

def export_users_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="users.csv"'

    writer = csv.writer(response)
    writer.writerow(['user_id', 'username', 'email', 'filename', 'datasetdetail_ID', 'dataset_ID', 'dataset_name', 'download_time', 'model_ID', 'model_name'])

    users = Download_history.objects.all().values_list('user_id', 'username', 'email', 'filename', 'datasetdetail_ID', 'dataset_ID', 'dataset_name', 'download_time', 'model_ID', 'model_name')
    for user in users:
        writer.writerow(user)

    return response

#Help Page
def help(request):
    return render(request, 'myadmin/help/index.html')

