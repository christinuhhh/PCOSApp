# Generated by Django 5.1.1 on 2024-11-30 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pcosapp', '0003_remove_recipe_author_name_remove_recipe_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='recipe_instructions',
        ),
        migrations.AlterField(
            model_name='recipe',
            name='keywords',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
    ]