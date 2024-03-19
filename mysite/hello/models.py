from django.db import models

class blogpost(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=12)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


    

# class Student(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     address = models.CharField(max_length=200)
#     roll_number = models.IntegerField()
#     mobile = models.CharField(max_length=10)
#   #  date = models.DateTimeField()

#     def __str__(self):
#         return self.first_name + " " + self.last_name