FROM python:3.6

ENV repoDir /var/www

RUN apt-get -y update && apt-get install -y \
    git

COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

RUN mkdir -p ${repoDir}

WORKDIR ${repoDir}

ARG CACHEBREAK=1

COPY / ${repoDir}/cookify
WORKDIR ${repoDir}/cookify



