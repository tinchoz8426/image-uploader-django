# Generated by Django 4.1 on 2022-09-10 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_image', '0002_image_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='archivo',
            field=models.FileField(default='prueba.png', upload_to=''),
            preserve_default=False,
        ),
    ]
