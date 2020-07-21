from django.db import models

# Create your models here.
class signup(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField(max_length=100)
    gender=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    occupation=models.CharField(max_length=100)
    secret_number=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class releases(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(blank=True,upload_to="releases")
    video=models.CharField(max_length=500)
    title=models.CharField(blank=True,max_length=400)

    def __str__(self):
        return self.name

class discover(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(blank=True,upload_to="discover")
    video=models.CharField(max_length=500)
    title = models.CharField(blank=True, max_length=400)

    def __str__(self):
        return self.name

class features(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(blank=True,upload_to="features")
    video=models.CharField(max_length=500)
    title = models.CharField(blank=True, max_length=400)

    def __str__(self):
        return self.name

class ads(models.Model):
    ad1=models.ImageField(blank=True,upload_to="ads")
    ad2=models.ImageField(blank=True,upload_to="ads")



class add(models.Model):
   ad = models.FileField(upload_to="addd",blank=True)