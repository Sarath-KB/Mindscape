# Generated by Django 4.2.1 on 2023-06-22 04:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0007_tbl_userregistration'),
        ('Admin', '0017_tbl_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_feedback',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Guest.tbl_userregistration'),
        ),
    ]
