FROM python:3.9

RUN apt update

RUN useradd --create-home --shell /bin/bash app
WORKDIR /home/app
USER app

COPY requirements.txt /home/app
RUN pip install -r requirements.txt
COPY *.py /home/app/

RUN mkdir /home/app/downloads

ENTRYPOINT [ "python","-m","main" ]