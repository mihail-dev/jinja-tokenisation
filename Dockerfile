FROM centos:latest

RUN curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py" && python get-pip.py && rm -f get-pip.py && pip install jinja2

COPY templates /opt/templates

COPY tokenisation.py /opt

CMD /bin/bash