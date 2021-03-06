# Generated by Django 2.2.1 on 2020-02-07 14:13

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('DiabeticRetinopathy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('name', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255, unique=True)),
                ('user_id', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('staff', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
