from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    excerpt = models.CharField(max_length=200, blank=True)
    author = models.ForeignKey(User)
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})
    class Meta:
        '''
        ordering 属性用来指定文章排序方式，['-created_time'] 指定了依据哪个属性的值进行排序，
        这里指定为按照文章发布时间排序，且负号表示逆序排列。列表中可以用多个项，比如
        ordering = ['-created_time', 'title'] ，那么首先依据 created_time 排序，如果
        created_time 相同，则再依据 title 排序。这样指定以后所有返回的文章列表都会自动按照 Meta
        中指定的顺序排序，因此可以删掉视图函数中对文章列表中返回结果进行排序的代码了。
        '''
        ordering = ['-created_time']
