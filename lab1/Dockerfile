FROM ubuntu

RUN apt update && apt install -y python3.8 python3-pip
RUN pip3 install countryinfo

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

COPY . /usr/src/app

CMD ["python3", "main.py"]