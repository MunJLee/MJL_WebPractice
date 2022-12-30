FROM python:3.6.12-alpine
WORKDIR /app
COPY requirements.txt /app
RUN pip3 install -r requirements.txt
COPY ./src /app
EXPOSE 5000
CMD ["python3", "/app/restapp.py"]
