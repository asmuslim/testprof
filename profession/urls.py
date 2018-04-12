from django.contrib import admin
from django.urls import path, include

from .views import (ViewSetType, ViewSetRate, ViewSetProfession, ViewSetQuestion,
                    ViewSetAnswerOne, ViewSetAnswerTwo, ViewSetAnswerThree, ViewSetAnswerFour,
                    ViewSetAnswerFive, home)

from rest_framework import routers

router1 = routers.SimpleRouter()
router1.register('type', ViewSetType)

router2 = routers.SimpleRouter()
router2.register('rate', ViewSetRate)

router3 = routers.SimpleRouter()
router3.register('question', ViewSetQuestion)

router4 = routers.SimpleRouter()
router4.register('profession', ViewSetProfession)

router5 = routers.SimpleRouter()
router5.register('answer1', ViewSetAnswerOne)

router6 = routers.SimpleRouter()
router6.register('answer2', ViewSetAnswerTwo)

router7 = routers.SimpleRouter()
router7.register('answer3', ViewSetAnswerThree)

router8 = routers.SimpleRouter()
router8.register('answer4', ViewSetAnswerFour)

router9 = routers.SimpleRouter()
router9.register('answer5', ViewSetAnswerFive)

urlpatterns = [
    path('', home, name='home')
]

urlpatterns += router1.urls
urlpatterns += router2.urls
urlpatterns += router3.urls
urlpatterns += router4.urls
urlpatterns += router5.urls
urlpatterns += router6.urls
urlpatterns += router7.urls
urlpatterns += router8.urls
urlpatterns += router9.urls
