from django.db import models

# Create your models here.

#通过写类，来创建使用数据库，然后使用下列语句执行sql语句


#object.save()
#object.delete()



class Student(models.Model):
    objects = None
    s_name = models.CharField(max_length=16, unique=True)
    S_age = models.IntegerField(default=1)


