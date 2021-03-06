# Generated by Django 2.0.3 on 2018-04-05 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profession', '0006_auto_20180405_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='abstractmind',
            field=models.FloatField(blank=True, null=True, verbose_name='Абстрактное мышление'),
        ),
        migrations.AlterField(
            model_name='rate',
            name='attention',
            field=models.FloatField(blank=True, null=True, verbose_name='Внимательность'),
        ),
        migrations.AlterField(
            model_name='rate',
            name='charspeech',
            field=models.FloatField(blank=True, null=True, verbose_name='Характеристика речи'),
        ),
        migrations.AlterField(
            model_name='rate',
            name='emotion',
            field=models.FloatField(blank=True, null=True, verbose_name='Эмоциональная устойчивость'),
        ),
        migrations.AlterField(
            model_name='rate',
            name='generalchar',
            field=models.FloatField(blank=True, null=True, verbose_name='Общие характеристики поведения'),
        ),
        migrations.AlterField(
            model_name='rate',
            name='liability',
            field=models.FloatField(blank=True, null=True, verbose_name='Ответственность'),
        ),
        migrations.AlterField(
            model_name='rate',
            name='mind',
            field=models.FloatField(blank=True, null=True, verbose_name='Память'),
        ),
        migrations.AlterField(
            model_name='rate',
            name='physical',
            field=models.FloatField(blank=True, null=True, verbose_name='Физическая выносливость'),
        ),
        migrations.AlterField(
            model_name='rate',
            name='speedmake',
            field=models.FloatField(blank=True, null=True, verbose_name='Быстрота принятия решения'),
        ),
    ]
