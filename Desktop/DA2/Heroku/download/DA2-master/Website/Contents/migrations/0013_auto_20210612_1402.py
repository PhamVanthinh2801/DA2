# Generated by Django 3.1.2 on 2021-06-12 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contents', '0012_auto_20210508_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('SB', 'GIÀY NAM'), ('SG', 'GIÀY NỮ'), ('SK', 'GIÀY TRẺ EM')], max_length=255),
        ),
    ]