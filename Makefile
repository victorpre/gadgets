build-backend:
	venv/bin/python3 venv/bin/pip3 install -r requirements.txt
	venv/bin/python3 backend/manage.py migrate

run-backend:
	venv/bin/python3 backend/manage.py runserver

run-frontend:
	cd frontend && npm start

run-tests:
	venv/bin/python3 backend/manage.py test
