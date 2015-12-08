#!/bin/bash

# caso uma excecao ocorra antes do "echo", a excecao eh lancada para cima e faz
# com que o jenkins entenda a excecao e reporte o problema
set -e  # If occur any error, exit
function to_console {
    echo -e "\n $1 \n"
}

# construcao do virtualenv, instacao das dependencias e execucao dos testes
virtualenv venv/
to_console " --> Created the Virtualenv."

source venv/bin/activate
to_console " --> Activated the Virtualenv."

pip install -r venv/requirements.txt
to_console " --> Installed the requirements."

python tests/run_tests.py
to_console " --> Ran the tests in tests/run_tests.py."