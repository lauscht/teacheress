FROM python:3.8-slim

# set working directory
WORKDIR /app/

# Copy local sources
COPY . .

# set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install -r requirements.txt
RUN python setup.py develop
