import os.path
from os import path
import yaml
from voluptuous import Schema, MultipleInvalid, Invalid, Required, Any, Optional, ALLOW_EXTRA


def file_check(filename):
    if path.isfile(filename):
        print ("File " +  filename + " found")
        return "File Found"
    else: 
        print("File " + filename + " not found")
        return "File Not Found"

def YAML_check(filename):
    with open(filename) as file:
    try:
        citation = yaml.safe_load(file)
        return "YAML file loaded"
    except yaml.YAMLError as exc:
            print(exc)
        return "YAML failed to load"



def Contents_check(filename):
    file = open(filename)
    citation = yaml.safe_load(file)
    s = Schema({
        Required("doi"): str,
        Required("title"): str,
        Optional("version"): str,
        Required("authors"): dict,
        Required("license"): str,
        },
        extra=ALLOW_EXTRA
        )

    try:
        s(citation)
        print("Passed")
        return "Citation Scheme passed"	
    except	 MultipleInvalid as e:
        exc = e
        print ("Error: " + str(exc))
        return "Citation Schema not Valid"





def main():
    print('Citation Check')
    filename = 'CITATION.cff'
    print (filename)
    print(file_check(filename))
    print(YAML_check(filename))
    print(Contents_check(filename))



if __name__ == "__main__":
    main()
