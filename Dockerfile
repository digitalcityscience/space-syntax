# Builder-Worker based on https://github.com/p3palazzo/depthmapx-docker
FROM alpine:3.12 AS depthmapX-builder
WORKDIR /work
ARG version=0.8.0
ARG url="https://github.com/SpaceGroupUCL/depthmapX/archive/refs/heads/master.zip"
ARG tarball="v${version}.zip"

RUN apk --no-cache add \
  unzip \
  bash \
  binutils \
  clang \
  cmake \
  g++ \
  gcc \
  glu-dev \
  make \
  musl-dev \
  qt5-qtbase-dev \
  wget

RUN wget ${url} -O ${tarball} && \
  unzip ${tarball} -d depthmapX-${version}


RUN cd depthmapX-${version}/depthmapX-master && \
  mkdir build && \
  cd build && \
  cmake .. && \
  make -j depthmapXcli && \
  cp depthmapXcli/depthmapXcli /usr/local/bin/

FROM python:3.9

LABEL org.opencontainers.image.source https://github.com/digitalcityscience/space-syntax

RUN apt update

RUN useradd --create-home --shell /bin/bash app
WORKDIR /home/app
USER app

COPY requirements.txt /home/app
RUN pip install -r requirements.txt
COPY *.py /home/app/

RUN mkdir /home/app/downloads
COPY --from=depthmapX-builder \
  /usr/local/bin/depthmapXcli \
  /home/app/downloads/depthmapX

ENTRYPOINT [ "python","-m","main" ]