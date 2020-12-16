FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /sbturAPI
WORKDIR /sbturAPI
ADD requirements.txt /sbturAPI/
RUN pip install --upgrade pip && pip install -r requirements.txt
RUN pip install --upgrade djongo
ADD . /sbturAPI/
