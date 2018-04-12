# Generated by Django 2.0.3 on 2018-04-06 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profession', '0007_auto_20180405_2115'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerTypeFour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225, verbose_name='Содержание')),
            ],
            options={
                'verbose_name_plural': 'Четвертые-Ответы',
                'verbose_name': 'Четвертый-Ответ',
            },
        ),
        migrations.CreateModel(
            name='AnswerTypeOne',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225, verbose_name='Содержание')),
            ],
            options={
                'verbose_name_plural': 'Первые-Ответы',
                'verbose_name': 'Первый-Ответ',
            },
        ),
        migrations.CreateModel(
            name='AnswerTypeThree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225, verbose_name='Содержание')),
            ],
            options={
                'verbose_name_plural': 'Третьи-Ответы',
                'verbose_name': 'Третий-Ответ',
            },
        ),
        migrations.CreateModel(
            name='AnswerTypeTwo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225, verbose_name='Содержание')),
            ],
            options={
                'verbose_name_plural': 'Вторые-Ответы',
                'verbose_name': 'Второй-Ответ',
            },
        ),
        migrations.CreateModel(
            name='QuestionType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True, verbose_name='Содержание')),
                ('answer1', models.ForeignKey(blank=True, max_length=225, null=True, on_delete=django.db.models.deletion.CASCADE, to='profession.AnswerOne', verbose_name='Первый ответ')),
                ('answer2', models.ForeignKey(blank=True, max_length=225, null=True, on_delete=django.db.models.deletion.CASCADE, to='profession.AnswerTwo', verbose_name='Второй ответ')),
                ('answer3', models.ForeignKey(blank=True, max_length=225, null=True, on_delete=django.db.models.deletion.CASCADE, to='profession.AnswerThree', verbose_name='Третий ответ')),
                ('answer4', models.ForeignKey(blank=True, max_length=225, null=True, on_delete=django.db.models.deletion.CASCADE, to='profession.AnswerFour', verbose_name='Четвертый ответ')),
                ('answer5', models.ForeignKey(blank=True, max_length=225, null=True, on_delete=django.db.models.deletion.CASCADE, to='profession.AnswerFive', verbose_name='Пятый ответ')),
            ],
            options={
                'verbose_name_plural': 'Вопросы Типа',
                'verbose_name': 'Вопрос Типа',
            },
        ),
        migrations.CreateModel(
            name='RateType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manNature', models.FloatField(blank=True, null=True, verbose_name='Человек-природа')),
                ('manTechnician', models.FloatField(blank=True, null=True, verbose_name='Человек-техника')),
                ('manMan', models.FloatField(blank=True, null=True, verbose_name='Человек-человек')),
                ('manEngineeringSigns', models.FloatField(blank=True, null=True, verbose_name='Человек-инжинерные знаки')),
                ('manArtisticImage', models.FloatField(blank=True, null=True, verbose_name='Человек-художественый образ')),
            ],
            options={
                'verbose_name_plural': 'Коэффициенты Типа',
                'verbose_name': 'Коэффициент Типа',
            },
        ),
        migrations.AddField(
            model_name='answertypetwo',
            name='rate',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profession.RateType', verbose_name='Коэффициент'),
        ),
        migrations.AddField(
            model_name='answertypethree',
            name='rate',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profession.RateType', verbose_name='Коэффициент'),
        ),
        migrations.AddField(
            model_name='answertypeone',
            name='rate',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profession.RateType', verbose_name='Коэффициент'),
        ),
        migrations.AddField(
            model_name='answertypefour',
            name='rate',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profession.RateType', verbose_name='Коэффициент'),
        ),
    ]