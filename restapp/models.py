from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Company(models.Model):
    title = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = "companies"
    def __str__(self):
        return self.title

class Rest(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    job = models.CharField(max_length=100)
    image = models.ImageField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "restModels"
    def __str__(self):
        return self.job