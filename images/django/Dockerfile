FROM python:3.10

RUN apt-get update && apt-get install -y \
		postgresql \
		systemctl \
		postgresql-contrib \
		postgresql-client
RUN rm -rf /var/lib/apt/lists/*

COPY requirements.txt requirements.txt
COPY . code
WORKDIR /code

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
