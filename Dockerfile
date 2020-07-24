FROM python:3.7.3-slim

RUN apt-get update && apt-get install -y wget gmic
COPY oiio-2.0.5-cp37-none-linux_x86_64.whl /tmp/
RUN pip install --no-cache-dir /tmp/oiio-2.0.5-cp37-none-linux_x86_64.whl \
    && rm /tmp/oiio-2.0.5-cp37-none-linux_x86_64.whl

COPY remove_spec.py resize.py report_size.py convert2jpg.py /usr/bin/
RUN chmod 755 /usr/bin/*.py