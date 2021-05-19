# Generated by Django 2.0.1 on 2018-01-18 18:07

from django.db import migrations


def create_subjects(apps, schema_editor):
    Subject = apps.get_model('classroom', 'Subject')
    Subject.objects.create(name='Arson', color='#343a40')
    Subject.objects.create(name='Offensive Behavior', color='#007bff')
    Subject.objects.create(name='Murder', color='#28a745')
    Subject.objects.create(name='Theft', color='#17a2b8')
    Subject.objects.create(name='Fraud', color='#ffc107')


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_subjects),
    ]
