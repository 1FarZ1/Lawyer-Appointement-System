FROM python:3.9-alpine

WORKDIR /app

COPY . /app

RUN pip3 install -r requirements.txt

# COPY . .

# CMD ["python3", "app.py"]