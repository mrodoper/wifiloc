# wifiloc

This is a wifi based positioning project. It takes the wifi scans fed into it and based on this data, it estimates where the wifi routers are.

# Setup

If you like to use virtualenv:

To activate: $ mkvirtualenv --python=/usr/bin/python3 -a ./src/ wifiloc -r ./req_virtualenv.txt
To deactivate: $ deactivate

If you want to use anaconda:

To install anaconda visit: http://conda.pydata.org/docs/installation.html
To create environment: $ conda create --name wifi_pos python=3
To activate: $ source activate wifi_pos
To deactivate: $ source deactivate

# Tests

go to root of your project and run for individual test in a package

$ python -m unittest test.unit.scan_test

# Linting

Install lint: https://www.pylint.org/
To start the inspection: $ pylint <module or package>
There is already a .pylintrc file in the repo

# Run

run the scripts from src/.
$ python main.py
