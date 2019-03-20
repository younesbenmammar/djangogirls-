from django.db import models
from django.utils import timezone



class Post(models.Model):
    auteur = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    titre = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)


    def publier(self):
        self.published_date = timezone.now
        self.save

    def __str__(self):
        return self.titre

# Create your models here.
