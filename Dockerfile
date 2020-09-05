# For more information, please refer to https://aka.ms/vscode-docker-python
# FROM python

# # Keeps Python from generating .pyc files in the container
# # ENV PYTHONDONTWRITEBYTECODE 1
# # Turns off buffering for easier container logging
# # ENV PYTHONUNBUFFERED 1

# # Install pip requirements
# # ADD requirements.txt .
# RUN mkdir /app
# WORKDIR /app
# COPY requirements.txt /app/
# RUN pip install -r requirements.txt

# ADD . /app/
# COPY bot.py /app/
# # Switching to a non-root user, please refer to https://aka.ms/vscode-docker-python-user-rights
# # RUN useradd appuser && chown -R appuser /app
# # RUN chmod +x /app/bot.py
# # USER appuser

# # During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
# CMD ["python", "bot.py"]

FROM python

WORKDIR /app

COPY bot.py .

COPY requirements.txt .

#RUN apt update

#RUN apt install python3

RUN pip3 install -r requirements.txt

CMD ["python","bot.py"]

