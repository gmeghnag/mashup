FROM docker.io/python:3.6-alpine
RUN pip install flask requests
EXPOSE 8080
USER root
COPY . /mashup
RUN chgrp -R 0 /mashup \
    && chmod -R g=u /mashup
USER 1001
WORKDIR /mashup

ENTRYPOINT ["python"]
CMD ["app/app.py"]
