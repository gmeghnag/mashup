FROM docker.io/python:3.6-alpine
RUN pip install flask
EXPOSE 8080
USER root
COPY . /mashup-foods-v2
RUN chgrp -R 0 /mashup-foods-v2 \
    && chmod -R g=u /mashup-foods-v2
USER 1001
WORKDIR /mashup-foods-v2

ENTRYPOINT ["python"]
CMD ["app/app.py"]
