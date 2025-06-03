from django.db import models


class Movies(models.Model):
    name = models.CharField(max_length=40, null=False)
    genre = models.CharField(max_length = 30, null=False)
    duration = models.IntegerField(null=False)
    cost = models.IntegerField(null=False)
    picture = models.ImageField(upload_to= "movies_images", null= True)
    
    
    def __str__(self):
        return str(self.name)
