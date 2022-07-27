#Visotor page
from django.urls import path,include

from web.views import index, cart, orders, views, models
from myadmin.views import dataset
from myadmin.views import archive
from myadmin.views import user

urlpatterns = [
    path('', index.index, name="index"),
    path('download/<str:filename>/', index.download, name="web_download"),
    path('webuser/insert', user.webuserinsert, name="web_user_insert"), #执行添加
    #前端登陆Log Off的路由
    path('login', index.login, name="web_login"), #加载登录表单
    path('dologin', index.dologin, name="web_dologin"), #web_dologin
    path('logout', index.logout, name="web_logout"), #Log Off
    path('verify', index.verify, name="web_verify"), #Front End Verify Code
    path('signup', index.signup, name="web_signup"), #Frontend Signup
    path('help', index.help, name="web_help"), #Frontend Help
    path('about', index.about, name="web_about"), #Frontend About

    #为url路由添加请求前缀web/,凡是带此前缀的url地址必须登录后才可访问
    path("web/", include([
        path('', index.webindex, name="web_index"), #前台大堂点餐首页

        path('<int:pIndex>', index.webindex, name="web_index"), #前台Dataset首页
        #购物车信息管理路由
        path('cart/add/<str:pid>', cart.add, name="web_cart_add"), #购物车添加
        path('cart/delete/<str:pid>', cart.delete, name="web_cart_delete"), #购物车删除
        path('cart/clear', cart.clear, name="web_cart_clear"), #购物车清空
        path('cart/change', cart.change, name="web_cart_change"), #购物车更改

        #Model处理路由
        path('models/<int:pIndex>', models.index, name="web_models_index"), #可供下载的模型浏览
        path('orders/<int:pIndex>', orders.index, name="web_orders_index"), #订单浏览
        path('orders/insert', orders.insert, name="web_orders_insert"), #执行订单添加
        path('orders/detail', orders.detail, name="web_orders_detail"), #订单详情
        path('orders/status', orders.status, name="web_orders_status"), #修改订单状态

        # Dataset Query pages
        path('datasets/<int:pIndex>', views.index, name="web_datasets_index"),  # Dataset浏览
        #path('orders/detail', orders.detail, name="web_datasets_detail"),  # 订单详情
        path('detail/<int:pid>', views.dataset_detail, name="web_dataset_detail"), #订单详情
        #path('download/<slug:slug>', index.download, name="web_download"), #file download processing
        # Dataset Query pages
        path('index/', views.index),  # 订单浏览

    ]))
]
