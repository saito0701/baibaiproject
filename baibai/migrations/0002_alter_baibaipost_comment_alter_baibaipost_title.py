# Generated by Django 4.0 on 2024-11-25 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baibai', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baibaipost',
            name='comment',
            field=models.TextField(verbose_name='コメント'),
        ),
        migrations.AlterField(
            model_name='baibaipost',
            name='title',
            field=models.CharField(max_length=200, verbose_name='タイトル'),
        ),
    ]
