# Generated by Django 4.2.1 on 2023-06-08 07:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0015_tbl_feedback'),
        ('Guest', '0004_tbl_newhospital'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_unknownemergency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=5000)),
                ('major', models.CharField(max_length=50)),
                ('status', models.IntegerField(default=0)),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_place')),
            ],
        ),
    ]
