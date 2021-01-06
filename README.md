git clone https://github.com/DanielsRepo/RomanArabicConverter.git

cd RomanArabicConverter

docker-compose build

docker-compose up

To run tests:
coverage run manage.py test Converter -v 2
