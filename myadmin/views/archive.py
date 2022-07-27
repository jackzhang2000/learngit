#菜品类别信息管理的视图文件
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.core.paginator import Paginator
from datetime import datetime
# Create your views here.
from myadmin.models import Category, Shop, DatasetDetail, Datasets
import time, os


#uploaded archive zip filenames will be stored into DatasetDetail objects based on
def index(request, pIndex=1):
    '''Browse Info'''
    umod = DatasetDetail.objects
    ulist = umod.filter()
#    ulist = umod.filter(status__lt=9)

    mywhere=[]
    #获取并判断搜索条件
    kw = request.GET.get("keyword", None)
    if kw:
        ulist = ulist.filter(Dataset_Name__contains=kw)
        mywhere.append('keyword='+kw)
     # 获取、判断并封装状态status搜索条件
    '''status = request.GET.get('status','')
    if status != '':
        ulist = ulist.filter(status=status)
        mywhere.append("status="+status)
    '''
    ulist = ulist.order_by("-update_at")#对id排序
    #执行分页处理
    pIndex = int(pIndex)
    page = Paginator(ulist, 10) #以每页10条数据分页
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
    context = {"categorylist": list2, 'plist': plist, 'pIndex': pIndex, 'maxpages': maxpages, 'mywhere': mywhere}
    return render(request, "myadmin/archive/index.html", context)

def loadCategory(request,sid):
    clist = Category.objects.filter(status__lt=9, shop_id=sid).values("id", "name")
    #返回QuerySet对象，使用list强转成对应的菜品分类列表信息
    return JsonResponse({'data':list(clist)})

def add(request, did=0): #did is dataset id
    '''加载信息添加表单'''
    if did == 0:
        # 获取最近加的10个Datasets给DataManager编辑，如果加载所有Datasets列表很慢
        dlist = Datasets.objects.values('ID', 'Dataset_Name', 'update_at').order_by('-update_at')[:10]
        context = {"datasetlist": dlist}
        print(context)
        return render(request, "myadmin/archive/add.html", context)
    else: #If specify a dataset, then add archives for this dataset
        ob = Datasets.objects.get(ID=did)
        context = {'archive': ob}
        print(context)
        return render(request, "myadmin/archive/addid.html", context)

def insert(request):
    '''执行信息添加'''
    try:
        # Process only first file

        myfile1 = request.FILES.get("fileUpload1", None)
        myfile2 = request.FILES.get("fileUpload2", None)
        fileonserver1 = request.POST['fileonserver1']
        fileonserver2 = request.POST['fileonserver2']
        from pathlib import Path
        path1 = Path(fileonserver1) #get the path of the fileonserver1 on the host server
        path2 = Path(fileonserver2)  # get the path of the fileonserver1 on the host server
        archive_zip1 = ''
        archive_zip2 = ''
        archive_zip3 = ''
        archive_zip4 = ''

        if not myfile1 and not path1.is_file() and not myfile2 and not path2:
            return HttpResponse("No ZIP uploaded or file does not exist on the server!")

        if myfile1: ##save sever file 1 as archive file 2
            archive_zip1 = str(time.time()) + "." + myfile1.name.split('.').pop()
            destination1 = open("./static/uploads/archive/" + archive_zip1, "wb+")
            for chunk in myfile1.chunks():  # Write to the file from uploaded file
                destination1.write(chunk)
            destination1.close()

        if path1.is_file(): #if file exists on the server then just retrieve the filename
            archive_zip2 = os.path.basename(path1)

        if myfile2: #save uploaded file 2 as archive file 3
            archive_zip3 = str(time.time()) + "." + myfile2.name.split('.').pop()
            destination3 = open("./static/uploads/archive/" + archive_zip3, "wb+")
            for chunk in myfile2.chunks():  # Write to the file from uploaded file
                destination3.write(chunk)
            destination3.close()

        if path2.is_file(): ##save sever file 2 as archive file 4
            archive_zip4 = os.path.basename(path2)

        if archive_zip1:
            ar = DatasetDetail()
            ar.Dataset_ID = request.POST['dataset_id']
            ar.Dataset_Name = request.POST['dataset_name']
            #txt.split(", ")
            # an.Annotation_type = request.POST['detail']
            #ar.Annotation_type = request.GET.get("anno_type", 1)  # annotation_type:1 Detailed default/2 Coarse
            print(archive_zip1)
            ar.File_name = archive_zip1  # csv filename
            ar.File_type = 'ZIP'
            ar.Dataset_Name = request.POST['dataset_name']
            ar.create_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ar.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ar.save()
            context = {'info': "Add archive successfully！"}

        if archive_zip2:
            ar2 = DatasetDetail()
            ar2.Dataset_ID = request.POST['dataset_id']
            ar2.Dataset_Name = request.POST['dataset_name']
            print(archive_zip2)
            ar2.File_name = archive_zip2  # csv filename
            ar2.File_type = 'ZIP'
            ar2.create_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ar2.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ar2.save()
            context = {'info': "Add archive successfully！"}

        if archive_zip3:
            ar3 = DatasetDetail()
            ar3.Dataset_ID = request.POST['dataset_id']
            ar3.Dataset_Name = request.POST['dataset_name']
            print(archive_zip3)
            ar3.File_name = archive_zip3  # csv filename
            ar3.File_type = 'ZIP'
            ar3.create_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ar3.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ar3.save()
            context = {'info': "Add archive successfully！"}

        if archive_zip4:
            ar4 = DatasetDetail()
            ar4.Dataset_ID = request.POST['dataset_id']
            ar4.Dataset_Name = request.POST['dataset_name']
            print(archive_zip4)
            ar4.File_name = archive_zip4  # csv filename
            ar4.File_type = 'ZIP'
            ar4.create_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ar4.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ar4.save()
            context = {'info': "Add archive successfully！"}

    except Exception as err:
        print(err)
        context = {'info': "Add archive failed！"}
    return render(request, "myadmin/info.html", context)


def delete(request, did=0):
    '''执行信息删除'''
    try:
        ob = DatasetDetail.objects.get(ID=did)
        ob.delete()
        context = {'info': "Record deleted successfully!！"}
    except Exception as err:
        print(err)
        context = {'info': "Record deleted failed!！"}
    return render(request, "myadmin/info.html", context)

def edit(request, did=0):
    '''加载信息编辑表单'''
    try:
        ob = DatasetDetail.objects.get(ID=did)
        context = {'archive': ob}
        #slist = Shop.objects.values("id", 'name')
        #context["shoplist"] = slist
        return render(request, "myadmin/archive/edit.html", context)
    except Exception as err:
        print(err)
        context = {'info':"没有找到要修改的信息！"}
        return render(request,"myadmin/info.html", context)

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