FROM ubuntu:22.04

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3  \
    python3-pip && \
    pip install requests

COPY main.py /app/main.py
WORKDIR /app

CMD ["python3", "main.py"]