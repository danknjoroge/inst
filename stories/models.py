from django.db import models

# Create your models here.

class Profile(models.Model):
    photo = models.ImageField()
    bio = models.TextField()


    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def __str__(self):
        return self.bio



class Image(models.Model):
    image = models.ImageField(upload_to= 'images/', default="Image")
    img_name= models.CharField(max_length=44)
    img_caption= models.TextField()
    likes = models.IntegerField()
    comments = models.TextField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def search_by_img_name(cls, searchname):
        image = cls.objects.filter(img_name__icontains=searchname)
        return image


    def __str__(self):
        return self.img_name







