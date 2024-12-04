import datetime
from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from .models import BookInstance
from .models import Author
from datetime import date, timedelta

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

class AuthorForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']

    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data.get('date_of_birth')
        if date_of_birth and date_of_birth > date.today() - timedelta(days=18*365):
            raise forms.ValidationError('Автор должен быть старше 18 лет.')
        return date_of_birth

    def clean_date_of_death(self):
        date_of_death = self.cleaned_data.get('date_of_death')
        if date_of_death and date_of_death >= date.today():
            raise forms.ValidationError('Дата смерти не может быть сегодняшней или в будущем.')
        return date_of_death