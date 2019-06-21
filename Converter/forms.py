import re
from django import forms
from django.core.exceptions import ValidationError
from Converter.models import Converter


class ConverterForm(forms.ModelForm):
    class Meta:
        model = Converter
        fields = ['number', 'result']
        widgets = {
            'number': forms.TextInput(attrs={'placeholder': 'Number'}),
            'result': forms.TextInput(attrs={'placeholder': 'Result', 'readonly': 'True'})
        }

    def clean_number(self):
        number = self.cleaned_data['number']

        invalid_input = (
            'IIII', 'VV', 'XXXX', 'LL', 'CCCC', 'DD',
            'MMMM', 'IM', 'VM', 'XM', 'LM', 'DM', 'ID', 'VD',
            'XD', 'LD', 'IC', 'VC', 'LC', 'IL', 'VL', 'VX'
        )

        if number.isdigit():
            if int(number) == 0:
                raise ValidationError("There is no zero in Roman numerals")
            elif int(number) > 3999:
                raise ValidationError("Number should be less than 3999")
        elif bool(re.match("^(?=.*[a-zA-Zа-яА-Я])(?=.*[0-9])|(?=.*\W)", number)):
            raise ValidationError("Type either arabic or roman number in field")
        elif number.isalpha():
            if any(i not in ['M', 'D', 'C', 'L', 'X', 'V', 'I'] for i in number.upper()) or \
                    any(i in number.upper() for i in invalid_input):
                    raise ValidationError("Input is not a valid roman numeral")

        return number


