#! /bin/sh
echo $INPUT_SWITCH

if [ "$INPUT_SWITCH" == "registry" ] ; then
    echo "python should do something"
else
    echo "Nope"
fi
