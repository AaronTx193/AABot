#!/bin/bash

while true; do
    python3 bot.py
    exit_code=$?

    if [ $exit_code == 2 ]
    then
        echo "Terminate exit code recieved. Exiting"
        break
    elif [ $exit_code == 3 ]
    then
        seconds=1
        echo "Restarting without delay"
    else
        seconds=5
    fi

    # git reset --hard


    for ((second=$seconds; second > 0; second--))
    do
        echo -ne "Restarting in $second seconds..\r"
        sleep 1
    done
done