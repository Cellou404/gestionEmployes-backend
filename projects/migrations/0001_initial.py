# Generated by Django 4.1.7 on 2023-03-10 20:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('complete', models.BooleanField(default=False, verbose_name='complete')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='ProjectTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=200, verbose_name='task name')),
                ('description', models.TextField(help_text='500 characters allowed', max_length=500, verbose_name='description')),
                ('complete', models.BooleanField(default=False, verbose_name='complete')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
            ],
            options={
                'verbose_name': 'Project Task',
                'verbose_name_plural': 'Project Tasks',
                'ordering': ['created'],
            },
        ),
    ]