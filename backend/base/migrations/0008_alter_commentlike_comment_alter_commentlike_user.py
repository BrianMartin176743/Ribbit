# Generated by Django 4.0.1 on 2022-02-19 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_commentlike'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentlike',
            name='comment',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='commentlike',
            name='user',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]