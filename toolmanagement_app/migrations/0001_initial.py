# Generated by Django 5.1 on 2024-08-26 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('sl_no', models.AutoField(primary_key=True, serialize=False)),
                ('project_name', models.CharField(max_length=255)),
                ('project_type', models.CharField(max_length=255)),
                ('vertical', models.CharField(max_length=255)),
                ('platform', models.CharField(max_length=255)),
                ('developer', models.CharField(max_length=255)),
                ('tool_name', models.CharField(max_length=255)),
                ('command', models.TextField()),
                ('technology', models.CharField(max_length=255)),
                ('tool_description', models.TextField()),
                ('year_of_creation', models.CharField(max_length=255)),
                ('repository_path', models.CharField(max_length=1024)),
            ],
        ),
    ]
