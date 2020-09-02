FROM ubuntu:18.04
COPY . /app
RUN make /app
CMD pip3 install -r /app/requirements.txt
CMD python /app/bot.py