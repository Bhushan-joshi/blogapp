# Generated by Django 3.0.5 on 2020-04-18 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_auto_20200417_1641'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user',
            new_name='author',
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='kick.png', upload_to='images'),
        ),
    ]