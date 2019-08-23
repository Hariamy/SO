#!/bin/bash

declare -a ARRAY

exec 10<&0

exec < $1

let count=0
while read LINE; do
	for word in $LINE; do	
		ARRAY[$count]=$word"  "
		((count++))
	done
	ARRAY[$count]="\n"
	((count++))
done

for elemento in $ARRAY; do
	if [$elemento -eq "\n"]; then
		echo -e $elemento
	else
		echo $elemento
	fi
done


exec 0<&10 10<&-
