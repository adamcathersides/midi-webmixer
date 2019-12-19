FROM python:3.7.4-buster

COPY . /midi-webmixer/
RUN apt update && apt install -y liblo-dev librtmidi-dev
RUN pip install /midi-webmixer/

ENTRYPOINT ["webmixer"]
CMD ["/config.ini"]
