# Generated by Django 4.2.7 on 2023-11-21 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='defaultt', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
