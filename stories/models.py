from email.mime import image
from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField()
    img_name= models.CharField(max_length=44)
    img_caption= models.TextField()
    likes = models.IntegerField()
    comments = models.CharField(max_length=1001)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()



class Profile(models.Model):
    photo = models.ImageField()
    bio = models.TextField()


    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()






