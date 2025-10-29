from django.db import models

# Create your models here.
class Myself(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)  # discription -> description
    image = models.ImageField(upload_to='image', blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title