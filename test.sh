#!/bin/bash

engine_path=$1

# docker build
docker build -t test $engine_path
if [ "$?" -ne "0" ]
then
    echo `"docker build -t test $engine_path" failed`
    exit 1
fi

# docker run
pgn_example='[Site "Chess.com"]
[Date "2019.05.27"]
[Event "Vs. Computer"]
[Round "1"]
[White "Guest"]
[Black "Computer Level 2"]
[Result "*"]
[CurrentPosition "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"]

 *'

output=$(docker run -it -e pgn="$pgn_example" test)
if [ "$?" -ne "0" ]
then
    echo `"docker run -it -e pgn=test $engine_path" failed`
    exit 1
fi

# validate returned move
python3 validator.py "$pgn_example" "$output"
if [ "$?" -ne "0" ]
then
    echo `Returned move ("$output") was invalid`
    exit 1
fi

echo "All tests have passed"
