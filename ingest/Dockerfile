FROM python:3-alpine
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN apt-get update && apt-get install -y \
  python3-dev \
  libxml2-dev libxslt-dev \
  libjpeg-dev zlib1g-dev libpng12-dev \
  curl \
  git
RUN pip3 install -r requirements.txt
RUN curl https://raw.githubusercontent.com/codelucas/newspaper/master/download_corpora.py | python
RUN git clone https://github.com/elelsee/aws-es-connection.git
RUN cd aws-es-connection && python3 setup.py install
RUN cd ..
COPY . /code/
CMD ["python3", "ingest.py"]
