# Generated by Django 2.2.4 on 2019-08-25 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mineral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('slug', models.TextField()),
                ('image_filename', models.TextField()),
                ('image_caption', models.TextField()),
                ('category', models.TextField()),
                ('formula', models.TextField()),
                ('strunz_classification', models.TextField()),
                ('unit_cell', models.TextField()),
                ('color', models.TextField()),
                ('crystal_habit', models.TextField()),
                ('mohs_scale_hardness', models.TextField()),
                ('crystal_system', models.TextField()),
                ('crystal_symmetry', models.TextField()),
                ('cleavage', models.TextField()),
                ('luster', models.TextField()),
                ('streak', models.TextField()),
                ('diaphaneity', models.TextField()),
                ('optical_properties', models.TextField()),
                ('refractive_index', models.TextField()),
                ('specific_gravity', models.TextField()),
                ('group', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
