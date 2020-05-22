from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='dp')

    def __str__(self):
        return f"{self.user} Profile"

    def save(self, *args, **kawrgs):
        super().save(*args, **kawrgs)
        image = Image.open(self.image.path)
        if image.height > 300 or image.width > 300:
            reshape = (300, 300)
            image.thumbnail(reshape)
            image.save(self.image.path)
