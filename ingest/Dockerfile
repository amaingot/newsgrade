FROM python:2.7
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN apt-get update && apt-get install -y \
  python-dev \
  libxml2-dev libxslt-dev \
  libjpeg-dev zlib1g-dev libpng12-dev \
  curl \
  git
RUN pip install -r requirements.txt
RUN curl https://raw.githubusercontent.com/codelucas/newspaper/master/download_corpora.py | python
RUN git clone https://github.com/elelsee/aws-es-connection.git
RUN cd aws-es-connection && python setup.py install
RUN cd ..
COPY . /code/
RUN python ingest.py
#CMD ["python", "ingest.py"]
