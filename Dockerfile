FROM ubuntu:20.04

MAINTAINER Lauren Williams "laurenwilliamssoftwareeengineer@gmail.com"

ENV TZ=Europe/London

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update && apt-get install -y \
    python3-pip \
    libgl1-mesa-glx \
    libglib2.0-0

COPY ./requirements.txt /bot/requirements.txt

WORKDIR /bot

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /bot

ENTRYPOINT ["python3"]

CMD ["main.py"]
