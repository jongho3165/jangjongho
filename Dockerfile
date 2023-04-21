FROM python:3.6.8

WORKDIR .

COPY requirements.txt ./
COPY ./djconfig ./djconfig

RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt
RUN pip3 install django-summernote
CMD [ "python3", "djconfig/manage.py", "runserver", "0.0.0.0:8000" ]
