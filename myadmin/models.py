from django.db import models
from datetime import datetime


#Datasets table in PostgreSQL
class Datasets(models.Model):
    ID = models.AutoField(primary_key=True)     # Primary Key、Auto-increment
    Dataset_Name = models.TextField(max_length=50)    #e.g. Jasco Roberts Bank Dataset
    Num_Of_Files = models.IntegerField(default=1)  # The number of wav files
    Num_Of_Annotated_Events = models.IntegerField(default=1)  # Annotated records#
    Number_of_Subsets = models.IntegerField(default=1)  # Annotated records#
    Species_identified = models.TextField()    #Multi-line text created based on Dataset details
    Ecotype = models.TextField()  # Multi-line text created based on Dataset details
    Pods = models.TextField()  # Multi-line text created based on Dataset details
    Calltype = models.TextField()  # Multi-line text created based on Dataset details
    Sampling_rate = models.CharField(max_length=100) #96 KHz
    Total_Duration = models.CharField(max_length=100)    #1246 seconds
    File_Size = models.CharField(max_length=100)    #size of all zip files for download = models.CharField(max_length=100)  # size of all zip files for download
    Total_Size = models.CharField(max_length=100)    #size of all zip files for download
    Number_of_Subsets = models.IntegerField(default=1)    #e.g. 10 means 10 zip files
    Location = models.CharField(max_length=100)   #e.g.Roberts Bank, British Columbia
    Latitude = models.CharField(max_length=50)    #44.6488
    Longitude = models.CharField(max_length=50)  #-63.5752
    Depth = models.CharField(max_length=50)  #-63.5752  #20.5 (by meter)
    YAML_Filename = models.TextField()    #e.g. Jasco_Roberts_Bank.yml
    Summary_by_Species = models.CharField(max_length=100)    #Summary image filename by Species uploaded by the data manager
    Summary_by_Ecotypes = models.CharField(max_length=100)#Summary image filename by Ecotypes uploaded by the data manager
    Summary_by_Pods = models.CharField(max_length=100)    #Summary image filename by Pods uploaded by the data manager
    Summary_by_CallType = models.CharField(max_length=100)    #Summary image filename by CallType uploaded by the data manager
    create_at = models.DateTimeField(default=datetime.now)    #creation time
    update_at = models.DateTimeField(default=datetime.now)    #update time
    create_by = models.CharField(max_length=50)   #created by whom
    update_by = models.CharField(max_length=50)    #updated by whom
    Annotation_type = models.IntegerField()  # Detailed or Coarse, updated by annotation pages.
    record_start = models.DateTimeField()    #record start time
    record_end = models.DateTimeField()  # record end time

    def __str__(self):
        return str(self.ID) + ":"+self.Dataset_Name

    # Customized table name，Default name：myapp_dataset
    class Meta:
        db_table = "myadmin_dataset"

#DatasetDetail table in PostgreSQL
class DatasetDetail(models.Model):
    ID = models.AutoField(primary_key=True)     # Primary Key、Auto-increment
    Dataset_ID = models.IntegerField()    #Foreign Key to Dataset ID
    File_type = models.CharField(max_length=50)  # wav, zip, yml, tsv, etc.
    File_name = models.TextField()  # e.g. Roberts_Bank001.zip
    Download_link = models.TextField()    #e.g.http://halo.dal.ca/data/Roberts_Bank001.zip
    create_at = models.DateTimeField(default=datetime.now)    #creation time
    update_at = models.DateTimeField(default=datetime.now)    #update time
    create_by = models.CharField(max_length=50)   #created by whom
    update_by = models.CharField(max_length=50)    #updated by whom
    Dataset_Name = models.TextField(max_length=50)

    def __str__(self):
        return self.Dataset_Name + ":"+self.File_name

    # Customized table name，Default name：myapp_dataset
    class Meta:
        db_table = "myadmin_datasetdetail"


#Annotation Tables
class Annotation(models.Model):
    ID = models.AutoField(primary_key=True)     # Primary Key、Auto-increment
    Dataset_ID = models.IntegerField()    #Foreign Key to Dataset ID
    Annotation_type = models.CharField(max_length=50)  # -63.5752
    File_name = models.TextField()  # e.g. Roberts_Bank001.wav
    File_path = models.TextField()  # e.g. Roberts_Bank001.wav
    Create_at = models.DateTimeField(default=datetime.now)    #creation time
    Update_at = models.DateTimeField(default=datetime.now)    #update time
    Create_by = models.CharField(max_length=50)   #created by whom
    Update_by = models.CharField(max_length=50)    #updated by whom
    Dataset_name = models.TextField(max_length=100)

    def __str__(self):
        return self.Dataset_name + ":"+self.File_name

    # Customized table name，Default name：myapp_dataset
    class Meta:
        db_table = "myadmin_annotation"

#Model Tables
class Model(models.Model):
    ID = models.AutoField(primary_key=True)     # Primary Key、Auto-increment
    yaml_file = models.TextField()
    model_name = models.TextField()
    machine_learning_method = models.TextField()  # Foreign Key to Dataset ID
    classification_level = models.TextField()  # Foreign Key to Dataset ID
    classes = models.TextField()  # Foreign Key to Dataset ID
    training_datasets = models.TextField()  # Foreign Key to Dataset ID
    Create_at = models.DateTimeField(default=datetime.now)    #creation time
    Update_at = models.DateTimeField(default=datetime.now)    #update time
    Create_by = models.CharField(max_length=50)   #created by whom
    Update_by = models.CharField(max_length=50)    #updated by whom
    model_package_file = models.TextField(max_length=100)
    test_datasets = models.TextField()  # Foreign Key to Dataset ID
    yaml_content = models.TextField()  # Foreign Key to Dataset ID

    def __str__(self):
        return self.machine_learning_method + ":"+self.model_name

    # Customized table name，Default name：myapp_dataset
    class Meta:
        db_table = "myadmin_model"

# Create your models here.
#员工账号信息模型
class User(models.Model):
    username = models.CharField(max_length=50)    #员工账号
    email = models.CharField(max_length=255)    #Email
    password_hash = models.CharField(max_length=100)#密码
    password_salt = models.CharField(max_length=50)    #密码干扰值
    status = models.IntegerField(default=1)    #:1正常/2禁用/6管理员/9删除
    create_at = models.DateTimeField(default=datetime.now)    #创建时间
    update_at = models.DateTimeField(default=datetime.now)    #修改时间
    Institution = models.CharField(max_length=255)    #密码干扰值
    Job = models.CharField(max_length=255)
    Purpose = models.CharField(max_length=255)
    Country = models.CharField(max_length=255)
    Address = models.CharField(max_length=512)


    def toDict(self):
        return {'id':self.id,'username':self.username,'email':self.email,'password_hash':self.password_hash,'password_salt':self.password_salt,'status':self.status,'create_at':self.create_at.strftime('%Y-%m-%d %H:%M:%S'),'update_at':self.update_at.strftime('%Y-%m-%d %H:%M:%S')}

    class Meta:
        db_table = "users"  # 更改表名


#Vistor download history
class Download_history(models.Model):
    user_id = models.IntegerField() # Foreign Key to user ID
    username = models.CharField(max_length=50)    #username in user table
    email = models.CharField(max_length=255)    #Email
    filename = models.CharField(max_length=512)
    datasetdetail_ID = models.IntegerField()
    dataset_ID = models.IntegerField()
    dataset_name = models.CharField(max_length=512)
    download_time = models.DateTimeField(default=datetime.now)    #downlaod time
    model_ID = models.CharField(max_length=50)    #ID in myadmin_model table
    model_name = models.CharField(max_length=50)  # model_name in myadmin_model table


    def toDict(self):
        return {'id':self.id, 'user_id':self.user_id, 'username':self.username, 'email':self.email, 'filename':self.filename, 'update_at':self.download_time.strftime('%Y-%m-%d %H:%M:%S')}

    class Meta:
        db_table = "download_history"  # Table name



class Shop(models.Model):
    name = models.CharField(max_length=255)        #店铺名称
    cover_pic = models.CharField(max_length=255)#封面图片
    banner_pic = models.CharField(max_length=255)#图标Logo
    address = models.CharField(max_length=255)    #店铺地址
    phone = models.CharField(max_length=255)    #联系电话
    status = models.IntegerField(default=1)        #状态:1正常/2暂停/9删除
    create_at = models.DateTimeField(default=datetime.now)    #创建时间
    update_at = models.DateTimeField(default=datetime.now)    #修改时间

    def toDict(self):
        shopname = self.name.split("-")
        return {'id':self.id,'name':shopname[0],'shop':shopname[1],'cover_pic':self.cover_pic,'banner_pic':self.banner_pic,'address':self.address,'phone':self.phone,'status':self.status,'create_at':self.create_at.strftime('%Y-%m-%d %H:%M:%S'),'update_at':self.update_at.strftime('%Y-%m-%d %H:%M:%S')}

    class Meta:
        db_table = "shop"  # 更改表名

#菜品分类信息模型
class Category(models.Model):
    shop_id = models.IntegerField()        #店铺id
    name = models.CharField(max_length=50)#分类名称
    status = models.IntegerField(default=1)        #状态:1正常/9删除
    create_at = models.DateTimeField(default=datetime.now)    #创建时间
    update_at = models.DateTimeField(default=datetime.now)    #修改时间

    class Meta:
        db_table = "category"  # 更改表名

#菜品信息模型
class Product(models.Model):
    shop_id = models.IntegerField()        #店铺id
    category_id = models.IntegerField()    #菜品分类id
    cover_pic = models.CharField(max_length=50)    #菜品图片
    name = models.CharField(max_length=50)#菜品名称
    price = models.FloatField()    #菜品单价
    status = models.IntegerField(default=1)        #状态:1正常/2停售/9删除
    create_at = models.DateTimeField(default=datetime.now)    #创建时间
    update_at = models.DateTimeField(default=datetime.now)    #修改时间

    def toDict(self):
        return {'id':self.id,'shop_id':self.shop_id,'category_id':self.category_id,'cover_pic':self.cover_pic,'name':self.name,'price':self.price,'status':self.status,'create_at':self.create_at.strftime('%Y-%m-%d %H:%M:%S'),'update_at':self.update_at.strftime('%Y-%m-%d %H:%M:%S')}

    class Meta:
        db_table = "product"  # 更改表名

#会员信息模型
class Member(models.Model):
    nickname = models.CharField(max_length=50)    #昵称
    avatar = models.CharField(max_length=255)    #头像
    mobile = models.CharField(max_length=50)    #电话
    status = models.IntegerField(default=1)        #状态:1正常/2禁用/9删除
    create_at = models.DateTimeField(default=datetime.now)    #创建时间
    update_at = models.DateTimeField(default=datetime.now)    #修改时间

    def toDict(self):
        return {'id':self.id,'nickname':self.nickname,'avatar':self.avatar,'mobile':self.mobile,'status':self.status,'create_at':self.create_at.strftime('%Y-%m-%d %H:%M:%S'),'update_at':self.update_at.strftime('%Y-%m-%d %H:%M:%S')}

    class Meta:
        db_table = "member"  # 更改表名

# 订单模型
class Orders(models.Model):
    shop_id = models.IntegerField()   #店铺id号
    member_id = models.IntegerField() #会员id
    user_id = models.IntegerField()   #操作员id
    money = models.FloatField()     #金额
    status = models.IntegerField(default=1)   #订单状态:1过行中/2无效/3已完成
    payment_status = models.IntegerField(default=1)   #支付状态:1未支付/2已支付/3已退款
    create_at = models.DateTimeField(default=datetime.now)  #创建时间
    update_at = models.DateTimeField(default=datetime.now)  #修改时间

    class Meta:
        db_table = "orders"  # 更改表名


#订单详情模型
class OrderDetail(models.Model):
    order_id = models.IntegerField()  #订单id
    product_id = models.IntegerField()  #菜品id
    product_name = models.CharField(max_length=50) #菜品名称
    price = models.FloatField()     #单价
    quantity = models.IntegerField()  #数量
    status = models.IntegerField(default=1) #状态:1正常/9删除

    class Meta:
        db_table = "order_detail"  # 更改表名


# 支付信息模型
class Payment(models.Model):
    order_id = models.IntegerField()  #订单id号
    member_id = models.IntegerField() #会员id
    money = models.FloatField()     #支付金额
    type = models.IntegerField()      #付款方式：1会员付款/2收银收款
    bank = models.IntegerField(default=1) #收款银行渠道:1微信/2余额/3现金/4支付宝
    status = models.IntegerField(default=1) #支付状态:1未支付/2已支付/3已退款
    create_at = models.DateTimeField(default=datetime.now)  #创建时间
    update_at = models.DateTimeField(default=datetime.now)  #修改时间

    class Meta:
        db_table = "payment"  # 更改表名
