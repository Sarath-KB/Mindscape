# Generated by Django 4.2 on 2023-05-04 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0006_tbl_hospitaltype'),
        ('Guest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_newhospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=50)),
                ('logo', models.FileField(upload_to='HospitalLogo/')),
                ('proof', models.FileField(upload_to='HospitalLogo/')),
                ('password', models.CharField(max_length=100)),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_place')),
            ],
        ),
    ]