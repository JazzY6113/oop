import datetime
from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from .models import BookInstance

class RenewBookModelForm(ModelForm):
    def clean_due_back(self):
       data = self.cleaned_data['due_back']

       #Проверка того, что дата не в прошлом
       if data < datetime.date.today():
           raise ValidationError('Неверная дата – продление в прошлом.')

       #Check date is in range librarian allowed to change (+4 weeks)
       if data > datetime.date.today() + datetime.timedelta(weeks=4):
           raise ValidationError('Неверная дата – продление более чем на 4 недели вперед.')

       # Не забывайте всегда возвращать очищенные данные
       return data

    class Meta:
        model = BookInstance
        fields = ['due_back',]
        labels = { 'due_back': ('Дата продления'), }
        help_texts = { 'due_back': ('Введите дату между текущим моментом и 4 неделями (по умолчанию 3).'), }

