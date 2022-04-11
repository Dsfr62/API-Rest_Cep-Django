# Generated by Django 4.0.1 on 2022-04-08 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='loc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cep', models.TextField(max_length=20)),
                ('endereco', models.TextField(max_length=100)),
                ('numero', models.TextField(max_length=10)),
                ('bairro', models.TextField(max_length=20)),
                ('data_criacao', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Loc',
            },
        ),
    ]
