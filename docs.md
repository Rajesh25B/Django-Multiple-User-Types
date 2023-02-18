create venv
pip install django djangorestframework Pillow djangorestframework-simplejwt psycopg2
create project
create app "users"
create app "listings"
*psql -U postgres
 CREATE DATABASE listings_users OWNER postgres;
 CREATE DATABASE listings_listings OWNER postgres;
 \l (backslash l(small el) lists all dbs)
 \q
 \password
*settings.py
	apps
	db settings
	media urls
	set globally Rest-framework permission_classes and authentication_classes
	simple_jwt settings
* work on projects urls for simple_jwt token 

	
