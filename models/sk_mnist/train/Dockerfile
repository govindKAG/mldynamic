FROM python:2

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential

COPY /requirements.txt /tmp/
RUN cd /tmp && \
    pip install --no-cache-dir -r requirements.txt

RUN mkdir training
COPY ./create_model.py /training/create_model.py
COPY ./pos_tweets.txt /training/pos_tweets.txt
COPY ./neg_tweets.txt /training/neg_tweets.txt
WORKDIR /training

CMD ["python -u /training/create_model.py"]

# TODO : optimize the size using the following resources
# https://hackernoon.com/tips-to-reduce-docker-image-sizes-876095da3b34
# https://www.fromlatest.io/#/
# https://blog.replicated.com/refactoring-a-dockerfile-for-image-size/
