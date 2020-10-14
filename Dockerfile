FROM python:3

RUN apt-get update && apt-get install -y \
    # for compilemessages
    gettext \
    libgettextpo-dev \
    # python3-saml
    libxml2-dev \
    libxmlsec1-dev

ADD requirements.txt /tmp/requirements.txt

RUN pip install --upgrade pip && pip install -r /tmp/requirements.txt --no-cache-dir

ADD . /code

WORKDIR /code