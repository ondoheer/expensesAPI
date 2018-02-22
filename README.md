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

// use python manage.py
$ docker-compose exec SPENDY python manage.py <command>

// MIGRATIONS
$ docker-compose exec spendy bash -c "python manage.py db init"
$ docker-compose exec spendy bash -c "python manage.py db migrate --message '<message>' "
$ docker-compose exec spendy bash -c "python manage.py db upgrade "
```

## TODO

* Development Seeders
* REAL server responses
