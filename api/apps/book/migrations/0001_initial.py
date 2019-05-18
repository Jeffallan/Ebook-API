# Generated by Django 2.2.1 on 2019-05-14 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('subtitle', models.CharField(max_length=500)),
                ('image_url', models.URLField(max_length=500)),
                ('isbin', models.CharField(max_length=20)),
                ('year', models.PositiveSmallIntegerField()),
                ('language', models.CharField(max_length=50)),
                ('file_size', models.CharField(max_length=50)),
                ('file_format', models.CharField(max_length=10)),
                ('description', models.TextField()),
                ('download_link', models.URLField(max_length=500)),
                ('author', models.ManyToManyField(to='author.Author')),
                ('category', models.ManyToManyField(to='category.Category')),
            ],
        ),
    ]
