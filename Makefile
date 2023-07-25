# Linux - Macox
#export PYTHONPATH=$HOME/Developer/Python/:$PYTHONPATH
# Windows
#set PYTHONPATH=C:\path\to\dirWithScripts\;%PYTHONPATH%
install-dep:
	pip install flask
	pip install flask_restful
	pip install unittest
	
start-local:
	python apps/backend/public/app.py

acceptance-test:
	#python -m unittest discover -s tests/ -p "*_test.py" -v
	python -m pytest -ra -s tests/apps/ -v

test:
	python -m pytest -ra -s tests/src/ -v