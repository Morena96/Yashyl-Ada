# Generated by Django 3.1.5 on 2021-01-23 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('company', models.CharField(blank=True, max_length=250, null=True)),
                ('phone', models.CharField(max_length=50)),
                ('text', models.TextField(max_length=500)),
            ],
            options={
                'verbose_name': 'Contact us mail',
                'verbose_name_plural': 'Contact us mails',
            },
        ),
    ]
