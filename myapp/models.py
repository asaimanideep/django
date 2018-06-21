from django.db import models

class Person(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    address=models.CharField(max_length=50)
    mobile_num=models.IntegerField()
    city=models.CharField(max_length=30)
    state=models.CharField(max_length=30)
    country=models.CharField(max_length=30)
    zipcode=models.IntegerField()

    def __str__(self):
        return self.firstname +' '+ self.lastname
