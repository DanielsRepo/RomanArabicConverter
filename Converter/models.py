from django.db import models


class UserInfo(models.Model):
    browser = models.CharField(max_length=50)
    os = models.CharField(max_length=50)
    device = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()


class Converter(models.Model):
    number = models.CharField(max_length=10)
    result = models.CharField(max_length=10, blank=True)
    user_info = models.ManyToManyField(UserInfo)

    def convert(self, number):
        if number.isdigit():
            return self.arabic_to_roman(int(number))
        else:
            return self.roman_to_arabic(number.upper())

    def roman_to_arabic(self, number):
        roman_system = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

        result = 0

        for i in range(len(number)):
            num = roman_system[number[i]]

            if i + 1 < len(number) and roman_system[number[i + 1]] > num:
                result -= num
            else:
                result += num

        return result

    def arabic_to_roman(self, number):
        arabics = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
        romans = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')

        result = ''

        for i in range(len(arabics)):
            count = int(number / arabics[i])
            result += romans[i] * count
            number -= arabics[i] * count

        return result





