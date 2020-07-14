FROM python:3.7.3-slim

COPY remove_spec.py resize.py /usr/bin/
RUN chmod 755 /usr/bin/*.py
RUN apt-get update && apt-get install -y wget gmic
COPY oiio-2.0.5-cp37-none-linux_x86_64.whl /tmp/
RUN pip install --no-cache-dir /tmp/oiio-2.0.5-cp37-none-linux_x86_64.whl \
    && rm /tmp/oiio-2.0.5-cp37-none-linux_x86_64.whl
