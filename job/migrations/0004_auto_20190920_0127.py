# Generated by Django 2.1.4 on 2019-09-19 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_auto_20190122_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='bookimage',
            field=models.ImageField(default='images/ds.jpg', upload_to='images/'),
        ),
    ]
