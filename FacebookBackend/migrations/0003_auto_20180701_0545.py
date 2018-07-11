# Generated by Django 2.0.6 on 2018-07-01 05:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FacebookBackend', '0002_auto_20180630_1240'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attachmentlinks',
            options={},
        ),
        migrations.AlterField(
            model_name='attachmentlinks',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FacebookBackend.Post'),
        ),
        migrations.AlterUniqueTogether(
            name='attachmentlinks',
            unique_together=set(),
        ),
    ]