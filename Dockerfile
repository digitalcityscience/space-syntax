# Builder-Worker based on https://github.com/p3palazzo/depthmapx-docker
FROM debian:bullseye-slim AS depthmapX-builder
WORKDIR /work
ARG version=0.8.0
ARG url="https://github.com/SpaceGroupUCL/depthmapX/archive/refs/heads/master.zip"
ARG tarball="v${version}.zip"

RUN apt update && apt install -y \
  unzip \
  bash \
  binutils \
  clang \
  cmake \
  g++ \
  gcc \
  make \
  musl-dev \
  qtbase5-dev \
  wget

RUN wget ${url} -O ${tarball} && \
  unzip ${tarball} -d depthmapX-${version}


RUN cd depthmapX-${version}/depthmapX-master && \
  mkdir build && \
  cd build && \
  cmake .. && \
  make -j2 depthmapXcli && \
  cp depthmapXcli/depthmapXcli /usr/local/bin/

FROM python:3.9-slim-bullseye

LABEL org.opencontainers.image.source https://github.com/digitalcityscience/space-syntax

RUN apt update

COPY --from=depthmapX-builder \
  /usr/local/bin/depthmapXcli \
  /usr/local/bin/depthmapXcli
RUN chmod +x /usr/local/bin/depthmapXcli

RUN useradd --create-home --shell /bin/bash app
WORKDIR /home/app
RUN chown -R app:app /home/app
USER app

COPY requirements.txt /home/app
RUN pip install -r requirements.txt
COPY *.py /home/app/


ENTRYPOINT [ "python","-m","main" ]