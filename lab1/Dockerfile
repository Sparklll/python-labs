FROM ubuntu

COPY . /

RUN apt update && apt install -y \
    python3.8 \
    python3-pip \
    && pip3 install -r requirments.txt \
    && rm -rf /var/lib/apt/lists/*

CMD ["python3", "main.py"]