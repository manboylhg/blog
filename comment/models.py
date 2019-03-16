from django.db import models

# Create your models here.

from django.utils.timezone import now
from apps.myblog.models import Article

# 评论Models
class Comment(models.Model):

    name = models.CharField(verbose_name='用户名', max_length=50, blank=True, null=True)
    email = models.EmailField(verbose_name='邮件地址', max_length=100, default='904405840@qq.com')
    article = models.ForeignKey(Article, verbose_name='对应文章', on_delete=models.CASCADE, blank=True, null=True)
    content = models.TextField(verbose_name='评论内容', blank=True, null=True)
    created_time = models.DateTimeField(verbose_name='创建时间', default=now)
    last_modified_time = models.DateTimeField(verbose_name='最近修改时间', default=now)

    class Meta:
        ordering = ['-created_time']
        verbose_name = '评论'  # 指定后台显示模型名称
        verbose_name_plural = '评论列表'  # 指定后台显示模型复数名称
        db_table = 'comment'
    def __str__(self):
        return self.content[:20]


