from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    picture = models.FileField(upload_to='img/', blank=True, null=True)
    # image = models.ImageField(upload_to="img/",
    #                           verbose_name=u'Ваше фото', help_text='150x150px')
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title



# topic = models.ForeignKey(Topic, null=True, blank=True)
#
#
# class Topic(models.Model):
#     name = models.CharField(max_length=255)


class News(models.Model):
    title = models.CharField(verbose_name=u'Заголовок', max_length=255)


def handle_uploaded_file(f):
    with open('/file_tmp.tmp/', 'w+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

#
# class ExampleModel(models.Model):
#     model_pic = models.ImageField(upload_to='pic_folder/', default='pic_folder/None/no-img.jpg')
