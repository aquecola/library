#!/bin/bash

[ $# -ne 1 ] && echo "1 argument requared, got $#" && exit 1
x=$1
cat /home/$USER/code/library/notes | grep $x
