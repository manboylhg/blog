# Generated by Django 2.1.3 on 2019-03-16 04:58

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('myblog', '0005_auto_20190316_1258'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, null=True, verbose_name='评论内容')),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('last_modified_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='最近修改时间')),
                ('article', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myblog.Article', verbose_name='对应文章')),
            ],
            options={
                'verbose_name': '评论',
                'ordering': ['-created_time'],
                'db_table': 'comment',
                'verbose_name_plural': '评论列表',
            },
        ),
    ]
