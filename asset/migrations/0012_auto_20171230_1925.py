# Generated by Django 2.0 on 2017-12-30 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0011_auto_20171230_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='file',
            field=models.FileField(blank=True, default=None, null=True, upload_to='%Y%m%d70297', verbose_name='文件'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='id',
            field=models.IntegerField(db_column='FId', default=1000, primary_key=True, serialize=False),
        ),
    ]