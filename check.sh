#! /bin/sh

echo "Repository: https://github.com/$INPUT_REPOSITORY"
echo "Calling howfairis https://github.com/$INPUT_REPOSITORY"
if [ "$INPUT_SWITCH" == "repository" ] ; then
    /usr/local/bin/python /data/1-repository/check_repository.py
elif [ "$INPUT_SWITCH" == "license" ] ; then
    /usr/local/bin/python /data/2-license/check_license.py
elif [ "$INPUT_SWITCH" == "registry" ] ; then
    /usr/local/bin/python /data/3-registry/check_registry.py
elif [ "$INPUT_SWITCH" == "citation" ] ; then
    /usr/local/bin/python /data/4-citation/check_citation.py
elif [ "$INPUT_SWITCH" == "checklist" ] ; then
    /usr/local/bin/python /data/5-checklist/check_checklist.py
else
    echo "You need to specify the value of \$SWITCH as one of 'repository', 'license', 'registry', 'citation', or 'checklist'."
fi
