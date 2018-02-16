# Simple expenses Api


### Migrations with Flask-migrate

```
$ python manage.py db init

$ python manage.py db migrate

$ python manage.py db upgrade

```

## Testing and Coverage

```
# test and coverage all
$ coverage run --source app --branch -m unittest discover

# test single testcase
python -m unittest tests.auth.test_tokens

# test all
python -m unittest discover
```



