# Generated by Django 4.1.1 on 2022-09-30 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0003_post_writer"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="writer",
        ),
    ]
