from django.db import models

# Create your models here.
class Topic(models.Model):
    title=models.CharField( max_length=50,primary_key=True)
    
    def __Str__(self):
        return self.title
    
class Website(models.Model):
    title=models.ForeignKey(Topic, on_delete=models.CASCADE)
    name=models.CharField(max_length=50,primary_key=True)
    url=models.URLField( max_length=200)
    email=models.EmailField( max_length=254)
    
    def __Str__(self):
        return self.name
    
class Access(models.Model):
    name=models.ForeignKey(Website, on_delete=models.CASCADE)
    date=models.DateField()
    author=models.CharField(max_length=50)
    
    def __str__(self):
        return self.author
    