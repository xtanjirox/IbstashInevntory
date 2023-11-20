from crispy_forms.helper import FormHelper
from django import forms
from apps.core import models


class CategoryForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['size'].widget.attrs['class'] = 'form-select multiple-remove choices__input'

    class Meta:
        model = models.Category
        fields = '__all__'
