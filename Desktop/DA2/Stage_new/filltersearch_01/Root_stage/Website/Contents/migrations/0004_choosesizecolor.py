# Generated by Django 3.1.2 on 2021-04-29 09:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Contents', '0003_auto_20210428_2059'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChooseSizeColor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producsize', models.CharField(choices=[('Small', 'S'), ('Medium', 'M'), ('Large', 'L')], max_length=255)),
                ('producColor', models.CharField(choices=[('Purple', 'P'), ('Red', 'R'), ('Blue', 'B')], max_length=255)),
                ('status', models.BooleanField(default=False)),
                ('Product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Contents.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]