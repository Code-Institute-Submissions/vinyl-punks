# Generated by Django 3.1.3 on 2021-02-12 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_album_avg_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='era',
            field=models.IntegerField(choices=[(1980, '1980'), (1990, '1990'), (2000, '2000'), (2010, '2010'), (2020, '2020')], default=1990),
        ),
    ]
