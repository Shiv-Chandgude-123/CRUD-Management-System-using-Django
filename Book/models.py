from django.db import models

# Create your models here.

class book(models.Model):
    book_name = models.CharField(max_length=20)
    book_price = models.FloatField()
    author = models.CharField(max_length=20)
    pubdate = models.DateField()
    qty = models.IntegerField()


    def __str__(self):
        return self.book_name

class employee(models.Model):
    ename = models.CharField(max_length=20)
    sal = models.FloatField()
    deptno = models.IntegerField()
    job = models.CharField(max_length=20)
    age = models.IntegerField()

    def __str__(self):
        return self.ename