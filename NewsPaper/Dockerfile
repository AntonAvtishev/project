FROM python:3.9

RUN mkdir /app

COPY requirements.txt /app

RUN pip3 install -r /app/requirements.txt --no-cache-dir

COPY ./ /app

WORKDIR /app

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
