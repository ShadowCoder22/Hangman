#!/bin/bash

docker rm -f hangman
docker run --name hangman -it shadowcoder22/hangman:1.0.0
