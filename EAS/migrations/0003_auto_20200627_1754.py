# Generated by Django 3.0.7 on 2020-06-27 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EAS', '0002_auto_20200627_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='former',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='EAS.Course'),
        ),
    ]
