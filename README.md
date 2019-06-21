git clone https://github.com/DanielsRepo/RomanArabicConverter.git

project\Scripts\activate

Rename "env.example" file to ".env" and type to this file SECRET_KEY

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver

To run tests:
coverage run manage.py test Converter -v 2
