# Generated by Django 3.0.7 on 2020-06-27 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EAS', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='identity',
            field=models.CharField(default='student', max_length=32),
        ),
        migrations.AlterField(
            model_name='user',
            name='grade',
            field=models.IntegerField(default=1),
        ),
    ]
