# Generated by Django 3.0.8 on 2020-07-29 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trek',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Last_Name', models.CharField(max_length=100)),
                ('Adventure', models.CharField(max_length=100)),
                ('Trek_Date', models.DateField()),
                ('Email', models.CharField(max_length=120)),
                ('Mob_No', models.IntegerField()),
                ('country', models.CharField(max_length=100)),
                ('State', models.CharField(max_length=100)),
                ('Zip', models.IntegerField()),
                ('paymentMethod', models.CharField(max_length=100)),
                ('Book_Date', models.DateField()),
            ],
        ),
    ]
