#菜品类别信息管理的视图文件
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.core.paginator import Paginator
from datetime import datetime
# Create your views here.
from myadmin.models import Category, Shop, DatasetDetail, Datasets


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
    context = {"categorylist": list2, 'plist': plist, 'pIndex': pIndex, 'maxpages': maxpages, 'mywhere': mywhere}
    return render(request, "myadmin/category/index.html", context)

def loadCategory(request,sid):
    clist = Category.objects.filter(status__lt=9, shop_id=sid).values("id", "name")
    #返回QuerySet对象，使用list强转成对应的菜品分类列表信息
    return JsonResponse({'data':list(clist)})

def add(request):
    '''加载信息添加表单'''
    #获取当前所有店铺 获取最近加的20个Datasets给DataManager编辑，如果加载所有Datasets列表很慢
    slist = Shop.objects.filter(pub_date__year=2006).values("id",'name')
    context = {"shoplist": slist}
    return render(request, "myadmin/category/add.html", context)

def insert(request):
    '''执行信息添加'''
    try:
        ob = Category()
        ob.shop_id = request.POST['shop_id']
        ob.name = request.POST['name']
        ob.status = 1
        ob.create_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {'info':"添加成功！"}
    except Exception as err:
        print(err)
        context = {'info':"添加失败！"}
    return render(request,"myadmin/info.html",context)

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

def edit(request,cid=0):
    '''加载信息编辑表单'''
    try:
        ob = Category.objects.get(id=cid)
        context = {'category':ob}
        slist = Shop.objects.values("id",'name')
        context["shoplist"] = slist
        return render(request,"myadmin/category/edit.html",context)
    except Exception as err:
        print(err)
        context = {'info':"没有找到要修改的信息！"}
        return render(request,"myadmin/info.html",context)

def update(request,cid):
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