from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from django.urls import reverse
# Create your models here.

class Gram(models.Model):
    Photo = models.ImageField(upload_to="media/",blank=False)
    comment = models.TextField(blank=True,null=True)
    date = models.DateTimeField(auto_now_add=True,null=True)
    author = models.ForeignKey(
    get_user_model(),
    on_delete=models.CASCADE,
    null=True,
    )


    def get_absolute_url(self):
        return reverse("display")


class Reply(models.Model):
    post = models.ForeignKey(Gram,
    on_delete=models.CASCADE,
    related_name="replys")
    reply = models.CharField(max_length=100)
    author =  models.ForeignKey(
    get_user_model(),
    on_delete=models.CASCADE,
    null=True,
    )

    def __str__(self):
        return self.reply

    def get_absolute_url(self):
        return reverse("display")
