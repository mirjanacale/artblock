# Generated by Django 4.2.16 on 2024-11-21 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('block', '0006_remove_post_posts_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('draft', 'Draft')], default='active', max_length=10),
        ),
    ]