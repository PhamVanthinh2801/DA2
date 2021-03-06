# Generated by Django 3.1.2 on 2021-05-08 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Contents', '0011_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choosesizecolor',
            name='producColor',
            field=models.CharField(choices=[('Purple', 'Purple'), ('Red', 'Red'), ('Blue', 'Blue')], max_length=255),
        ),
        migrations.AlterField(
            model_name='choosesizecolor',
            name='producsize',
            field=models.CharField(choices=[('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large')], max_length=255),
        ),
        migrations.AlterField(
            model_name='order',
            name='choosesizecolor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='choosesizecolor', to='Contents.choosesizecolor'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='producsize',
            field=models.CharField(choices=[('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large')], max_length=255),
        ),
    ]
