FROM ubuntu

COPY . /

RUN set -o errexit -o nounset \
    && apt-get update && apt-get install -y \
    python3.8 \
    python3-pip \
    && pip3 install -r requirements.txt \
    && rm -rf /var/lib/apt/lists/*

CMD ["python3", "main.py"]