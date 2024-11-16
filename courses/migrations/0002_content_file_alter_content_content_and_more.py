# Generated by Django 5.1.2 on 2024-11-04 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='assignments/'),
        ),
        migrations.AlterField(
            model_name='content',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='content',
            name='content_type',
            field=models.CharField(choices=[('video', 'Video'), ('file', 'File'), ('image', 'Image'), ('text', 'Text'), ('assignment', 'Assignment')], max_length=50),
        ),
    ]