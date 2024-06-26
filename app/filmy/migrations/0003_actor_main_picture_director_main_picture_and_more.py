# Generated by Django 5.0.6 on 2024-05-17 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmy', '0002_actor_director_genre_remove_movie_title_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='main_picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='director',
            name='main_picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='movie',
            name='main_picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
