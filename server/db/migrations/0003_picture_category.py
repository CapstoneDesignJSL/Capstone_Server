# Generated by Django 2.1.7 on 2019-03-25 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_auto_20190325_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='category',
            field=models.CharField(default=None, max_length=10),
        ),
    ]