# Generated by Django 4.2.1 on 2023-05-08 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kaznacheistvo_site', '0005_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='questionsObject',
        ),
        migrations.AlterField(
            model_name='answer',
            name='answer',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='questions',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='AllAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('child', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='qwertyy', to='kaznacheistvo_site.answer')),
                ('parrent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='qwerty', to='kaznacheistvo_site.answer')),
            ],
        ),
    ]
