# Generated by Django 5.1.2 on 2024-10-28 19:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OptionGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255)),
            ],
            options={
                'verbose_name': 'Option Group',
                'verbose_name_plural': 'Option Groups',
            },
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(allow_unicode=True, unique=True),
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('type', models.CharField(choices=[('text', 'Text'), ('integer', 'Integer'), ('float', 'Float'), ('option', 'Option'), ('multi_option', 'Multi Option')], default='text', max_length=255)),
                ('required', models.BooleanField(default=False)),
                ('option_group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='attributes', to='catalog.optiongroup')),
            ],
            options={
                'verbose_name': 'Option',
                'verbose_name_plural': 'Options',
            },
        ),
        migrations.CreateModel(
            name='OptionGroupValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='values', to='catalog.optiongroup')),
            ],
            options={
                'verbose_name': 'Option Group Value',
                'verbose_name_plural': 'Option Group Values',
            },
        ),
        migrations.CreateModel(
            name='ProductClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tiitle', models.CharField(db_index=True, max_length=255)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('slug', models.SlugField(allow_unicode=True, unique=True)),
                ('track_stock', models.BooleanField(default=True)),
                ('require_shipping', models.BooleanField(default=True)),
                ('options', models.ManyToManyField(to='catalog.option')),
            ],
            options={
                'verbose_name': 'Product Class',
                'verbose_name_plural': 'Product Classes',
            },
        ),
        migrations.CreateModel(
            name='ProductAttribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('type', models.CharField(choices=[('text', 'Text'), ('integer', 'Integer'), ('float', 'Float'), ('option', 'Option'), ('multi_option', 'Multi Option')], default='text', max_length=255)),
                ('required', models.BooleanField(default=False)),
                ('option_group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='options', to='catalog.optiongroup')),
                ('product_class', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attributes', to='catalog.productclass')),
            ],
            options={
                'verbose_name': 'Product Attribute',
                'verbose_name_plural': 'Product Attributes',
            },
        ),
    ]
