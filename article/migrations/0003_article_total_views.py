# Generated by Django 4.1.2 on 2022-10-26 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_alter_article_author_alter_article_body_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='total_views',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
