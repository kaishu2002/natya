# Generated by Django 5.0.7 on 2024-09-11 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dhruvam', '0007_alter_danceclass_guru'),
    ]

    operations = [
        migrations.AlterField(
            model_name='danceclass',
            name='video_link',
            field=models.FileField(upload_to='videos/'),
        ),
    ]
