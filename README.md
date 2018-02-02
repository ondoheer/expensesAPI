# Simple expenses Api


### Migrations with Flask-migrate

```
$ python manage.py db init

$ python manage.py db migrate

$ python manage.py db upgrade

```

## Endpoints


Endpoint | method | expects | returns
---------|--------|---------|
/login | POST | JSON user, password | access_token, refresh_token
/refresh | POST | HEADER access_token | refresh_token
/main       | GET | HEADER access_token | {
    "months": [
        {
            "2018-2": {
                "categories": {
                    "3": {
                        "amount": 23.5,
                        "label": "Taxi",
                        "name": "taxi"
                    }
                },
                "total": 23.5
            }
        }
    ]
}

/expense | POST | HEADER access_token, {
	"amount": "23.5",
	"name": "gasto de prueba",
	"category_id": 3
} | {"msg":"text"}
/expense | GET |  HEADER access_token |
     [
        {
            "amount": 34.5,
            "category_id": 2,
            "date": "Thu, 01 Feb 2018 16:04:10 GMT",
            "id": 11,
            "month_id": null,
            "name": "comida china",
            "user_id": 4
        }, ...]
/category | GET |  HEADER access_token | [
    {
        "id": 32,
        "label": "Peluquería",
        "name": "peluqueria",
        "user_id": 4
    }, ...]
/category   | POST |  HEADER access_token {
	"label": "Nueva Categoria"
} | {"msg":"text"}

