FROM python:3.11.0-bullseye
RUN apt-get -y update &&\
    apt-get -y install wkhtmltopdf xvfb &&\
    printf '#!/bin/bash\nxvfb-run -a --server-args="-screen 0, 1024x768x24" /usr/bin/wkhtmltopdf -q $*' > /usr/bin/wkhtmltopdf.sh &&\
    chmod a+x /usr/bin/wkhtmltopdf.sh &&\
    ln -s /usr/bin/wkhtmltopdf.sh /usr/local/bin/wkhtmltopdf
WORKDIR /app
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY ./app .
RUN chmod +x /app/script.sh
CMD ["/bin/sh", "-c", "./app/script.sh && python ./app/run.py"]
