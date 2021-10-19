# Builder-Worker based on https://github.com/p3palazzo/depthmapx-docker
FROM alpine:3.12 AS depthmapX-builder
WORKDIR /work
ARG version=0.8.0
ARG url="https://github.com/SpaceGroupUCL/depthmapX/archive/refs/tags/v${version}.tar.gz"
ARG tarball="v${version}.tar.gz"

RUN apk --no-cache add \
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

RUN wget ${url} && \
  tar -xzf ${tarball} && \
  cd depthmapX-${version} && \
  mkdir build && \
  cd build && \
  cmake .. && \
  make -j && \
  cp depthmapXcli/depthmapXcli /usr/local/bin/

FROM python:3.9

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