# Generated by Django 4.2.3 on 2023-07-12 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avicenna', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(default='f05d77fd', max_length=100, unique=True),
        ),
    ]
