# Generated by Django 5.1.1 on 2024-10-24 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pecas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peca',
            name='codigo_barras',
            field=models.CharField(max_length=255),
        ),
    ]