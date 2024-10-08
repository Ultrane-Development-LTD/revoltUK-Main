# Generated by Django 5.0.7 on 2024-09-21 15:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('revoltUK', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='legislation',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='revoltUK.category'),
        ),
    ]
