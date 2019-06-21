from django.test import TestCase
from Converter.models import Converter
from Converter.forms import ConverterForm
from django.urls import reverse


class ConverterTest(TestCase):
    def __init__(self, *args, **kwargs):
        super(ConverterTest, self).__init__(*args, **kwargs)
        self.converter = Converter()

    # model tests

    def test_convert(self):
        result_str = self.converter.convert('1234')
        self.assertEqual(True, isinstance(result_str, str))

        result_int = self.converter.convert('MCCXXXIV')
        self.assertEqual(True, isinstance(result_int, int))

    def test_roman_to_arabic(self):
        result_arabic = self.converter.roman_to_arabic('MCCXXXIV')
        self.assertEqual(result_arabic, 1234)

    def test_arabic_to_roman(self):
        result_roman = self.converter.arabic_to_roman(1234)
        self.assertEqual(result_roman, 'MCCXXXIV')

    # view tests

    def test_index_view(self):
        url = '/'
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_conversion_view(self):
        response = self.client.post(
            reverse('convert'),
            {'number': '1234'}
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['result'], 'MCCXXXIV')

    # form tests

    def test_valid_form(self):
        form = ConverterForm({'number': '1234'})
        self.assertTrue(form.is_valid())

        form = ConverterForm({'number': 'MCCXXXIV'})
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form = ConverterForm({'number': '0'})
        self.assertFalse(form.is_valid())

        form = ConverterForm({'number': '4000'})
        self.assertFalse(form.is_valid())

        form = ConverterForm({'number': '4qwe,&'})
        self.assertFalse(form.is_valid())

        form = ConverterForm({'number': 'XEX'})
        self.assertFalse(form.is_valid())

        form = ConverterForm({'number': 'MMMM'})
        self.assertFalse(form.is_valid())
