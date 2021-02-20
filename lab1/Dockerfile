FROM ubuntu

RUN apt update && apt install -y \
    python3.8 \
    python3-pip \
    && pip3 install countryinfo \
    && mkdir -p /usr/src/app \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

COPY . /usr/src/app

CMD ["python3", "main.py"]