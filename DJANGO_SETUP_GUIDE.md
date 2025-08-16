# Django Backend Setup Guide 🚀

This guide will walk you through setting up and running the Django backend for the Nepal Health Ministry E-Aarogya app.

## Prerequisites

Before starting, make sure you have:
- Python 3.8+ installed
- pip (Python package manager)
- Git (optional, for version control)

## Step 1: Navigate to Backend Directory

Open your terminal/command prompt and navigate to the backend directory:

```bash
cd C:\Users\Dell\E-Aarogya\backend
```

## Step 2: Create Virtual Environment (Recommended)

Create a virtual environment to isolate project dependencies:

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

You should see `(venv)` in your command prompt when activated.

## Step 3: Install Dependencies

Install all required Python packages:

```bash
# Install main Django dependencies
pip install django djangorestframework django-cors-headers django-filter

# Install database dependencies
pip install psycopg2-binary  # For PostgreSQL (recommended)
# OR
pip install sqlite3  # For SQLite (simpler setup)

# Install EWARS PDF extraction dependencies
pip install -r requirements_pdf.txt
```

## Step 4: Database Setup

### Option A: SQLite (Easier for Development)

SQLite is included with Python and requires no additional setup.

1. Update `health_ministry/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

### Option B: PostgreSQL (Production Ready)

1. Install PostgreSQL on your system
2. Create a database and user
3. Update `health_ministry/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'eaarogya_db',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## Step 5: Run Database Migrations

Create and apply database migrations:

```bash
# Create migration files
python manage.py makemigrations

# Apply migrations to database
python manage.py migrate
```

## Step 6: Create Superuser (Optional)

Create an admin user to access Django admin panel:

```bash
python manage.py createsuperuser
```

Follow the prompts to set username, email, and password.

## Step 7: Load Sample Data

Load initial data for diseases, locations, and safety tips:

```bash
# Load sample outbreak data
python manage.py loaddata sample_data.json

# Import EWARS data (requires internet connection)
python manage.py import_ewars_data --max-bulletins=3
```

## Step 8: Start Development Server

Run the Django development server:

```bash
python manage.py runserver
```

You should see output like:
```
System check identified no issues (0 silenced).
August 13, 2025 - 23:15:00
Django version 4.2.0, using settings 'health_ministry.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

## Step 9: Test API Endpoints

Open your browser or use a tool like Postman to test these endpoints:

### Basic Endpoints:
- http://127.0.0.1:8000/admin/ (Django Admin)
- http://127.0.0.1:8000/api/v1/districts/ (Districts list)
- http://127.0.0.1:8000/api/v1/outbreaks/ (Outbreaks list)

### EWARS Enhanced Endpoints:
- http://127.0.0.1:8000/api/v1/ewars/national-overview/
- http://127.0.0.1:8000/api/v1/ewars/disease-tracker/
- http://127.0.0.1:8000/api/v1/ewars/outbreak-alerts/
- http://127.0.0.1:8000/api/v1/ewars/safety-tips/

## Step 10: Connect Frontend

Once the backend is running, your React Native frontend can connect to:
- Base URL: `http://localhost:8000` (for local development)
- API Base: `http://localhost:8000/api/v1/`

## Troubleshooting

### Common Issues:

**1. Port Already in Use**
```bash
# Run on different port
python manage.py runserver 8001
```

**2. Database Connection Error**
- Check database credentials in settings.py
- Ensure database server is running
- For PostgreSQL: `pg_ctl start`

**3. Module Not Found Error**
```bash
# Ensure virtual environment is activated
venv\Scripts\activate

# Reinstall dependencies
pip install -r requirements.txt
```

**4. Migration Errors**
```bash
# Reset migrations (WARNING: This deletes data)
python manage.py migrate --fake-initial

# Or delete migration files and recreate
rm outbreaks/migrations/0*.py
python manage.py makemigrations
python manage.py migrate
```

**5. CORS Issues (Frontend can't connect)**
- Ensure `django-cors-headers` is installed
- Check `CORS_ALLOWED_ORIGINS` in settings.py

## Development Workflow

### Daily Development:
1. Activate virtual environment: `venv\Scripts\activate`
2. Start server: `python manage.py runserver`
3. Make changes to code
4. Server auto-reloads on file changes

### Adding New Features:
1. Create/modify models in `models.py`
2. Run: `python manage.py makemigrations`
3. Run: `python manage.py migrate`
4. Update views and URLs as needed

### Updating EWARS Data:
```bash
# Fetch latest data from EWARS
python manage.py import_ewars_data --max-bulletins=5 --save-raw
```

## Production Deployment

For production deployment, consider:
1. Use PostgreSQL database
2. Set `DEBUG = False` in settings.py
3. Configure proper `ALLOWED_HOSTS`
4. Use environment variables for secrets
5. Set up proper logging
6. Use a production WSGI server like Gunicorn

## Useful Commands

```bash
# Check for issues
python manage.py check

# Create new app
python manage.py startapp app_name

# Django shell (interactive Python with Django)
python manage.py shell

# Show all URLs
python manage.py show_urls

# Collect static files
python manage.py collectstatic
```

## Next Steps

Once your backend is running:
1. Test all API endpoints
2. Start your React Native frontend
3. Verify data flows between frontend and backend
4. Import real EWARS data
5. Test the complete application flow

Happy coding! 🎉
