FROM python:3.8

RUN apt-get update

WORKDIR /horta

COPY ./ .

RUN pip install -r requirements.txt

CMD ["python", "./app.py"]