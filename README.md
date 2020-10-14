# WebStore
Web store is a personal project in wich I apply all I have learned about framework Django

## How to install:
Clone the repository:
```git
git clone <link-http-to-clone-this-project>   
```
Open project file:
```bash
cd WebStore
```
Install python3 and pip3, then create virtualenv:
```
virtualenv venv -p python3
```
Run virtualenv.
```
source ./venv/bin/activate
```
Install dependences:
```
pip3 install -r requirements.txt 
```
## Configurations:
There is a .env.example fileinto webStorePlan folder. You must copy and paste it in the same path with the next name: <.env>
<br></br>Here you can config the secret_key and another variables of project
## Database
This project use MariaDB:10.4. You can create a docker for it.
<br></br>Pull the image:
```
docker pull mariadb:10.4
```
Create your docker:
```
docker run -d -p 3306:3306 --name <docker_name> -e MYSQL_ROOT_PASSWORD=<password_root_user> -e MYSQL_DATABASE=<database_name> -e MYSQL_USER=<database_user_name> -e MYSQL_PASSWORD=<database_user_password> -d mariadb:10.4
```
Where 

* **<docker_name>** - *name of your docker*
* **<password_root_user>** - *It is the password you want use in your user root of MariaDB*
* **<database_name>** - *name of database*
* **<database_user_name>** - *user name for the <database_name>*
* **<database_user_password>** - *password of <database_user_name>*
<br></br>
Run your docker
<br></br>
Makemigrations, migrate and superuser:
```
python3 manage.py makemigrations
```
```
python3 manage.py migrate
```
Next line will ask you a user_name and user_password:
```
python3 manage.py createsuperuser
```
Now, you can run the app:
```
python3 manage.py runserver
```
