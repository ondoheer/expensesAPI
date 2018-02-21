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

# terminal report
$ coverage report

# html report
$ coverage html

# test single testcase
python -m unittest tests.auth.test_tokens

# test all
python -m unittest discover
```

## Docker comands

```
// Run the project
$ docker-compose run

// access psotgres cli
$ docker-compose exec postgres psql -U spendy

# I'm not really loving docker, just because in general I hate devops
```
