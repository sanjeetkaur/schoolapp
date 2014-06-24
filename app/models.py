from django.db import models
# Create your models here.
 
class list(models.Model):
    name = models.CharField(max_length=20)
    roll_no = models.IntegerField(max_length=10)
    branch = models.CharField(max_length=10)
    session = models.IntegerField(max_length=4)
    marks = models.IntegerField(max_length=4)
    backlog = models.CharField(max_length=10)
    def __unicode__(self):
         return self.roll_no
