#!/bin/bash
FROM --platform=linux/amd64 python:3.10
COPY . .
RUN pip install -r requirements.txt
EXPOSE 80
ENTRYPOINT [ "python" ]
CMD [ "main.py" ]