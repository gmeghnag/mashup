FROM docker.io/python:3.6-alpine
RUN pip install flask
EXPOSE 8080
USER root
COPY . /mashup-foods-v1
RUN chgrp -R 0 /mashup-foods-v1 \
    && chmod -R g=u /mashup-foods-v1
USER 1001
WORKDIR /mashup-foods-v1

ENTRYPOINT ["python"]
CMD ["app/app.py"]
