help:  # Use the keyword "make" plus the any of the commands in blue bellow e.g.: make diff
	@egrep -h '\s#\s' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?# "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

req:   # Step 1: Install requirements.txt file - command: make req
	@echo "⬇ ⬇ ⬇ Installing Requirements.txt ⬇ ⬇ ⬇"
	@pip install -r requirements.txt
	@echo "👉 Congratulations. You are ready to use this template"

venv:  # Option 1: Use venv as a virtual environment - command: make venv
	@echo "**********  Creating Virtual Enviroment ********** "
	@python -m venv venv
	@echo "✨ Virtual environment successfully created ✨"
	@echo "👉 To activate this environment use the following command: . venv/bin/activate"
	@echo "👉 To deactivate this environment type: deactivate"


conda: # Option 2: Use conda as a virtual environment - command: make conda
	@echo "**********  Creating Virtual Enviroment ********** "
	@conda create --name testing python=3.9 -y

check: # Check code formating on files inside the src folder - command: make check
	@echo "********** Checking code formating with flake8 ********** "
	@flake8 src

diff:  # Check difference on files inside the src folder - command: make diff
	@echo "********** Checking what is different ********** "
	@black src --check --diff

standard:    # Format all code on files inside the src folder - command: make standard
	@echo "**********  Formating code with black **********"
	@black src
	@echo "\n 📤 Code ready for git push 📤 \n"

remove:       # Remove environment - command: make remove
	@rm -rf venv

