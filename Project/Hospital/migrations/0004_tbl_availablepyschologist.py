# Generated by Django 4.2 on 2023-05-09 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital', '0003_tbl_availablepyschiatrist'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_availablepyschologist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('from_time', models.CharField(max_length=50)),
                ('to_time', models.CharField(max_length=50)),
                ('psychiatrist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hospital.tbl_pyschologist')),
            ],
        ),
    ]