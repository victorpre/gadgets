run-backend:
	venv/bin/python3 backend/manage.py runserver

run-frontend:
	cd frontend && npm start
