from django import forms
from .models import Day

'''
forms.ModelFormとすることでmodels.pyに記した属性の入力フォームを自動的に作成してくれる。
MetaClassの中に該当するmodelとfieldsを書く（特定の属性の場合はtappleで書く
'''
class DayCreateForm(forms.ModelForm):
    class Meta:
        model = Day
        fields = '__all__'