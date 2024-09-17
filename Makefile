# Makefile

# Variabel
PYTHON = python3
MANAGE = $(PYTHON) manage.py
RUNSERVER_CMD = $(MANAGE) runserver

# Target default
default: runserver

# Target untuk menjalankan server Django
runserver:
	$(RUNSERVER_CMD)

# Target untuk migrasi database
migrate:
	$(MANAGE) migrate

# Target untuk membuat superuser
createsuperuser:
	$(MANAGE) createsuperuser

# Target untuk menjalankan server dalam mode debug
runserver_debug:
	$(MANAGE) runserver --settings=your_project.settings.debug
