#!/usr/bin/env bash

for i in $(ls input*)
do
    echo Fichier: $i
    output=$(echo $i | sed 's/input/output/')
    soluce=$(echo $i | sed 's/input/soluce/')
    cat $i | python ex.py > $soluce
    diff <(sed -e '$a\' $output) $soluce && echo OK
done