from .models import (Type, Profession, Rate, Question,
                     AnswerOne, AnswerTwo, AnswerThree, AnswerFour, AnswerFive,
                     QuestionType, RateType,
                     AnswerTypeOne,AnswerTypeTwo,AnswerTypeThree,AnswerTypeFour)

from rest_framework import serializers


class TypeSerializers(serializers.ModelSerializer):

    class Meta:
        model = Type
        fields = ('id', 'name',)


class ProfessionSerializers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Profession
        fields = ('name', 'rate', 'type',)


class RateSerializers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Rate
        fields = ('url', 'attention', 'emotion', 'generalchar', 'charspeech', 'abstractmind', 'mind', 'liability', 'speedmake', 'physical',)


class QuestionSerializers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Question
        fields = ('name', 'answer1', 'answer2', 'answer3', 'answer4', 'answer5',)


class Answer1Serializers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = AnswerOne
        fields = ('name', 'rate',)


class Answer2Serializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AnswerTwo
        fields = ('name', 'rate',)


class Answer3Serializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AnswerThree
        fields = ('name', 'rate',)


class Answer4Serializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AnswerFour
        fields = ('name', 'rate',)


class Answer5Serializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AnswerFive
        fields = ('name', 'rate',)

