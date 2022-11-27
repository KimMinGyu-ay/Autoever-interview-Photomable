# Generated by Django 3.2 on 2022-04-25 22:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import main.utils


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_gallery_s3_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_s3_url',
            field=models.CharField(default='https://photomarble.s3.ap-northeast-2.amazonaws.com/blank-profile.png', max_length=400),
        ),
        migrations.AlterField(
            model_name='collection',
            name='landmark',
            field=models.ForeignKey(db_column='landmark_id', on_delete=django.db.models.deletion.CASCADE, to='main.landmark'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='user',
            field=models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='gallery',
            field=models.ForeignKey(db_column='gallery_id', on_delete=django.db.models.deletion.CASCADE, to='main.gallery'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='landmark',
            field=models.ForeignKey(db_column='landmark_id', default='', on_delete=django.db.models.deletion.CASCADE, to='main.landmark'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='user',
            field=models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='like',
            name='gallery',
            field=models.ForeignKey(db_column='gallery_id', on_delete=django.db.models.deletion.CASCADE, to='main.gallery'),
        ),
        migrations.AlterField(
            model_name='like',
            name='user',
            field=models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='photoguide',
            name='landmark',
            field=models.ForeignKey(db_column='landmark_id', on_delete=django.db.models.deletion.CASCADE, to='main.landmark'),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_photo',
            field=models.ImageField(default='../static/main/images/balnk-profile.png', upload_to=main.utils.upload_image),
        ),
    ]
