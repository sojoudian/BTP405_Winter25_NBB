FROM python:3.12

WORKDIR /app

COPY app.py /app/

RUN pip install flask

EXPOSE 6000

CMD [ "python", "app.py" ]