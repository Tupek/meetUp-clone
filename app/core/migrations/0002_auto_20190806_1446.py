# Generated by Django 2.2.3 on 2019-08-06 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='interests',
            field=models.CharField(choices=[('Adventure', 'Adventure'), ('Food', 'Food'), ('Tech', 'Tech'), ('Family', 'Family'), ('Health', 'Health'), ('Sports', 'Sports'), ('Film', 'Film'), ('Books', 'Books'), ('Dance', 'Dance'), ('Arts', 'Arts')], max_length=9),
        ),
    ]
