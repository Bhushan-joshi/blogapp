from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    image=models.ImageField(default="default.jpg", upload_to='images')

    def __str__(self):
        return f'{self.user.username} profile'
    

    def save(self,*args, **kwargs):
        super().save()

        img=Image.open(self.image.path)
        if img.height>300 and img.width>300:
            output_img=(300,300)
            img.thumbnail(output_img)
            img.save(self.image.path)
