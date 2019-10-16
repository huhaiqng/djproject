# Generated by Django 2.2.5 on 2019-10-16 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deployjar', '0007_auto_20191016_0949'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jarmodel',
            name='instance',
        ),
        migrations.AddField(
            model_name='jarmodel',
            name='pro_instance',
            field=models.ManyToManyField(to='deployjar.Instance', verbose_name='生产实例'),
        ),
    ]
