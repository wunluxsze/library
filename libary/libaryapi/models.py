from django.db import models

# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    autor = models.CharField(max_length=200)
    read = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.title

    def __str__(self):
        return self.date

    def __str__(self):
        return self.autor