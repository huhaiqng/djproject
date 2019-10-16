# Generated by Django 2.2.5 on 2019-10-16 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deployjar', '0010_auto_20191016_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jarmodel',
            name='pro_instance',
            field=models.ManyToManyField(blank=True, null=True, related_name='pro', to='deployjar.Instance', verbose_name='生产实例'),
        ),
        migrations.AlterField(
            model_name='jarmodel',
            name='test_instance',
            field=models.ManyToManyField(blank=True, null=True, related_name='test', to='deployjar.Instance', verbose_name='测试实例'),
        ),
    ]
