#Dataset的视图文件
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from datetime import datetime
import time, os
# Create your views here.
from myadmin.models import Product, Category, Shop, Datasets, DatasetDetail, Annotation
from ruamel.yaml import YAML

def detail(request, pid=0):
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
    return render(request, "myadmin/dataset/detail.html", context)

def index(request, pIndex=1):
    '''Browse all datasets'''
    umod = Datasets.objects
    ulist = umod.filter()
    mywhere=[]

    #Filtered by dataset name
    kw = request.GET.get("keyword", None)
    if kw:
        ulist = ulist.filter(Dataset_Name__contains=kw)
        mywhere.append('keyword='+kw)
    #获取并判断搜索菜品类别条件
    cid = request.GET.get("category_id", None)
    if cid:
        ulist = ulist.filter(category_id=cid)
        mywhere.append('category_id='+cid)
     # 获取、判断并封装状态status搜索条件
    status = request.GET.get('status', '')
    if status != '':
        ulist = ulist.filter(status=status)
        mywhere.append("status="+status)
    ulist = ulist.order_by("-update_at")# list the latest one
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

    context = {"datasetlist":list2, 'plist':plist, 'pIndex':pIndex, 'maxpages':maxpages, 'mywhere':mywhere}
    return render(request, "myadmin/dataset/index.html", context)

def add(request):
    '''加载信息添加表单'''
    #获取当前所有店铺
    slist = Shop.objects.values("id", 'name')
    context = {"shoplist":slist}
    return render(request,"myadmin/dataset/add.html", context)

def insert(request):
    ''''Insert the new dataset into database'''
    #image files processing
    summary_by_species_pic = request.FILES.get("Summary_by_Species", None)
    print(summary_by_species_pic)
    summary_by_ecotypes_pic = request.FILES.get("Summary_by_Ecotypes", None)
    print(summary_by_ecotypes_pic)
    summary_by_pods_pic = request.FILES.get("Summary_by_Pods", None)
    print(summary_by_pods_pic)
    summary_by_calltype_pic = request.FILES.get("Summary_by_CallType", None)
    print(summary_by_calltype_pic)
    #if not summary_by_species_pic and not summary_by_ecotypes_pic and not summary_by_pods_pic and not summary_by_calltype_pic:
    #    return HttpResponse("No upload images!")

    if summary_by_species_pic:
        summary_by_species = str(time.time())+"."+summary_by_species_pic.name.split('.').pop()
        destination = open("./static/uploads/dataset/"+summary_by_species, "wb+")
        # url will be http://localhost:8000/static/uploads/dataset/1648150968.7661688.png
        for chunk in summary_by_species_pic.chunks():      # 分块写入文件
            destination.write(chunk)
        destination.close()

    if summary_by_ecotypes_pic:
        summary_by_ecotypes = str(time.time())+"."+summary_by_ecotypes_pic.name.split('.').pop()
        destination = open("./static/uploads/dataset/"+summary_by_ecotypes, "wb+")
        # url will be http://localhost:8000/static/uploads/dataset/1648150968.7661688.png
        for chunk in summary_by_ecotypes_pic.chunks():      # 分块写入文件
            destination.write(chunk)
        destination.close()

    if summary_by_pods_pic:
        summary_by_pods = str(time.time())+"."+summary_by_pods_pic.name.split('.').pop()
        destination = open("./static/uploads/dataset/"+summary_by_pods, "wb+")
        # url will be http://localhost:8000/static/uploads/dataset/1648150968.7661688.png
        for chunk in summary_by_pods_pic.chunks():      # 分块写入文件
            destination.write(chunk)
        destination.close()

    if summary_by_calltype_pic:
        summary_by_calltype = str(time.time())+"."+summary_by_calltype_pic.name.split('.').pop()
        destination = open("./static/uploads/dataset/"+summary_by_calltype, "wb+")
        # url will be http://localhost:8000/static/uploads/dataset/1648150968.7661688.png
        for chunk in summary_by_calltype_pic.chunks():      # 分块写入文件
            destination.write(chunk)
        destination.close()

    ob = Datasets()
    ob.Dataset_Name = request.POST['datasetname']
    ob.Num_Of_Files = request.POST['numoffiles']
    ob.Num_Of_Annotated_Events = request.POST['numofannoevent']
    ob.Species_identified = request.POST['speciesidf']
    ob.Sampling_rate = request.POST['samplerate']
    ob.Total_Duration = request.POST['fileduration']
    ob.Total_Size = request.POST['totalsize']
    ob.File_Size = request.POST['filesize']
    ob.Number_of_Subsets = request.POST['noofsubsets']
    ob.Location = request.POST['location']
    ob.Latitude = request.POST['latitude']
    ob.Longitude = request.POST['longitude']
    ob.Depth = request.POST['depth']
    ob.Ecotype = request.POST['ecotype']
    ob.Pods = request.POST['pods']
    ob.Calltype = request.POST['calltype']
    ob.Depth = request.POST['depth']
    ob.record_start = request.POST['Datetimelocalfrom']
    ob.record_end = request.POST['Datetimelocalto']
    #ob.YAML_Filename = request.POST['YAML_Filename']
    if summary_by_species_pic:
        ob.Summary_by_Species = summary_by_species
    if summary_by_ecotypes_pic:
        ob.Summary_by_Ecotypes = summary_by_ecotypes
    if summary_by_pods_pic:
        ob.Summary_by_Pods = summary_by_pods
    if summary_by_calltype_pic:
        ob.Summary_by_CallType = summary_by_calltype
    ob.create_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ob.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ob.save()

    # 创建一个yaml对象
    #yaml = YAML()
    # 注册这个 “Datasets” 类
    #yaml.register_class(Datasets)

    # 将1个实例化后的对象保存到文件
    #yaml.dump([ob], open('./static/uploads/dataset/dataset.yaml', 'w', encoding='utf-8'))

    #yaml.dump([person_1, person_2], open('./person.yaml', 'w', encoding='utf-8')) 存2个对象
    context = {'info': "Add Dataset successfully！"}
    return render(request, "myadmin/info.html", context)

def delete(request, pid=0):
    '''执行信息删除'''
    try:
        ob = Datasets.objects.get(ID=pid)
        ob.delete()
        context = {'info': "Record deleted successfully!！"}
    except Exception as err:
        print(err)
        context = {'info': "Fail to delete！"}
    return render(request, "myadmin/info.html", context)

def edit(request, pid=0):
    '''加载信息编辑表单'''
    try:
        ob = Datasets.objects.get(ID=pid)
        context = {'dataset': ob}
        return render(request, "myadmin/dataset/edit.html", context)
    except Exception as err:
        print(err)
        context = {'info': "No record to be edit！"}
        return render(request,"myadmin/info.html", context)

def update(request, pid):
    '''执行信息编辑'''
    try:
        #获取原图片
        old_sum_species_pic = request.POST['old_sum_species_pic']
        old_sum_ecotypes_pic = request.POST['old_sum_ecotypes_pic']
        old_sum_pods_pic = request.POST['old_sum_pods_pic']
        old_sum_calltype_pic = request.POST['old_sum_calltype_pic']
        #图片的上传处理
        new_sum_species_pic = request.FILES.get("new_sum_species_pic", None)
        new_sum_ecotypes_pic = request.FILES.get("new_sum_ecotypes_pic", None)
        new_sum_pods_pic = request.FILES.get("new_sum_pods_pic", None)
        new_sum_calltype_pic = request.FILES.get("new_sum_calltype_pic", None)

        if not new_sum_species_pic:
            summary_by_species = old_sum_species_pic  # If new_sum_species_pic is null, use old picture
        else:  # If cover_pic1 is not null, update with the new picture
            summary_by_species = str(time.time())+"."+new_sum_species_pic.name.split('.').pop()
            destination = open("./static/uploads/dataset/"+summary_by_species, "wb+")
            for chunk in new_sum_species_pic.chunks():      # 分块写入文件
                destination.write(chunk)  
            destination.close()

        if not new_sum_ecotypes_pic:
            summary_by_ecotypes = old_sum_ecotypes_pic  # If new_sum_species_pic is null, use old picture
        else:  # If cover_pic1 is not null, update with the new picture
            summary_by_ecotypes = str(time.time())+"."+new_sum_ecotypes_pic.name.split('.').pop()
            destination = open("./static/uploads/dataset/"+summary_by_ecotypes, "wb+")
            for chunk in new_sum_ecotypes_pic.chunks():      # 分块写入文件
                destination.write(chunk)
            destination.close()

        if not new_sum_pods_pic:
            summary_by_pods = old_sum_pods_pic  # If new_sum_species_pic is null, use old picture
        else:  # If cover_pic1 is not null, update with the new picture
            summary_by_pods = str(time.time())+"."+new_sum_pods_pic.name.split('.').pop()
            destination = open("./static/uploads/dataset/"+summary_by_pods, "wb+")
            for chunk in new_sum_pods_pic.chunks():      # 分块写入文件
                destination.write(chunk)
            destination.close()

        if not new_sum_calltype_pic:
            summary_by_calltype = old_sum_calltype_pic  # If new_sum_species_pic is null, use old picture
        else:  # If cover_pic1 is not null, update with the new picture
            summary_by_calltype = str(time.time())+"."+new_sum_calltype_pic.name.split('.').pop()
            destination = open("./static/uploads/dataset/"+summary_by_calltype, "wb+")
            print('准备写入new_sum_calltype_pic')
            for chunk in new_sum_calltype_pic.chunks():      # 分块写入文件
                destination.write(chunk)
            destination.close()
            print('写入new_sum_calltype_pic成功！')

        ob = Datasets.objects.get(ID=pid)
        ob.Dataset_Name = request.POST['datasetname']
        ob.Num_Of_Files = request.POST['numoffiles']
        ob.Species_identified = request.POST['speciesidf']
        ob.Location = request.POST['location']
        ob.Latitude = request.POST['latitude']
        ob.Longitude = request.POST['longitude']
        ob.Depth = request.POST['depth']
        ob.Summary_by_Species = summary_by_species
        ob.Summary_by_Ecotypes = summary_by_ecotypes
        ob.Summary_by_Pods = summary_by_pods
        ob.Summary_by_CallType = summary_by_calltype
        ob.Num_Of_Annotated_Events = request.POST['numofannoevent']
        ob.Number_of_Subsets = request.POST['noofsubsets']
        ob.Sampling_rate = request.POST['samplerate']
        ob.Total_Duration = request.POST['fileduration']
        ob.File_Size = request.POST['filesize']
        ob.Total_Size = request.POST['totalsize']
        ob.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {'info': "Update successfully！"}
        #判断并删除老图片
        if new_sum_species_pic and old_sum_species_pic:
            print('delete old_sum_species_pic')
            os.remove("./static/uploads/dataset/"+old_sum_species_pic)
        if new_sum_ecotypes_pic and old_sum_ecotypes_pic:
            print('delete old_sum_ecotypes_pic')
            os.remove("./static/uploads/dataset/"+old_sum_ecotypes_pic)
        if new_sum_pods_pic and old_sum_pods_pic:
            print('delete old_sum_pods_pic')
            os.remove("./static/uploads/dataset/"+old_sum_pods_pic)
        if new_sum_calltype_pic and old_sum_calltype_pic:
            print('delete old_sum_calltype_pic')
            os.remove("./static/uploads/dataset/"+old_sum_calltype_pic)
        print("Success!")
    except Exception as err:
        print(err)
        context = {'info': "Fail to update！"}
        print("Failed")
         #判断并删除新图片
        if new_sum_species_pic:
            os.remove("./static/uploads/dataset/" + summary_by_species)
        if new_sum_ecotypes_pic:
            os.remove("./static/uploads/dataset/" + summary_by_ecotypes)
        if new_sum_pods_pic:
            os.remove("./static/uploads/dataset/" + summary_by_pods)
        if new_sum_calltype_pic:
            print(new_sum_calltype_pic)
            os.remove("./static/uploads/dataset/" + summary_by_calltype)

    return render(request, "myadmin/info.html", context)