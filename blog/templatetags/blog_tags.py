from ..models import Post, Category
from django import template

register = template.Library()

@register.simple_tag
def get_recent_posts(num=5):
    '''侧边栏-最近文章'''
    return Post.objects.all().order_by('-created_time')[:num]

@register.simple_tag
def archives():
    '''
    侧边栏-归档
    :return: 返回‘created_time’字段的date对象列表，精确到月份
    '''
    return Post.objects.dates('created_time', 'month', order='DESC')

@register.simple_tag
def get_categories():
    return Category.objects.all()