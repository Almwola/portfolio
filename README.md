# Mohamed Abd Elmwoli — Portfolio (Django)

Single-page portfolio built with Python and Django. Projects, skills and
certificates are stored in the database and edited from the Django admin.

## Run locally

```bash
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt

python manage.py migrate
python manage.py seed_portfolio   # loads the real content (safe to re-run)
python manage.py createsuperuser  # for /admin
python manage.py runserver
```

Open http://127.0.0.1:8000/ and the admin at http://127.0.0.1:8000/admin/.

## Things to add yourself

| What | Where |
|---|---|
| CV | Put `Mohamed-Abd-Elmwoli-CV.pdf` in `portfolio/static/portfolio/assets/`. Until then `/cv/` returns a clear 404 message. |
| Certificate images | Admin → Certifications → upload the image. The modal shows it on click. |
| GitHub link per project | Admin → Projects → `github_url`. All projects currently point to the profile `https://github.com/Almwola`. |
| Live demo links | Admin → Projects → `demo_url`. Left empty, the demo button is hidden (featured cards show "coming soon"). |

## Contact form

Messages are saved to the database (Admin → Contact messages), so nothing is
lost and nothing is faked. Email notification is optional and only used when
these environment variables are set:

```
EMAIL_HOST, EMAIL_PORT, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, CONTACT_NOTIFY_EMAIL
```

## Deployment notes

```
DJANGO_DEBUG=0
DJANGO_SECRET_KEY=<long random string>
DJANGO_ALLOWED_HOSTS=yourdomain.com
DJANGO_CSRF_TRUSTED_ORIGINS=https://yourdomain.com
```

Then run `python manage.py collectstatic` and serve with gunicorn
(`gunicorn config.wsgi`). WhiteNoise serves the static files. Uploaded
certificates live in `media/`; serve that folder from your web server or
object storage in production. For PostgreSQL, change `DATABASES` in
`config/settings.py` and install `psycopg[binary]`.
