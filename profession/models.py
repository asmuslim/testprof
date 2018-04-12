from django.db import models


class Type(models.Model):
    name = models.CharField('Имя', max_length=32)

    def __str__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'


class Profession(models.Model):
    name = models.CharField('Имя', max_length=32)
    rate = models.ForeignKey('Rate', verbose_name='Коэффициенты', on_delete=models.CASCADE)
    type = models.ForeignKey('Type', verbose_name='Тип', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = 'Профессия'
        verbose_name_plural = 'Профессии'


class Rate(models.Model):
    attention = models.FloatField('Внимательность', blank=True, null=True)
    emotion = models.FloatField('Эмоциональная устойчивость', blank=True, null=True)
    generalchar = models.FloatField('Общие характеристики поведения', blank=True, null=True)
    charspeech = models.FloatField('Характеристика речи', blank=True, null=True)
    abstractmind = models.FloatField('Абстрактное мышление', blank=True, null=True)
    mind = models.FloatField('Память', blank=True, null=True)
    liability = models.FloatField('Ответственность', blank=True, null=True)
    speedmake = models.FloatField('Быстрота принятия решения', blank=True, null=True)
    physical = models.FloatField('Физическая выносливость', blank=True, null=True)

    def __str__(self):
        return '%s %s %s %s %s %s %s %s %s' % (self.attention, self.emotion, self.generalchar,
                                                  self.charspeech, self.abstractmind, self.mind,
                                                  self.liability, self.speedmake, self.physical)

    class Meta:
        verbose_name = 'Коэффициент'
        verbose_name_plural = 'Коэффициенты'


class RateType(models.Model):
    manNature = models.FloatField('Человек-природа', blank=True, null=True)
    manTechnician = models.FloatField('Человек-техника', blank=True, null=True)
    manMan = models.FloatField('Человек-человек', blank=True, null=True)
    manEngineeringSigns = models.FloatField('Человек-инжинерные знаки', blank=True, null=True)
    manArtisticImage = models.FloatField('Человек-художественый образ', blank=True, null=True)

    def __str__(self):
        return '%s %s %s %s %s' % (self. manNature, self.manTechnician, self.manMan,
                                                  self.manEngineeringSigns , self.manArtisticImage)

    class Meta:
        verbose_name = 'Коэффициент Типа'
        verbose_name_plural = 'Коэффициенты Типа'


class Question(models.Model):
    name = models.TextField('Содержание', blank=True, null=True)
    answer1 = models.ForeignKey('AnswerOne', verbose_name='Первый ответ', blank=True, null=True, max_length=225, on_delete=models.CASCADE)
    answer2 = models.ForeignKey('AnswerTwo', verbose_name='Второй ответ', blank=True, null=True, max_length=225, on_delete=models.CASCADE)
    answer3 = models.ForeignKey('AnswerThree', verbose_name='Третий ответ', blank=True, null=True, max_length=225, on_delete=models.CASCADE)
    answer4 = models.ForeignKey('AnswerFour', verbose_name='Четвертый ответ', blank=True, null=True, max_length=225, on_delete=models.CASCADE)
    answer5 = models.ForeignKey('AnswerFive', verbose_name='Пятый ответ', blank=True, null=True, max_length=225, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class QuestionType(models.Model):
    name = models.TextField('Содержание', blank=True, null=True)
    answer1 = models.ForeignKey('AnswerTypeOne', verbose_name='Первый ответ Типа', blank=True, null=True, max_length=225, on_delete=models.CASCADE)
    answer2 = models.ForeignKey('AnswerTypeTwo', verbose_name='Второй ответ Типа', blank=True, null=True, max_length=225, on_delete=models.CASCADE)
    answer3 = models.ForeignKey('AnswerTypeThree', verbose_name='Третий ответ Типа', blank=True, null=True, max_length=225, on_delete=models.CASCADE)
    answer4 = models.ForeignKey('AnswerTypeFour', verbose_name='Четвертый ответ Типа', blank=True, null=True, max_length=225, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = 'Вопрос Типа'
        verbose_name_plural = 'Вопросы Типа'


class AnswerOne(models.Model):
    name = models.CharField('Содержание', max_length=225)
    rate = models.ForeignKey('Rate', verbose_name='Коэффициент', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = 'Первый-Ответ'
        verbose_name_plural = 'Первые-Ответы'


class AnswerTwo(models.Model):
    name = models.CharField('Содержание', max_length=225)
    rate = models.ForeignKey('Rate', verbose_name='Коэффициент', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = 'Второй-Ответ'
        verbose_name_plural = 'Вторые-Ответы'


class AnswerThree(models.Model):
    name = models.CharField('Содержание', max_length=225)
    rate = models.ForeignKey('Rate', verbose_name='Коэффициент', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = 'Третий-Ответ'
        verbose_name_plural = 'Третьи-Ответы'


class AnswerFour(models.Model):
    name = models.CharField('Содержание', max_length=225)
    rate = models.ForeignKey('Rate', verbose_name='Коэффициент', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = 'Четвертый-Ответ'
        verbose_name_plural = 'Четвертые-Ответы'


class AnswerFive(models.Model):
    name = models.CharField('Содержание', max_length=225)
    rate = models.ForeignKey('Rate', verbose_name='Коэффициент', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = 'Пятый-Ответ'
        verbose_name_plural = 'Пятые-Ответы'


class AnswerTypeOne(models.Model):
    name = models.CharField('Содержание', max_length=225)
    rate = models.ForeignKey('RateType', verbose_name='Коэффициент', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = 'Первый-Ответ Типа'
        verbose_name_plural = 'Первые-Ответы Типа'


class AnswerTypeTwo(models.Model):
    name = models.CharField('Содержание', max_length=225)
    rate = models.ForeignKey('RateType', verbose_name='Коэффициент', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = 'Второй-Ответ Типа'
        verbose_name_plural = 'Вторые-Ответы Типа'


class AnswerTypeThree(models.Model):
    name = models.CharField('Содержание', max_length=225)
    rate = models.ForeignKey('RateType', verbose_name='Коэффициент', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = 'Третий-Ответ Типа'
        verbose_name_plural = 'Третьи-Ответы Типа'


class AnswerTypeFour(models.Model):
    name = models.CharField('Содержание', max_length=225)
    rate = models.ForeignKey('RateType', verbose_name='Коэффициент', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = 'Четвертый-Ответ Типа'
        verbose_name_plural = 'Четвертые-Ответы Типа'
