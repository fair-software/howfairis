#! /bin/sh

if [ "$INPUT_SWITCH" == "registry" ] ; then
    /usr/local/bin/python /data/3-registry/check_registry.py
else
    echo "Nope"
fi
