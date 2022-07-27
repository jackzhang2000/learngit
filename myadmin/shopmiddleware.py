#自定义中间类（执行是否登录判断）
from django.shortcuts import redirect
from django.urls import reverse
import re

class ShopMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("ShopMiddleware")

    def __call__(self, request):
        path = request.path
        print("url:", path)

        #Determine whether the management part is logged in
        #定义后台不登录也可直接访问的url列表

        urllist = ['/myadmin/login', '/myadmin/logout','/myadmin/dologin', '/myadmin/verify']
        #判断当前请求url地址是否是以/myadmin开头,并且不在urllist中，才做是否登录判断
        if re.match(r'^/myadmin', path) and (path not in urllist):
            #判断是否登录(在于session中没有adminuser)
            if 'adminuser' not in request.session:
                #重定向到登录页
                return redirect(reverse("myadmin_login"))
                #pass

        ##Determine whether the visitor part is logged in（session中是否有webuser）
        # Define a list of urls that can be accessed directly without logging in in the visitor part
        url_download = ['/web/download']
        print()
        print(request.session)
        if 'webuser' not in request.session and re.match(r'^/download', path):
        #if re.match(r'^/static/uploads', path):
            #disable web user login requirement unless downloading files
            return redirect(reverse("web_download"))

        response = self.get_response(request)
        # Code to be executed for each request/response after
        # the view is called.
        return response