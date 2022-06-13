FROM python:3.8-alpine
LABEL version="1'0" maintainer="RJP"
COPY * /app/
RUN pip3 install Flask
EXPOSE 8080
ENV ENVIRONMENT="DEV"
ENV DISPLAY_FONT="arial"
ENV DISPLAY_COLOR="red"

#TODO *bonus* add a health check that tells docker the app is running properly

RUN chmod 777 /app/app.py
USER 1000
CMD python3 /app/app.py
HEALTHCHECK CMD curl --fail http://localhost:8080
