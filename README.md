
## Running Locally

```bash
git clone this repo
```

```bash
pip install -r requirements.txt
```

```bash
python manage.py migrate
```

```bash
python manage.py runserver
```
# audio-test


 	celery -A uploads worker -l DEBUG -E

    celery -A uploads beat -l info

    celery -A uploads purge

    celery flower -A uploads --address=127.0.0.1 --port=5555
