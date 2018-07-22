from django.db import models

class Memo(models.Model):
    title = models.CharField(max_length = 200)
    text = models.TextField()
    words = models.IntegerField(default = 0)

    class Meta:
        ordering = ['words']
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'

    def __str__(self):
        return self.title
# Create your models here.
