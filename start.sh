#!/bin/bash
docker build -t among_bot .
docker run -i --name among_bot --rm among_bot &

#python3 bot.py >> log.txt
