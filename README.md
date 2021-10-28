* Git clone, you can use the command: <br>
    if you want to clone the repository with https: <br>
        > git clone https://github.com/ntrca/ntrca_certificates.git <br>
    if you want to clone the repository with ssh: <br> 
        > git clone git@github.com:ntrca/ntrca_certificates.git <br>
    if you want to clone the repository with GitHub CIL: <br>
        > git clone gh repo clone ntrca/ntrca_certificates <br>
<br><br>
* Go to the directory: <br>
    cd ntrca_certificates <br>
<br><br>

* Create virtual environment: <br>
    > python -m venv your venv name <br>
    if your os is windows, you can use the command: <br>
    > your venv name\Scripts\activate <br>
    if your os is linux then you can use this command: <br>
    > source your venv name/bin/activate <br>
<br><br>

* Then install requirements.txt
    > pip install -r requirements.txt

* Create database: <br>
    if your os is windows, you can use the command: <br>
    > C:\Program Files\PostgreSQL\postgres version\bin <br>
  ![alt text](https://i.ibb.co/Wk6bzWj/Screenshot-1.png) <br>
        click the path and write: <br>
            > cmd <br>
            > psql -U postgres <br>
<br><br>
    and then input the following command: <br>
        > create database Database Name; <br>
    if your os is linux, you can use the command: <br>
        > sudo -u postgres psql <br>
    and then input the following command: <br>
        > create database Database Name; <br>
<br><br>
* if you want to create postgres user, you can use the command: <br>
    > psql -U postgres<br>
    > create user your user name with encrypted password 'mypassword';<br>
    > create database Database Name;<br>
    > grant all privileges on database Database Name to your user name;<br>
<br><br>
* Go to DB Directory and copy final_data.psql with path<br>
    if your os is windows, you can use the command:<br>
        > C:\Program Files\PostgreSQL\postgres version\bin<br>
        click the path and write:<br>
            > cmd <br>
            > psql -U your user name -d your Database Name -h 127.0.0.1 -f database path\final_data.psql<br>
    if your os is linux, you can use the command:<br>
        > sudo -u postgres psql -d your Database Name -h 127.0.0.1 -f database path/final_data.psql<br>
<br><br>

* Go to the example and copy local_settings.txt and pest in <span style="color: red">ntrca</span> and rename local_settings.txt to local_settings.py
* Open  local_settings.py
* Then Enter here your database name: 'NAME': 'your db name',
* Then Enter here your postgres username: 'USER': 'postgres',
* Then Enter here your postgres password: 'PASSWORD': 'your password',
* Then go to project directory and run the following command:<br>
    > python manage.py makemigrations<br>
    > python manage.py migrate<br>
    > python manage.py createsuperuser<br>
        Enter the username for the superuser: example (admin)<br>
        Enter the email for the superuser: example (admin@gmail.com) # Optional<br>
        Enter the password for the superuser: example (admin)<br>
    > python manage.py runserver<br>
