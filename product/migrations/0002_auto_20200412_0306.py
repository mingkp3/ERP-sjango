# Generated by Django 2.2 on 2020-04-12 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=300, unique=True)),
            ],
        ),
        migrations.DeleteModel(
            name='AllProduct',
        ),
    ]
