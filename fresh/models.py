from django.db import models

class UserInfo(models.Model):
	uname = models.CharField(max_length=20)
	upwd = models.CharField(max_length=40)
	uemail = models.CharField(max_length=30)
	ushou = models.CharField(max_length=20,default='')
	uaddress = models.CharField(max_length=100,default='')
	uyoubian = models.CharField(max_length=6,default='')
	uphone = models.CharField(max_length=11,default='')
	#default,blank是python层面的约束，不影响数据库表结构
	def __str__(self):
		return self.uname

'''
class TypeInfo(models.Model):
	title = models.CharField(max_length=20)
	isDelete = models.BooleanField()

class GoodsInfo(models.Model):
	gtitle = models.CharField(max_length=20)
	gtype = models.ForeignKey(TypeInfo)
	gprice = models.DecimalField()
	gdesc = models.BooleanField()
	isDelete = models.BooleanField()

class CarInfo(models.Model):
	user = models.ForeignKey(UserInfo)
	goods = models.ForeignKey(GoodsInfo)
	count = models.IntegerField()

class OrderInfo(models.Model):
	user = models.ForeignKey(UserInfo)
	ototal = models.CharField()
	state = models.CharField()

class OrderDetailInfo(models.Model):
	order = models.ForeignKey(OrderInfo)
	goods = models.ForeignKey(GoodsInfo)
	count = models.IntegerField()
	price = models.DecimalField()
'''