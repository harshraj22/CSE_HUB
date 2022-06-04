FROM python:3.8-alpine

WORKDIR /usr/src/app

# To Get pillow work: https://stackoverflow.com/questions/57787424/django-docker-python-unable-to-install-pillow-on-python-alpine
RUN apk add --no-cache jpeg-dev zlib-dev
RUN apk add --no-cache --virtual .build-deps build-base linux-headers 

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./cse_hub .

EXPOSE 12345

CMD ["echo", "Hello World"]
CMD ["python3", "manage.py", "migrate" ,"--run-syncdb"]
CMD ["python3", "manage.py", "makemigrations"]
CMD ["python3", "manage.py", "migrate"]
# https://stackoverflow.com/questions/55831728/what-is-statreloader-while-running-django
CMD ["python3", "manage.py", "runserver", "0.0.0.0:12345", "--noreload"]