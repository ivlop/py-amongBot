# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3

# Keeps Python from generating .pyc files in the container
# ENV PYTHONDONTWRITEBYTECODE 1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

# Install pip requirements
# ADD requirements.txt .
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt

ADD . /app/

# Switching to a non-root user, please refer to https://aka.ms/vscode-docker-python-user-rights
# RUN useradd appuser && chown -R appuser /app
# RUN chmod +x /app/bot.py
# USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
# RUN python3 ./app/bot.py
# CMD ["python", "bot.py"]
