#coding: utf-8

from django.db import models
import datetime
import os
# Create your models here.
class Record(models.Model):
    name = models.CharField('Имя', max_length=30)
    text = models.TextField('Текст', max_length = 2000)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзывы'
        
def make_upload_path(instance, filename):
    now = datetime.datetime.now()
    path, ext = os.path.splitext(filename)
    fn = "f%s%s%s%s%s%s"%(now.year, now.month, now.day, now.hour, now.minute, now.second)
    return "uploads/%s%s"%(fn, ext)

class Gallery(models.Model):
    name = models.CharField('Название галереи', max_length = 300)
    date_created = models.DateTimeField('Время создания', auto_now_add = True)

    class Meta:
        ordering = ('-date_created', )
        verbose_name = 'фотогалерея'
        verbose_name_plural = 'фотогалереи'

    def __unicode__(self):
        return self.name

    def get_fotos(self):
        return Foto.objects.filter(gallery__id = self.id)

class Foto(models.Model):
    gallery = models.ForeignKey(Gallery, verbose_name = 'Фотогалерея')
    foto = models.ImageField('Фото', upload_to = make_upload_path)
    comment = models.CharField('Примечание', max_length = 300)
    date_created = models.DateTimeField('Время создания', auto_now_add = True)

    def __unicode__(self):
        return '%s - %s' % (self.gallery.name, self.comment)

    class Meta:
        ordering = ('-date_created', )
        verbose_name = 'фото'
        verbose_name_plural = 'фотографии'