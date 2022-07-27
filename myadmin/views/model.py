#View of Annotation Management
import os

from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.core.paginator import Paginator
from datetime import datetime, time
# Create your views here.
from myadmin.models import Category, Shop, DatasetDetail, Datasets, Annotation, Model, Download_history
from datetime import datetime
# Create your views here.
from myadmin.models import Category, Shop, DatasetDetail, Datasets
import time, os

def detail(request, pid=0):
    ''' 加载订单详情 '''
    #oid = request.GET.get("oid",0)
    #load the Datasets details
    ob = Model.objects.get(ID=pid)
    context = {'model': ob}
    #load archive files list
    '''alist = DatasetDetail.objects.values('ID', 'File_name').filter(Dataset_ID=pid)
    context["archivelist"] = alist
    print(context)
    #load annotation files list (normally only 1 file to 1 dataset)
    if Annotation.objects.filter(Dataset_ID=pid).exists():
        an = Annotation.objects.get(Dataset_ID=pid)
        context["annotation"] = an'''
    print(context)
    return render(request, "myadmin/model/detail.html", context)


def index(request, pIndex=1):

    '''Browse Info'''
    umod = Model.objects
    ulist = umod.filter()
#    ulist = umod.filter(status__lt=9)

    mywhere=[]
    #获取并判断搜索条件
    kw = request.GET.get("keyword", None)
    print("display keywrod value")
    print(kw)
    if kw:
        ulist = ulist.filter(model_name__contains=kw)
        mywhere.append('keyword='+kw)
     # 获取、判断并封装状态status搜索条件
    '''status = request.GET.get('status', '')
    if status != '':
        ulist = ulist.filter(status=status)
        mywhere.append("status="+status)
    '''
    #ulist = ulist.order_by("ID")#对id排序
    ulist = ulist.order_by("-Update_at")  # list the latest one
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
    context = {"modellist": list2, 'plist': plist, 'pIndex': pIndex, 'maxpages': maxpages, 'mywhere': mywhere}
    return render(request, "myadmin/model/index.html", context)

def loadModel(request,sid):
    clist = Annotation.objects.filter(status__lt=9, shop_id=sid).values("id", "name")
    #返回QuerySet对象，使用list强转成对应的菜品分类列表信息
    return JsonResponse({'data':list(clist)})

def add(request):
    '''加载信息添加表单'''
    #获取最近加的10个Datasets给DataManager编辑，如果加载所有Datasets列表很慢
    dlist = Datasets.objects.values('ID', 'Dataset_Name', 'update_at').order_by('-update_at')
    context = {"datasetlist": dlist}
    print(context)
    return render(request, "myadmin/model/add.html", context)

def insert(request):
    '''执行信息添加'''

    ''''Insert the new dataset into database'''
    # image files processing
    model_yaml_filename =''
    print(request.FILES.get("modelyamlinput", None))
    model_yaml_file = request.FILES.get("modelyamlinput", None)
    print(model_yaml_file)
    model_upload_file = request.FILES.get("modeluploadfile", None)
    print(model_upload_file)
    modelfile_onserver = request.POST['modelfileonserver']
    print(modelfile_onserver)

    if not model_upload_file and not modelfile_onserver:
        return HttpResponse("No ZIP uploaded or model package file does not exist on the server!")

    print(model_yaml_file)

    if model_yaml_file: #Write YAML file to the server
        model_yaml_filename = "y"+str(time.time())+"."+model_yaml_file.name.split('.').pop()
        destination = open("./static/uploads/model/"+model_yaml_filename, "wb+")
        # url will be http://localhost:8000/static/uploads/dataset/1648150968.7661688.png
        for chunk in model_yaml_file.chunks():      # 分块写入文件
            destination.write(chunk)
        destination.close()

    from pathlib import Path
    if modelfile_onserver:
        model_path = Path(modelfile_onserver)
        if model_path.is_file():  ##save sever file 2 as archive file 4
            model_upload_filename = os.path.basename(model_path)
    # get the path of the model on the host server


    if model_upload_file: #Write uploaded model file to the server if user upload a file
        model_upload_filename = "m"+str(time.time())+"."+model_upload_file.name.split('.').pop()
        destination = open("./static/uploads/model/"+model_upload_filename, "wb+")
        # url will be http://localhost:8000/static/uploads/dataset/1648150968.7661688.png
        for chunk in model_upload_file.chunks():      # 分块写入文件
            destination.write(chunk)
        destination.close()


    ob = Model()
    if model_yaml_file:
        print(model_yaml_filename)
        print("write model_yaml_filename!")
        ob.yaml_file = model_yaml_filename
    ob.model_name = request.POST['name']
    ob.machine_learning_method = request.POST['machine_learning_method']
    ob.classification_level = request.POST['classification_level']
    ob.classes = request.POST['classes']
    int_training_dataset_name = request.POST['int_train_dataset_id']
    ob.training_datasets = request.POST['training_datasets'] + ", " + int_training_dataset_name
    int_test_dataset_name = request.POST['int_test_dataset_id']
    ob.test_datasets = request.POST['test_datasets'] + ", " + int_test_dataset_name
    ob.create_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ob.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ob.model_package_file = model_upload_filename
    ob.yaml_content = request.POST['yaml_content']
    ob.save()
    context = {'info': "Add successfully！"}

    return render(request, "myadmin/info.html", context)

def delete(request,pid=0):
    '''执行信息删除'''
    '''执行信息删除'''
    try:
        ob = Model.objects.get(ID=pid)
        ob.delete()
        context = {'info': "Record deleted successfully!！"}
    except Exception as err:
        print(err)
        context = {'info': "Fail to delete！"}
    return render(request, "myadmin/info.html", context)

def edit(request, pid=0):
    ob = Model.objects.get(ID=pid)
    context = {'model': ob}
    return render(request, "myadmin/model/edit.html", context)

def update(request, pid):
    '''执行信息编辑'''
    ob = Model.objects.get(ID=pid)

    model_yaml_filename = ''
    print(request.FILES.get("modelyamlinput", None))
    model_yaml_file = request.FILES.get("modelyamlinput", None)
    print(model_yaml_file)
    model_upload_file = request.FILES.get("modeluploadfile", None)
    print(model_upload_file)
    modelfile_onserver = request.POST['modelfileonserver']
    print(modelfile_onserver)

    if not model_upload_file and not modelfile_onserver and not old_yaml_file:
        return HttpResponse("No ZIP uploaded or NO YAML or model package file on the server!")
    old_yaml_file = request.FILES.get("old_yaml_file", None)
    print(old_yaml_file) # previous defined YAML file
    print(model_yaml_file) # New uploaded YAML file

    if model_yaml_file:  # Write YAML file to the server
        model_yaml_filename = str(time.time()) + "." + model_yaml_file.name.split('.').pop()
        destination = open("./static/uploads/model/" + model_yaml_filename, "wb+")
        # url will be http://localhost:8000/static/uploads/dataset/1648150968.7661688.png
        for chunk in model_yaml_file.chunks():  # 分块写入文件
            destination.write(chunk)
        destination.close()

    from pathlib import Path
    if modelfile_onserver:
        model_path = Path(modelfile_onserver)
        if model_path.is_file():  ##save sever file 2 as archive file 4
            model_upload_filename = os.path.basename(model_path)
    # get the path of the model on the host server

    if model_upload_file:  # Write uploaded model file to the server if user upload a file
        model_upload_filename = str(time.time()) + "." + model_upload_file.name.split('.').pop()
        destination = open("./static/uploads/model/" + model_upload_filename, "wb+")
        # url will be http://localhost:8000/static/uploads/dataset/1648150968.7661688.png
        for chunk in model_upload_file.chunks():  # 分块写入文件
            destination.write(chunk)
        destination.close()

    if model_yaml_file:
        print(model_yaml_filename)
        print("write model_yaml_filename!")
        ob.yaml_file = model_yaml_filename # Newly uploaded YAML file
    else:
        ob.yaml_file = old_yaml_file # Existing YAML file
    ob.model_name = request.POST['name']
    ob.machine_learning_method = request.POST['machine_learning_method']
    ob.classification_level = request.POST['classification_level']
    ob.classes = request.POST['classes']
    ob.training_datasets = request.POST['training_datasets']
    ob.test_datasets = request.POST['test_datasets']
    ob.create_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ob.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ob.model_package_file = model_upload_filename
    ob.save()
    context = {'info': "Update successfully！"}
    return render(request, "myadmin/info.html", context)
