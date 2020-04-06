from django.db import models

# Create your models here.
class Students(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    resImage = models.FileField(upload_to='images/')

    def __str__(self):
        return str(self.name)	
