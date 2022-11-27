from django.conf import settings
from django.db import models


class Ad(models.Model):
    title = models.CharField(max_length=150, unique=True, null=False, blank=False)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=500, null=True, blank=True)
    author = models.ForeignKey("users.User", verbose_name='Автор', related_name='ad', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='ad_images', null=True, blank=True)

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
        ordering = ("-created_at",)

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.CharField(max_length=150, unique=True, null=False, blank=False)
    author = models.ForeignKey("users.User", verbose_name='Автор', related_name='comment', on_delete=models.CASCADE)
    ad = models.ForeignKey(Ad, verbose_name='Объявление', related_name='comment', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        ordering = ("-created_at",)


