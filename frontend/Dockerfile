FROM docker.io/python:3.6-alpine
RUN pip install flask requests
EXPOSE 8080
USER root
COPY . /mashup-frontend
RUN chgrp -R 0 /mashup-frontend \
    && chmod -R g=u /mashup-frontend
USER 1001
WORKDIR /mashup-frontend

ENTRYPOINT ["python"]
CMD ["app/app.py"]
