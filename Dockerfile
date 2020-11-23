FROM python:alpine3.7
ADD ./api /opt/api
COPY requirements.txt /opt/
RUN apk add musl-dev gcc libffi-dev openssl-dev && \
    adduser -s /bin/bash -D -g "" svc && chown -R svc. /opt
WORKDIR /opt/api/
RUN pip install -r /opt/requirements.txt
EXPOSE 5000
USER svc
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
