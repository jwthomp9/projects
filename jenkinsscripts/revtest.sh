#!/bin/bash

oldowner="joe.thompson@1stdibs.com"
newowner="archives@1stdibs.com"
input="https://docs.google.com/document/d/1uhX4kNtiSWDYc_FaoaWeDq5dfuNSFbW08EpvTt9LB1g/edit"
inputrev=$(echo $input | rev | cut -d '/' -f 2 | rev)

echo $inputrev
echo $oldowner
echo $newowner
