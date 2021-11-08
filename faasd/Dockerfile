FROM --platform=${TARGETPLATFORM:-linux/amd64} ghcr.io/openfaas/classic-watchdog:0.1.5 as watchdog
FROM python:3.9-slim-buster

COPY --from=watchdog /fwatchdog /usr/bin/fwatchdog
RUN chmod +x /usr/bin/fwatchdog


ARG TARGETPLATFORM
ARG BUILDPLATFORM

# Allows you to add additional packages via build-arg
ARG ADDITIONAL_PACKAGE

COPY --from=watchdog /fwatchdog /usr/bin/fwatchdog
RUN chmod +x /usr/bin/fwatchdog
RUN apt-get update \
    && apt-get install -y ca-certificates ${ADDITIONAL_PACKAGE} \
    && rm -rf /var/lib/apt/lists/

# Add non root user
RUN addgroup --system app && adduser app --system --ingroup app
RUN chown app /home/app

USER app

ENV PATH=$PATH:/home/app/.local/bin

WORKDIR /home/app/

COPY faasd/index.py           .
COPY faasd/requirements.txt   .

USER root
RUN pip install -r requirements.txt

# Build the function directory and install any user-specified components
USER app

RUN mkdir -p function
RUN touch ./function/__init__.py

WORKDIR /home/app/function/

COPY requirements.txt	.
RUN pip install --user -r requirements.txt

#install function code
USER root

COPY *.py   .
RUN chown -R app:app ../

WORKDIR /home/app/

#configure healthcheck
USER app

ENV fprocess="python index.py"
EXPOSE 8080

HEALTHCHECK --interval=3s CMD [ -e /tmp/.lock ] || exit 1

CMD ["fwatchdog"]
