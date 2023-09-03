# Generated by Django 3.1.3 on 2023-09-02 23:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(default='Choice', max_length=100)),
                ('is_correct', models.BooleanField(default=False)),
                ('question_id', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chocies', models.ManyToManyField(to='onlinecourse.Choice')),
                ('enrollment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecourse.enrollment')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(default='Question?', max_length=300)),
                ('grade', models.FloatField(default=0.0)),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecourse.lesson')),
            ],
        ),
    ]
