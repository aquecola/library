#!/bin/bash

echo "What are you looking for?"
read x
echo "---"
cat /home/aquecola/knowledge_progress/notes | grep $x