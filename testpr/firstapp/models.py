from django.db import models

# Create your models here.


class ToDo(models.Model):
    title = models.CharField('Название задания', max_length=500)
    status = models.CharField('Статус', max_length= 300, default="не начато")

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'

    def __str__(self) -> str:
        return self.title
    

class ToDoHistory(models.Model):
    title = models.CharField('Название задания', max_length=500)
    status = models.CharField('Статус', max_length= 300, default="не начато")

    class Meta:
        verbose_name = 'archive Задание'
        verbose_name_plural = 'История заданий'

    def __str__(self) -> str:
        return self.title
    

