#后台管理子路由文件
from django.urls import path

from myadmin.views import index
from myadmin.views import user
from myadmin.views import shop
from myadmin.views import category
from myadmin.views import product
from myadmin.views import productbak
from myadmin.views import member
from myadmin.views import annotation
from myadmin.views import model
from myadmin.views import dataset
from myadmin.views import archive
from myadmin.views import download_history

urlpatterns = [
    path('', index.index, name="myadmin_index"), #后台首页
    path('help', index.help, name="myadmin_help"), #Help page

    #后台管理员登录、Log Off路由
    path('login', index.login, name="myadmin_login"), #加载登录表单
    path('dologin', index.dologin, name="myadmin_dologin"), #执行登录
    path('logout', index.logout, name="myadmin_logout"), #Log Off
    path('verify', index.verify, name="myadmin_verify"), #输出验证码

    #员工信息管理路由
    path('user/<int:pIndex>', user.index, name="myadmin_user_index"), #浏览
    path('user/add', user.add, name="myadmin_user_add"), #添加表单
    path('user/insert', user.insert, name="myadmin_user_insert"), #执行添加
    path('user/del/<int:uid>', user.delete, name="myadmin_user_delete"), #执行删除
    path('user/edit/<int:uid>', user.edit, name="myadmin_user_edit"), #加载编辑表单
    path('user/update/<int:uid>', user.update, name="myadmin_user_update"), #执行编辑

    #Download History
    path('downloadhist/<int:pIndex>', download_history.index, name="myadmin_downloadhist_index"), #浏览
    path('export', download_history.export_users_csv, name="export_users_csv"), #export to csv

    #Help Page for DataPortal Manager
    path('export', download_history.export_users_csv, name="export_users_csv"), #export to csv

    #店铺信息管理路由
    path('shop/<int:pIndex>', shop.index, name="myadmin_shop_index"), #浏览
    path('shop/add', shop.add, name="myadmin_shop_add"), #添加表单
    path('shop/insert', shop.insert, name="myadmin_shop_insert"), #执行添加
    path('shop/del/<int:sid>', shop.delete, name="myadmin_shop_delete"), #执行删除
    path('shop/edit/<int:sid>', shop.edit, name="myadmin_shop_edit"), #加载编辑表单
    path('shop/update/<int:sid>', shop.update, name="myadmin_shop_update"), #执行编辑

    #菜品类别信息管理路由
    path('category/<int:pIndex>', category.index, name="myadmin_category_index"), #浏览
    path('category/load/<int:sid>', category.loadCategory, name="myadmin_category_load"),
    path('category/add', category.add, name="myadmin_category_add"), #添加表单
    path('category/insert', category.insert, name="myadmin_category_insert"), #执行添加
    path('category/del/<int:cid>', category.delete, name="myadmin_category_del"), #执行删除
    path('category/edit/<int:cid>', category.edit, name="myadmin_category_edit"), #加载编辑表单
    path('category/update/<int:cid>', category.update, name="myadmin_category_update"), #执行编辑

    #菜品信息管理路由
    path('product/<int:pIndex>', productbak.index, name="myadmin_product_index"), #浏览
    path('product/add', productbak.add, name="myadmin_product_add"), #添加表单
    path('product/insert', productbak.insert, name="myadmin_product_insert"), #执行添加
    path('product/del/<int:pid>', product.delete, name="myadmin_product_del"), #执行删除
    path('product/edit/<int:pid>', product.edit, name="myadmin_product_edit"), #加载编辑表单
    path('product/update/<int:pid>', product.update, name="myadmin_product_update"), #执行编辑

    #Dataset Management URL
    path('dataset/<int:pIndex>', dataset.index, name="myadmin_dataset_index"), #浏览
    path('dataset/add', dataset.add, name="myadmin_dataset_add"), #添加表单
    path('dataset/insert', dataset.insert, name="myadmin_dataset_insert"), #执行添加
    path('dataset/del/<int:pid>', dataset.delete, name="myadmin_dataset_del"), #执行删除
    path('dataset/edit/<int:pid>', dataset.edit, name="myadmin_dataset_edit"), #加载编辑表单
    path('dataset/update/<int:pid>', dataset.update, name="myadmin_dataset_update"), #执行编辑
    path('dataset/detail/<int:pid>', dataset.detail, name="myadmin_dataset_detail"), #订单详情

    #Dataset achive management URL
    path('archive/<int:pIndex>', archive.index, name="myadmin_archive_index"), #浏览
    path('archive/add/<int:did>', archive.add, name="myadmin_archive_add"), #添加表单
    path('archive/insert', archive.insert, name="myadmin_archive_insert"), #执行添加
    path('archive/del/<int:did>', archive.delete, name="myadmin_archive_del"), #执行删除
    path('archive/edit/<int:did>', archive.edit, name="myadmin_archive_edit"), #加载编辑表单
    path('archive/update/<int:did>', archive.update, name="myadmin_archive_update"), #执行编辑

    #Annotation Management URL
    path('annotation/<int:pIndex>', annotation.index, name="myadmin_annotation_index"), #浏览
    path('annotation/<int:pid>', annotation.index, name="myadmin_annotation_index"), #Browse the annotations of a dataset
    path('annotation/add', annotation.add, name="myadmin_annotation_add"), #添加表单
    path('annotation/add/<int:did>', annotation.add, name="myadmin_annotation_add"),
    path('annotation/insert', annotation.insert, name="myadmin_annotation_insert"), #执行添加
    path('annotation/del/<int:pid>', annotation.delete, name="myadmin_annotation_del"), #执行删除
    path('annotation/edit/<int:pid>', annotation.edit, name="myadmin_annotation_edit"), #加载编辑表单
    path('annotation/update/<int:pid>', annotation.update, name="myadmin_annotation_update"), #执行编辑
    #path(r'^upload/csv/$', annotation.upload_csv, name="upload_csv"), #执行编辑


    #Model Management URL
    path('model/<int:pIndex>', model.index, name="myadmin_model_index"), #浏览
    path('model/add', model.add, name="myadmin_model_add"), #添加表单
    path('model/insert', model.insert, name="myadmin_model_insert"), #执行添加
    path('model/del/<int:pid>', model.delete, name="myadmin_model_del"), #执行删除
    path('model/edit/<int:pid>', model.edit, name="myadmin_model_edit"), #加载编辑表单
    path('model/update/<int:pid>', model.update, name="myadmin_model_update"), #执行编辑
    path('model/detail/<int:pid>', model.detail, name="myadmin_model_detail"), #订单详情

    #会员信息管理路由
    path('member/<int:pIndex>', member.index, name="myadmin_member_index"), #浏览
]