FROM python:3.7.4-buster

COPY . /midi-webmixer/
RUN pip install /midi-webmixer/

ENTRYPOINT ["webmixer"]
CMD ["/config.ini"]
