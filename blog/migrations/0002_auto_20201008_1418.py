# Generated by Django 3.0.7 on 2020-10-08 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('PUBLISHED', 'published'), ('UPDATED', 'updated')], default='', max_length=15),
        ),
    ]
