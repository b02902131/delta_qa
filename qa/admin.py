from django.contrib import admin
from django import forms

# Register your models here.
from .models import CQA

class CQAForm(forms.ModelForm):
    # context_text = forms.CharField( widget=forms.Textarea )
    # question_text = forms.CharField( widget=forms.Textarea )
    class Meta:
        model = CQA
        widgets = {
          'context_text': forms.Textarea(attrs={'rows':10, 'cols':100}),
          'question_text': forms.Textarea(attrs={'rows':4, 'cols':100}),
        }
        fields = '__all__'

class CQAAdmin(admin.ModelAdmin):
    form = CQAForm
    list_display = ('question_text', 'answer_text', 'pub_date', 'valid')


admin.site.register(CQA, CQAAdmin)
