INITIAL SETUP

create venv
pip install django djangorestframework Pillow djangorestframework-simplejwt psycopg2
create project
create app "users"
create app "listings"
\*psql -U postgres
CREATE DATABASE listings_users OWNER postgres;
CREATE DATABASE listings_listings OWNER postgres;
\l (backslash l(small el) lists all dbs)
\q
\password

\*settings.py
apps
db settings
media urls
set globally Rest-framework permission_classes and authentication_classes
simple_jwt settings
setup projects urls for simple_jwt token

IMP POINTS

- In django, cross-database relationships are not supported in django

1. users app

USER MODEL SETUP

- implement custom user model
- change settings AUTH_USER_MODEL
- makemigrations, but dont migrate yet bcoz we have two dbs, and no default db yet
  if we migrate, it migrates the default, but I wanna migrate to users db, so i need to
  have a router in order to accomplish that.
  TO manage routers, we have a setting DATABASE_ROUTERS

DB_ROUTER SETUP

- create a file router.py
- create a router class, add apps and develop funcs in it.
- now migrate 'python manage.py migrate users --database=users'
- connect to the db on psql using
  \l (lists all available dbs)
  \c coffee_users (connect to the coffee_users db)
  \dt (lists out the tables)
  coffee_users=# SELECT \* FROM users_useraccount (gives us the data)
  \q (Exists out the db terminal)
- create superuser
- access admin site
- we get error, so add some apps to router.py file and check admin site working
  properly

2. coffee_types app

- create a Coffee model and define model fields and methods
- run makemigrations
- create router.py file and configure settings
- migrate 'python manage.py migrate coffee_types --database=listings'
- connect to the db on psql using
  \l (lists all available dbs)
  \c coffee_listings (connect to the coffee_listings db)
  \dt (lists out the tables)
  coffee_users=# SELECT \* FROM coffee_types_coffee; (gives us the data)
  \q (Exists out the db terminal)

3. logic for registering an account, retrieving the user data, test out auth based endpoints

- create 2 drf views (register and retreive) in views.py (one needs no permissions and other needs them)
- create urls.py and include in main projects urls.py
- test in postman by registering few accounts with switching flags of is_accountant, is_manager etc.
- register normal users
- register other user
- login normal/other user==> pass email&pwd, get refresh and access tokens
- retrieve user profile at api/auth/me/ endpoint by passing authorization headers with access tokens
- get new access token by passing refresh token on endpoint api/token/refresh
- hit verify endpoint at api/token/verify/ by passing newly generated at refresh endpoint
  access token and expect "{}" as output
