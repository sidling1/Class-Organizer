# BUgs to fix
- Other person can access account by changin url
- Multiple times message gets saved due to multiple socket calls
- One student one course only
- logout errors
- when course create, chat auto create
- files upload

# Acadger
A Convenient way of data handling system for schools and colleges integrated with four basic operations of data storage in Computer-Science CRUD(create,read,update and delete),
complementary with an efficient student-Teacher interaction.

## Installation
 Python and Django need to be installed.
```bash
pip install django
```
## Usage
```bash
python manage.py makemigrations info

python manage.py migrate
```
Go to Acadger folder and run
```bash
python manage.py runserver
```
Then go to the browser and enter the url **http://loaclhost:8000/**

