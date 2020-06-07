# flask-simple-attendance-system
**Simple attendance system using Flask framework**

---


**Features**
- Login and logout
- View and report attendance
- User CRUD (*admin only*)

---

**Using the app**
1. Rename `config_sample.py` to `config.py` and adjust the configuration
2. Migrate the database
```
example:
flask db init
flask db migrate
flask db upgrade
```
3. Select the flask environment to run
```
example:
set flask_config=development
set flask_env=development
set flask_app=run.py
```
4. Create admin user by accessing `app_url/user/create-admin`
5. Log in (admin email `admin@mail.com` and password `12345678`)
