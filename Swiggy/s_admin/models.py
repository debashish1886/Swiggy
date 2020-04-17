from django.db import models

class AdminLoginModel(models.Model):
    username=models.CharField(unique=True,max_length=30)
    password=models.CharField(max_length=30)
    otp=models.IntegerField()

class StateModel(models.Model):
    state_no=models.AutoField(primary_key=True)
    state_name=models.CharField(max_length=30,unique=True)

    def __str__(self):
        return self.state_name

class CityModel(models.Model):
    city_no=models.AutoField(primary_key=True)
    city_name=models.CharField(max_length=30,unique=True)
    state=models.ForeignKey(StateModel,on_delete=models.CASCADE)

    def __str__(self):
        return self.city_name

class AreaMOdel(models.Model):
    area_no=models.AutoField(primary_key=True)
    area_name=models.CharField(max_length=40)
    city=models.ForeignKey(CityModel,on_delete=models.CASCADE)

    def __str__(self):
        return self.area_name

class RestaurantTypeModel(models.Model):
    no = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=50)

    def __str__(self):
        return self.type_name