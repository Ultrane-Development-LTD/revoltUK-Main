# Generated by Django 5.0.7 on 2024-09-22 12:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('revoltUK', '0003_remove_votingsession_duration_votingsession_end_time'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='votingsession',
            name='end_time',
            field=models.DateTimeField(),
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote_option', models.CharField(choices=[('yes', 'Yes'), ('no', 'No'), ('abstain', 'Abstain')], max_length=10)),
                ('voted_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('voting_session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='revoltUK.votingsession')),
            ],
            options={
                'unique_together': {('voting_session', 'user')},
            },
        ),
    ]
