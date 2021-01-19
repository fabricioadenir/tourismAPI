FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /tourismAPI
WORKDIR /tourismAPI
ADD requirements.txt /tourismAPI/
RUN pip install --upgrade pip && pip install -r requirements.txt
RUN pip install --upgrade djongo
ADD . /tourismAPI/
