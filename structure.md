```
finance-backend/
├── alembic/
│   ├── versions/
│   ├── README
│   ├── env.py
│   └── script.py.mako
├── src/
│   ├── auth/
│   │   ├── __init__.py
│   │   ├── permissions.py
│   │   ├── routes.py
│   │   ├── schema.py
│   │   └── service.py
│   ├── bank/
│   │   ├── enums.py
│   │   ├── models.py
│   │   ├── repository.py
│   │   ├── routes.py
│   │   ├── schema.py
│   │   └── service.py
│   ├── middleware/
│   │   ├── __init__.py
│   │   └── cors.py
│   ├── transaction/
│   │   ├── enums.py
│   │   ├── models.py
│   │   ├── repository.py
│   │   ├── routes.py
│   │   ├── schema.py
│   │   └── service.py
│   ├── user/
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── repository.py
│   │   ├── routes.py
│   │   ├── schema.py
│   │   └── service.py
│   ├── utils/
│   │   └── security.py
│   ├── __init__.py
│   ├── config.py
│   ├── database.py
│   ├── exceptions.py
│   ├── main.py
│   └── pagination.py
├── tests/
│   └── __init__.py
├── versions/
│   ├── 387475aafab5_add_foreign_key_to_banks.py
│   ├── 5a4d078c696b_add_transactions_table.py
│   └── b4349d81faf6_base_tables.py
├── .DS_Store
├── .env
├── .env.template
├── .gitignore
├── Makefile
├── README.md
├── alembic.ini
├── generate_structure.py
├── logging.ini
├── poetry.lock
├── pyproject.toml
└── structure.md
```
