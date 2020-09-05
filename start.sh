#!/bin/bash
docker build -t amongBot .
docker run -it --rm amongBot &

#python3 bot.py >> log.txt
