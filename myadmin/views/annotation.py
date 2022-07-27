#View of Annotation Management
import logging

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.core.paginator import Paginator
from datetime import datetime
import time, os
# Create your views here.
from myadmin.models import Category, Shop, DatasetDetail, Datasets, Annotation


def index(request, pIndex=1):
    '''Browse Info'''
    umod = Annotation.objects
    ulist = umod.filter()
#    ulist = umod.filter(status__lt=9)

    mywhere=[]
    #获取并判断搜索条件
    kw = request.GET.get("keyword", None)
    if kw:
        ulist = ulist.filter(Dataset_name__contains=kw)
        mywhere.append('keyword='+kw)
     # 获取、判断并封装状态status搜索条件
    '''status = request.GET.get('status', '')
    if status != '':
        ulist = ulist.filter(status=status)
        mywhere.append("status="+status)
    '''
    ulist = ulist.order_by("ID")#对id排序
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
    context = {"annotationlist": list2, 'plist': plist, 'pIndex': pIndex, 'maxpages': maxpages, 'mywhere': mywhere}
    return render(request, "myadmin/annotation/index.html", context)

def query(request, cid=0):
    '''Browse Info'''
    umod = Annotation.objects.get(id=cid)
    ulist = umod.filter()
#    ulist = umod.filter(status__lt=9)

    mywhere=[]
    #获取并判断搜索条件
    kw = request.GET.get("keyword", None)
    if kw:
        ulist = ulist.filter(Dataset_Name__contains=kw)
        mywhere.append('keyword='+kw)
     # 获取、判断并封装状态status搜索条件
    '''status = request.GET.get('status', '')
    if status != '':
        ulist = ulist.filter(status=status)
        mywhere.append("status="+status)
    '''
    ulist = ulist.order_by("ID")#对id排序
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
    context = {"annotationlist": list2, 'plist': plist, 'pIndex': pIndex, 'maxpages': maxpages, 'mywhere': mywhere}
    return render(request, "myadmin/annotation/index.html", context)

def loadAnnotation(request,sid):
    clist = Annotation.objects.filter(status__lt=9, shop_id=sid).values("id", "name")
    #返回QuerySet对象，使用list强转成对应的菜品分类列表信息
    return JsonResponse({'data':list(clist)})

def add(request, did=0): #did is dataset id
    '''加载信息添加表单'''
    if did == 0:
        # 获取最近加的20个Datasets给DataManager编辑，如果加载所有Datasets列表很慢
        dlist = Datasets.objects.values('ID', 'Dataset_Name', 'update_at').order_by('-update_at')[:10]
        context = {"datasetlist": dlist}
        print(context)
        return render(request, "myadmin/annotation/add.html", context)
    else: #If specify a dataset, then add archives for this dataset
        ob = Datasets.objects.get(ID=did)
        context = {'archive': ob}
        print(context)
        return render(request, "myadmin/annotation/addid.html", context)

def insert(request):
    '''执行信息添加'''
    try:
        # 图片的上传处理
        myfile = request.FILES.get("fileUpload", None)
        if not myfile:
            return HttpResponse("No CSV filename!")
        anno_csv = str(time.time()) + "." + myfile.name.split('.').pop()
        destination = open("./static/uploads/annotation/" + anno_csv, "wb+")
        for chunk in myfile.chunks():  # 分块写入文件
            destination.write(chunk)
        destination.close()

        an = Annotation()

        did = request.POST['dataset_id']
        an.Dataset_ID = did
        #an.Annotation_type = request.POST['detail']
        anno_type = request.POST["anno_type"]
        an.Annotation_type = anno_type  # annotation_type:1 Detailed default/2 Coarse
        an.File_name = anno_csv # csv filename
        an.Dataset_name = request.POST['dataset_name']
        an.create_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        an.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        an.save()
        #Update the annotation type linked dataset in dataset table
        ob = Datasets.objects.get(ID=did)
        ob.Annotation_type = anno_type
        ob.save()
        context = {'info': "Add annotation successfully！"}
    except Exception as err:
        print(err)
        context = {'info': "Add annotation failed！"}
    return render(request, "myadmin/info.html", context)

def delete(request, pid=0):
    '''执行信息删除'''
    try:
        ob = Annotation.objects.get(ID=pid)
        ob.delete()
        context = {'info': "Record deleted successfully!！"}
    except Exception as err:
        print(err)
        context = {'info':"Fail to delete!"}
    return render(request, "myadmin/info.html", context)

def edit(request,pid=0):
    '''加载信息编辑表单'''
    try:
        ob = Annotation.objects.get(ID=pid)
        context = {'anno': ob}
        print(context)
        # slist = Shop.objects.values("id", 'name')
        # context["shoplist"] = slist
        return render(request, "myadmin/annotation/edit.html", context)
    except Exception as err:
        print(err)
        context = {'info':"Records not found！"}
        return render(request,"myadmin/info.html",context)

def update(request, cid):
    '''执行信息编辑'''
    try:
        ob = Category.objects.get(id=cid)
        ob.shop_id = request.POST['shop_id']
        ob.name = request.POST['name']
        ob.status = request.POST['status']
        ob.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {'info':"修改成功！"}
    except Exception as err:
        print(err)
        context = {'info':"修改失败！"}
    return render(request,"myadmin/info.html",context)


def upload_csv(request):
    data = {}
    if "GET" == request.method:
        return render(request, "myadmin/upload_csv.html", data)
    # if not GET, then proceed
    csv_file = request.FILES["csv_file"]
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'File is not CSV type')
        return HttpResponseRedirect(reverse("myapp:upload_csv"))
    # if file is too large, return
    if csv_file.multiple_chunks():
        messages.error(request, "Uploaded file is too big (%.2f MB)." % (csv_file.size / (1000 * 1000),))
        return HttpResponseRedirect(reverse("myapp:upload_csv"))

    file_data = csv_file.read().decode("utf-8")

    lines = file_data.split("\n")
    # loop over the lines and save them in db. If error , store as string and then display
    for line in lines:
        fields = line.split(",")
        data_dict = {}
        data_dict["filename"] = fields[0]
        data_dict["start"] = fields[1]
        data_dict["end"] = fields[2]
        data_dict["freq_min"] = fields[3]
        try:
            form = EventsForm(data_dict)
            if form.is_valid():
                form.save()
            else:
                logging.getLogger("error_logger").error(form.errors.as_json())
        except Exception as e:
            logging.getLogger("error_logger").error(repr(e))
            pass
    return HttpResponseRedirect(reverse("myapp:upload_csv"))