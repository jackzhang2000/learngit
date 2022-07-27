from itertools import chain

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
# Create your views here.
from myadmin.models import User,Shop,Category,Product, Datasets, Model
from django.core.paginator import Paginator
from datetime import datetime, date
import time, os
# Create your views here.
from myadmin.models import Product, Category, Shop, Datasets, DatasetDetail, Annotation, Download_history
from datetime import datetime

def signup(request):
    ''' 项目前台大堂点餐首页 '''
    return render(request, "web/Signup.html")

def about(request):
    ''' 项目前台大堂点餐首页 '''
    return render(request, "web/about.html")

def help(request):
    ''' 项目前台大堂点餐首页 '''
    return render(request, "web/help.html")

def index(request):
    ''' 项目前台大堂点餐首页 '''
    return redirect(reverse("web_index"))

def webindex(request, pIndex=1):
    '''Browse all datasets'''
    umod = Datasets.objects

    '''Generate the distinct species list'''
    species_list = Datasets.objects.values_list('Species_identified', flat=True).distinct()
    species_list_dup = []
    for idx, word in enumerate([i for i in species_list if i]):
        species_list_dup.append(word.split(':'))
    species_list_dedup = list(dict.fromkeys(list(chain.from_iterable(species_list_dup))))
    species_idx = []
    for idx in range(len(species_list_dedup)):
        species_idx.append('species'+str(idx))
    species_dict = list(zip(species_idx, species_list_dedup))

    '''Generate the distinct Ecotype list'''
    ecotype_list = Datasets.objects.values_list('Ecotype', flat=True).distinct()
    ecotype_list_dup = []
    for idx, word in enumerate([i for i in ecotype_list if i]): #remove None and loop the list to retrieve index and value
        ecotype_list_dup.append(word.split(':')) #split 'SRKW:KW' to 'SRKW' and 'KW'
    ecotype_list_dedup = list(dict.fromkeys(list(chain.from_iterable(ecotype_list_dup))))
    ecotype_idx = []
    for idx in range(len(ecotype_list_dedup)):
        ecotype_idx.append('ecotype'+str(idx))
    ecotype_dict = list(zip(ecotype_idx, ecotype_list_dedup))

    '''Generate the distinct Pods list'''
    pods_list = Datasets.objects.values_list('Pods', flat=True).distinct()
    pods_list_dup = []
    for idx, word in enumerate([i for i in pods_list if i]):  # remove None and loop the list to retrieve index and value
        pods_list_dup.append(word.split(':'))  # split 'SRKW:KW' to 'SRKW' and 'KW'
    pods_list_dedup = list(dict.fromkeys(list(chain.from_iterable(pods_list_dup))))
    pods_idx = []
    for idx in range(len(pods_list_dedup)):
        pods_idx.append('pods' + str(idx))
    pods_dict = list(zip(pods_idx, pods_list_dedup))

    '''Generate the distinct Calltype list'''
    calltype_list = Datasets.objects.values_list('Calltype', flat=True).distinct()
    calltype_list_dup = []
    for idx, word in enumerate([i for i in calltype_list if i]):  # remove None and loop the list to retrieve index and value
        calltype_list_dup.append(word.split(':'))  # split 'SRKW:KW' to 'SRKW' and 'KW'
    calltype_list_dedup = list(dict.fromkeys(list(chain.from_iterable(calltype_list_dup))))
    calltype_idx = []
    for idx in range(len(calltype_list_dedup)):
        calltype_idx.append('calltype' + str(idx))
    calltype_dict = list(zip(calltype_idx, calltype_list_dedup))


    #print(Datasets.objects.values_list('Calltype', flat=True).distinct())
    print("-----------------------------------------------------------")
    ulist = umod.filter()

    ulist = ulist.order_by("-update_at")  # list the latest one


    mywhere=[]

    #Filtered by dataset name
    kw = request.GET.get("keyword", None)
    if kw:
        #date__range=[startdate, enddate]  & update_at=[startdate, enddate]
        ulist = ulist.filter(Dataset_Name__contains=kw)

    species1 = request.GET.get("species1", None)
    if species1:
        print(species1)
        # date__range=[startdate, enddate]  & update_at=[startdate, enddate]
        ulist = ulist.filter(Species_identified__contains=species1)
        mywhere.append('Species_identified=' + species1)

    species2 = request.GET.get("species2", None)
    if species2:
        print(species2)
        # date__range=[startdate, enddate]  & update_at=[startdate, enddate]
        ulist = ulist.filter(Species_identified__contains=species2)
        mywhere.append('Species_identified=' + species2)

    species3 = request.GET.get("species3", None)
    if species3:
        print(species3)
        # date__range=[startdate, enddate]  & update_at=[startdate, enddate]
        ulist = ulist.filter(Species_identified__contains=species3)
        mywhere.append('Species_identified=' + species3)

    eco1 = request.GET.get("eco1", None)
    if eco1:
        print(eco1)
        #date__range=[startdate, enddate]  & update_at=[startdate, enddate]
        ulist = ulist.filter(Ecotype__contains=eco1)
        mywhere.append('ecotype='+eco1)

    eco2 = request.GET.get("eco2", None)
    if eco2:
        print(eco2)
        #date__range=[startdate, enddate]  & update_at=[startdate, enddate]
        ulist = ulist.filter(Ecotype__contains=eco2)
        mywhere.append('ecotype='+eco2)

    pod1 = request.GET.get("pod1", None)
    if pod1:
        print(pod1)
        #date__range=[startdate, enddate]  & update_at=[startdate, enddate]
        ulist = ulist.filter(Pods__contains=pod1)
        mywhere.append('Pods='+pod1)

    pod2 = request.GET.get("pod2", None)
    if pod2:
        print(pod2)
        #date__range=[startdate, enddate]  & update_at=[startdate, enddate]
        ulist = ulist.filter(Pods__contains=pod2)
        mywhere.append('Pod2='+pod2)

    calltype1 = request.GET.get("calltype1", None)
    if calltype1:
        print(calltype1)
        # date__range=[startdate, enddate]  & update_at=[startdate, enddate]
        ulist = ulist.filter(Calltype__icontains=calltype1)
        mywhere.append('Calltype=' + calltype1)

    calltype2 = request.GET.get("calltype2", None)
    if calltype2:
        print(calltype2)
        # date__range=[startdate, enddate]  & update_at=[startdate, enddate]
        ulist = ulist.filter(Calltype__icontains=calltype2)
        mywhere.append('Calltype=' + calltype2)

    calltype4 = request.GET.get("calltype4", None)
    if calltype4:
        print(calltype4)
        # date__range=[startdate, enddate]  & update_at=[startdate, enddate]
        ulist = ulist.filter(Calltype__icontains=calltype4)
        mywhere.append('Calltype=' + calltype4)


    anno_type = request.GET.get("anno_type", None)
    if anno_type:
        print(anno_type)
        # date__range=[startdate, enddate]  & update_at=[startdate, enddate]
        ulist = ulist.filter(Annotation_type=anno_type)
        mywhere.append('anno_type=' + anno_type)

    #获取并判断搜索菜品类别条件
    format = '%Y-%m-%d'
    if request.GET.get("start_date", None):
        start_date = datetime.strptime(request.GET.get("start_date", None), format)
    if request.GET.get("end_date", None):
        end_date = datetime.strptime(request.GET.get("end_date", None), format)

    '''if start_date or end_date:
        print(start_date)
        print(end_date)
        #ulist = ulist.filter(update_at=[start_date, end_date])
        #mywhere.append('category_id='+cid)
    '''
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

    context = {"datasetlist": list2, 'plist': plist, 'pIndex': pIndex, 'maxpages': maxpages, 'mywhere': mywhere,
                "species": species_dict, "ecotype": ecotype_dict, "pods": pods_dict, "calltype": calltype_dict}

    #context = {'categorylist': request.session.get("categorylist",{}).items()}
    return render(request, "web/index.html", context)

def download(request, filename):
    ''' 加载登陆表单页 '''
    # 根据登录账号获取登录者信息
    print(request.session['webuser'])
    user = request.session['webuser']['username']
    email = request.session['webuser']['email']
    #user = request.POST['username']
    print(user)
    print(email)
    print(user + " " + email + " is downloading file: ")
    print(user + " " + email + " is downloading file: " + filename)
    dh = Download_history() #Initialize the download history
    dh.user_id = request.session['webuser']['id']
    dh.username = request.session['webuser']['username']
    dh.email = request.session['webuser']['email']
    dh.download_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if filename.startswith('y'):  # save yaml download history
        mm = Model.objects.get(yaml_file=filename)  # get information of model
        dh.model_ID = mm.ID
        dh.model_name = mm.model_name
        dh.filename = filename
        dh.save()
    elif filename.startswith('m'):  # save model package download history
        mm = Model.objects.get(model_package_file=filename)  # get information of model
        dh.model_ID = mm.ID
        dh.model_name = mm.model_name
        dh.filename = filename
        dh.save()
    else:  # save datasets download history
        dd = DatasetDetail.objects.get(File_name=filename) # get informaiton of archive file
        dataset_id = dd.Dataset_ID
        ds = Datasets.objects.get(ID=dataset_id) # get informaiton of dataset
        dh.datasetdetail_ID = dd.ID
        dh.dataset_ID = dataset_id
        dh.dataset_name = ds.Dataset_Name
        dh.filename = filename
        dh.save()
    return render(request, "web/about.html")


def login(request):
    ''' 加载登陆表单页 '''
    shoplist = Shop.objects.filter(status=1)
    context = {'shoplist': shoplist}
    return render(request, "web/login.html", context)

def dologin(request):
    ''' 执行登陆操作 '''
    try:
        #执行是否选择店铺判断
        #if request.POST['shop_id'] == '0':
        #    return redirect(reverse('web_login')+"?errinfo=1")

        #执行验证码的校验
        if request.POST['code'] != request.session['verifycode']:
            return redirect(reverse('web_login')+"?errinfo=2")
        
        #根据登录账号获取登录者信息
        user = User.objects.get(username=request.POST['username'])
        #判断当前用户是Administrator/Data Manager/Register User
        if user.status == 1 or user.status == 2 or user.status == 6:
            #判断登录密码是否相同
            import hashlib
            md5 = hashlib.md5()
            s = request.POST['pass']+user.password_salt #从表单中获取密码并添加干扰值
            md5.update(s.encode('utf-8')) #将要产生md5的子串放进去
            if user.password_hash == md5.hexdigest(): #获取md5值
                print('登录成功')
                #将当前登录成功的用户信息以webuser为key写入到session中
                request.session['webuser'] = user.toDict()
                '''获取当前店铺信息
                shopob = Shop.objects.get(id=request.POST['shop_id'])
                request.session['shopinfo'] = shopob.toDict()
                #获取当前店铺中所有的菜品类别和菜品信息
                clist = Category.objects.filter(shop_id = shopob.id,status=1)
                categorylist = dict() #菜品类别（内含有菜品信息）
                productlist = dict() #菜品信息
                #遍历菜品类别信息
                for vo in clist:
                    c = {'id':vo.id,'name':vo.name,'pids':[]}
                    plist = Product.objects.filter(category_id=vo.id,status=1)
                    #遍历当前类别下的所有菜品信息
                    for p in plist:
                        c['pids'].append(p.toDict())
                        productlist[p.id]=p.toDict()
                    categorylist[vo.id] = c  
                
                #将上面的结果存入到session中
                request.session['categorylist'] = categorylist
                request.session['productlist'] = productlist
                '''

                #重定向到下载页
                return redirect(reverse("web_index"))
            else:
                return redirect(reverse('web_login')+"?errinfo=5")
        else:
            return redirect(reverse('web_login')+"?errinfo=4")
    except Exception as err:
        print(err)
        return redirect(reverse('web_login')+"?errinfo=3")

def logout(request):
    ''' 执行前台Log Off操作 '''
    del request.session['webuser']
    return redirect(reverse('web_index'))

def verify(request):
    '''生成验证码 '''
    #引入随机函数模块
    import random
    from PIL import Image, ImageDraw, ImageFont
    #定义变量，用于画面的背景色、宽、高
    #bgcolor = (random.randrange(20, 100), random.randrange(
    #    20, 100),100)
    bgcolor = (242,164,247)
    width = 100
    height = 25
    #创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    #创建画笔对象
    draw = ImageDraw.Draw(im)
    #调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    #定义验证码的备选值
    #str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    str1 = '0123456789'
    #随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    #构造字体对象，ubuntu的字体路径为“/usr/share/fonts/truetype/freefont”
    font = ImageFont.truetype('static/arial.ttf', 21)
    #font = ImageFont.load_default().font
    #构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    #绘制4个字
    draw.text((5, -3), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, -3), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, -3), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, -3), rand_str[3], font=font, fill=fontcolor)
    #释放画笔
    del draw
    #存入session，用于做进一步验证
    request.session['verifycode'] = rand_str
    """
    python2的为
    # 内存文件操作
    import cStringIO
    buf = cStringIO.StringIO()
    """
    # 内存文件操作-->此方法为python3的
    import io
    buf = io.BytesIO()
    #将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    #将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')