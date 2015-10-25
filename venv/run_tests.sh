#!/bin/bash

virtualenv venv/
echo ""
echo " --> Created the Virtualenv."

source venv/bin/activate
echo ""
echo " --> Activated the Virtualenv."
echo ""

pip install -r venv/requirements.txt
echo ""
echo " --> Installed the requirements."
echo ""

python tests/run_tests.py
echo ""
echo " --> Ran the tests in tests/run_tests.py"

deactivate
echo ""
echo " --> Deactivated the Virtualenv."
echo ""