from django.shortcuts import render

from .models import (Type, Profession, Rate, Question,
                     AnswerOne, AnswerTwo, AnswerThree, AnswerFour, AnswerFive,
                     QuestionType, RateType,
                     AnswerTypeOne,AnswerTypeTwo,AnswerTypeThree,AnswerTypeFour)

from .serializers import (TypeSerializers, ProfessionSerializers, RateSerializers, QuestionSerializers,
                          Answer1Serializers, Answer2Serializers, Answer3Serializers, Answer4Serializers,
                          Answer5Serializers,)

from rest_framework import viewsets
from rest_framework import permissions


def home(request):
    start = 0
    end = 0
    return render(request, 'profession/home.html', locals())


class ViewSetType(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializers
    permission_classes = (permissions.AllowAny,)


class ViewSetProfession(viewsets.ModelViewSet):
    queryset = Profession.objects.all()
    serializer_class = ProfessionSerializers
    permission_classes = (permissions.AllowAny,)


class ViewSetRate(viewsets.ModelViewSet):
    queryset = Rate.objects.all()
    serializer_class = RateSerializers
    permissions_classes = (permissions.AllowAny,)


class ViewSetQuestion(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializers
    permission_classes = (permissions.AllowAny,)


class ViewSetAnswerOne(viewsets.ModelViewSet):
    queryset = AnswerOne.objects.all()
    serializer_class = Answer1Serializers
    permission_classes = (permissions.AllowAny,)


class ViewSetAnswerTwo(viewsets.ModelViewSet):
    queryset = AnswerTwo.objects.all()
    serializer_class = Answer2Serializers
    permission_classes = (permissions.AllowAny,)


class ViewSetAnswerThree(viewsets.ModelViewSet):
    queryset = AnswerThree.objects.all()
    serializer_class = Answer3Serializers
    permission_classes = (permissions.AllowAny,)


class ViewSetAnswerFour(viewsets.ModelViewSet):
    queryset = AnswerFour.objects.all()
    serializer_class = Answer4Serializers
    permission_classes = (permissions.AllowAny,)


class ViewSetAnswerFive(viewsets.ModelViewSet):
    queryset = AnswerFive.objects.all()
    serializer_class = Answer5Serializers
    permission_classes = (permissions.AllowAny,)


