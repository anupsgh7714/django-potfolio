# Generated by Django 3.2.8 on 2021-11-11 08:10

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_alter_projects_project_title_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='project_title_slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='project_title', unique=True),
        ),
    ]
