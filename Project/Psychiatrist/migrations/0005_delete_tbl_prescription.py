# Generated by Django 4.2.3 on 2023-07-10 04:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Psychiatrist', '0004_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='tbl_prescription',
        ),
    ]