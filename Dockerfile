FROM python:3.7.4-buster

RUN git clone https://github.com/adamcathersides/midi-webmixer.git && \
pip install /midi-webmixer/

ENTRYPOINT ["webmixer"]
CMD ["/config.ini"]
