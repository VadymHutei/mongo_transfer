FROM python:3.11

RUN mkdir /data
WORKDIR /app

COPY requirements.txt /data
COPY main.py /app

RUN pip install -U pip
RUN pip install -r /data/requirements.txt
CMD ["python", "main.py"]

# docker build -t mongo_transfer_img .
# docker run -it --name mongo_transfer mongo_transfer_img /bin/bash
