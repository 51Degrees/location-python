![51Degrees](https://51degrees.com/DesktopModules/FiftyOne/Distributor/Logo.ashx?utm_source=github&utm_medium=repository&utm_content=readme_main&utm_campaign=python-open-source) 
**v4 Location Python**

[Pipeline Documentation](https://docs.51degrees.com?utm_source=github&utm_medium=repository&utm_content=documentation&utm_campaign=python-open-source "advanced developer documentation")

## Introduction

This project contains the geo-location engines for the Python implementation of the 51Degrees Pipeline API.

The Pipeline is a generic web request intelligence and data processing solution with the ability to add a range of 51Degrees and/or custom plug ins (Engines) 

## Requirements and installation

* Python 2.7 or Python 3
* The `flask` python library to run the web examples

## Running examples

To run examples from this folder:

`python3 -m examples.cloud.gettingstarted`

To run the web example:

### Linux

Execute `export FLASK_APP=` with the name of the web example file, then `flask run`.

### Windows

Execute `$env:FLASK_APP = "x"` with the name of the example file, then `flask run`.
