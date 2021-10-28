* Git clone, you can use the command: <br>
    if you want to clone the repository with https: <br>
        git clone https://github.com/ntrca/ntrca_certificates.git <br>
    if you want to clone the repository with ssh: <br> 
        git clone git@github.com:ntrca/ntrca_certificates.git <br>
    if you want to clone the repository with GitHub CIL: <br>
        git clone gh repo clone ntrca/ntrca_certificates <br>
<br>
* Go to the directory: <br>
    cd ntrca_certificates <br>
<br>
* Create database: <br>
    if your os is windows, you can use the command: <br>
    > C:\Program Files\PostgreSQL\postgres version\bin <br>
    ![alt text](https://i.ibb.co/Wk6bzWj/Screenshot-1.png) <br>
        click the path and write: <br>
            > cmd <br>
            > psql -U postgres <br>
<br>
    and then input the following command: <br>
        > create database Database Name; <br>
    if your os is linux, you can use the command: <br>
        > sudo -u postgres psql <br>
    and then input the following command: <br>
        > create database Database Name; <br>
<br>
* if you want to create postgres user, you can use the command: <br>
    > psql -U postgres<br>
    > create user your user name with encrypted password 'mypassword';<br>
    > create database Database Name;<br>
    > grant all privileges on database Database Name to your user name;<br>
<br>
* Go to DB Directory and copy final_data.psql<br>
    if your os is windows, you can use the command:<br>
        > C:\Program Files\PostgreSQL\postgres version\bin<br>
        click the path and write:<br>
            > cmd<br>
            > psql -U your user name -d your Database Name -h 127.0.0.1 -f database path\final_data.psql<br>
    if your os is linux, you can use the command:<br>
        > sudo -u postgres psql -d your Database Name -h 127.0.0.1 -f database path/final_data.psql<br>
<br>
* Then go to project directory and run the following command:<br>
    > python manage.py makemigrations<br>
    > python manage.py migrate<br>
    > python manage.py createsuperuser<br>
        Enter the username for the superuser: example (admin)<br>
        Enter the email for the superuser: example (admin@gmail.com) # Optional<br>
        Enter the password for the superuser: example (admin)<br>
    > python manage.py runserver<br>
