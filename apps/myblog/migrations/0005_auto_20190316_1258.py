# Generated by Django 2.1.3 on 2019-03-16 04:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0004_auto_20190315_0020'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name': '类别', 'verbose_name_plural': '分类列表'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['name'], 'verbose_name': '标签', 'verbose_name_plural': '标签列表'},
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myblog.Category', verbose_name='文章分类'),
        ),
    ]
