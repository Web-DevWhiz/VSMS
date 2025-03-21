# Generated by Django 3.0.5 on 2025-03-11 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0008_auto_20201209_0917'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('present_status', models.CharField(max_length=10)),
                ('mechanic', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vehicle.Mechanic')),
            ],
        ),
    ]
