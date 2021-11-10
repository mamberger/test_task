# Generated by Django 3.2.9 on 2021-11-10 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('q_type', models.IntegerField(choices=[(1, 'Один вариант ответа'), (2, 'Несколько вариантов ответа')])),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('start_date', models.CharField(max_length=255)),
                ('end_date', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=1000)),
                ('is_active', models.BooleanField(default=0)),
                ('questions', models.ManyToManyField(to='questions.Questions')),
            ],
        ),
    ]