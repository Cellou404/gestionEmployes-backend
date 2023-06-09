# Generated by Django 4.1.7 on 2023-03-10 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_remove_employee_designation_employee_bio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='description',
        ),
        migrations.AddField(
            model_name='employee',
            name='address',
            field=models.CharField(blank=True, max_length=150, verbose_name='address'),
        ),
        migrations.AddField(
            model_name='employee',
            name='designation',
            field=models.CharField(default=1, max_length=150, verbose_name='designation'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='avatars/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='bio',
            field=models.TextField(blank=True, help_text='500 characters allowed', max_length=500, verbose_name='bio'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.CharField(max_length=150, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(max_length=150, verbose_name='name'),
        ),
    ]
