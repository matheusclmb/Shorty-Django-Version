# Generated by Django 4.0.4 on 2022-05-25 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shortener',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('shortcode', models.CharField(max_length=6, unique=True)),
                ('startDate', models.DateTimeField(auto_now_add=True)),
                ('lastSeenDate', models.DateTimeField(auto_now=True)),
                ('redirectCount', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ['-startDate'],
            },
        ),
    ]
