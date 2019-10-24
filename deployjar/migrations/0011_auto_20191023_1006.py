# Generated by Django 2.2.5 on 2019-10-23 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deployjar', '0010_auto_20191018_1221'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='host',
            name='hostuser',
        ),
        migrations.AlterField(
            model_name='host',
            name='version',
            field=models.CharField(choices=[('CentOS 6', 'CentOS 6'), ('CentOS 7', 'CentOS 7'), ('Windows 2008', 'Windows 2008')], max_length=200, verbose_name='版本'),
        ),
        migrations.AlterField(
            model_name='mysqlinstance',
            name='type',
            field=models.CharField(choices=[('master', '主节点'), ('slave', '从节点')], max_length=200, verbose_name='类型'),
        ),
    ]