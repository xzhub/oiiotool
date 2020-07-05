FROM python:3.7.3-slim

COPY remove_spec.py /usr/bin/
RUN chmod 755 /usr/bin/remove_spec.py
COPY oiio-2.0.5-cp37-none-linux_x86_64.whl /tmp/
RUN pip install --no-cache-dir /tmp/oiio-2.0.5-cp37-none-linux_x86_64.whl \
    && rm /tmp/oiio-2.0.5-cp37-none-linux_x86_64.whl
