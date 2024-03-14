from django.db import models

class Questions(models.Model):
    question = models.CharField(max_length=200,verbose_name='سوال')
    answer = models.TextField(verbose_name='جواب')


    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'سوالات متداول'
        verbose_name_plural = 'سوالات های متداول'