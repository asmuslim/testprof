from django.contrib import admin
from .models import (Type, Profession, Rate, Question,
                     AnswerOne, AnswerTwo, AnswerThree, AnswerFour, AnswerFive,
                     QuestionType, RateType,
                     AnswerTypeOne,AnswerTypeTwo,AnswerTypeThree,AnswerTypeFour)


class TypeAdmin(admin.ModelAdmin):
    #list_display = ['name', 'email']
    list_display = [field.name for field in Type._meta.fields]

    #inlines = [FieldMappingInline]
    #fields = ['email']
    #exclude = ["email"]
    list_filter = ['name',]
    search_fields = ['name',]

    class Meta:
        model = Type


admin.site.register(Type, TypeAdmin)


class ProfessionAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Profession._meta.fields]

    list_filter = ['name',]
    search_fields = ['name',]

    class Meta:
        model = Profession


admin.site.register(Profession, ProfessionAdmin)


class RateAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Rate._meta.fields]

    list_filter = ['id',]
    search_fields = ['id',]

    class Meta:
        model = Rate


class RateTypeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in RateType._meta.fields]

    list_filter = ['id',]
    search_fields = ['id',]

    class Meta:
        model = RateType

admin.site.register(RateType, RateTypeAdmin)


class QuestionAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Question._meta.fields]

    list_filter = ['name',]
    search_fields = ['name',]

    class Meta:
        model = Question


admin.site.register(Question, QuestionAdmin)


class QuestionTypeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in QuestionType._meta.fields]

    list_filter = ['name',]
    search_fields = ['name',]

    class Meta:
        model = QuestionType


admin.site.register(QuestionType, QuestionTypeAdmin)


class AnswerOneAdmin(admin.ModelAdmin):
    list_display = [field.name for field in AnswerOne._meta.fields]

    list_filter = ['name',]
    search_fields = ['name',]

    class Meta:
        model = AnswerOne


admin.site.register(AnswerOne, AnswerOneAdmin)


class AnswerTwoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in AnswerTwo._meta.fields]

    list_filter = ['name',]
    search_fields = ['name',]

    class Meta:
        model = AnswerTwo


admin.site.register(AnswerTwo, AnswerTwoAdmin)


class AnswerThreeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in AnswerThree._meta.fields]

    list_filter = ['name',]
    search_fields = ['name',]

    class Meta:
        model = AnswerThree


admin.site.register(AnswerThree, AnswerThreeAdmin)


class AnswerFourAdmin(admin.ModelAdmin):
    list_display = [field.name for field in AnswerFour._meta.fields]

    list_filter = ['name',]
    search_fields = ['name',]

    class Meta:
        model = AnswerFour


admin.site.register(AnswerFour, AnswerFourAdmin)


class AnswerFiveAdmin(admin.ModelAdmin):
    list_display = [field.name for field in AnswerFive._meta.fields]

    list_filter = ['name',]
    search_fields = ['name',]

    class Meta:
        model = AnswerFive


admin.site.register(AnswerFive, AnswerFiveAdmin)


class AnswerTypeOneAdmin(admin.ModelAdmin):
    list_display = [field.name for field in AnswerTypeOne._meta.fields]

    list_filter = ['name',]
    search_fields = ['name',]

    class Meta:
        model = AnswerTypeOne


admin.site.register(AnswerTypeOne, AnswerTypeOneAdmin)


class AnswerTypeTwoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in AnswerTypeTwo._meta.fields]

    list_filter = ['name',]
    search_fields = ['name',]

    class Meta:
        model = AnswerTypeTwo


admin.site.register(AnswerTypeTwo, AnswerTypeTwoAdmin)


class AnswerTypeThreeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in AnswerTypeThree._meta.fields]

    list_filter = ['name',]
    search_fields = ['name',]

    class Meta:
        model = AnswerTypeThree


admin.site.register(AnswerTypeThree, AnswerTypeThreeAdmin)


class AnswerTypeFourAdmin(admin.ModelAdmin):
    list_display = [field.name for field in AnswerTypeFour._meta.fields]

    list_filter = ['name',]
    search_fields = ['name',]

    class Meta:
        model = AnswerTypeFour


admin.site.register(AnswerTypeFour, AnswerTypeFourAdmin)