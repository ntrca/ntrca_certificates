* Git clone, you can use the command: <br>
    if you want to clone the repository with https: <br>
        git clone https://github.com/ntrca/ntrca_certificates.git <br>
    if you want to clone the repository with ssh: <br> 
        git clone git@github.com:ntrca/ntrca_certificates.git <br>
    if you want to clone the repository with GitHub CIL: <br>
        git clone gh repo clone ntrca/ntrca_certificates <br>

* Go to the directory:
    cd ntrca_certificates

* Create database:
    if your os is windows, you can use the command:
    > C:\Program Files\PostgreSQL\postgres version\bin
    ![alt text](https://i.ibb.co/Wk6bzWj/Screenshot-1.png)
        click the path and write:
            > cmd
            > psql -U postgres

    and then input the following command:
        > create database Database Name;
    if your os is linux, you can use the command:
        > sudo -u postgres psql
    and then input the following command:
        > create database Database Name;

* if you want to create postgres user, you can use the command:
    > psql -U postgres
    > create user your user name with encrypted password 'mypassword';
    > create database Database Name;
    > grant all privileges on database Database Name to your user name;

* Go to DB Directory and copy final_data.psql
    if your os is windows, you can use the command:
        > C:\Program Files\PostgreSQL\postgres version\bin
        click the path and write:
            > cmd
            > psql -U your user name -d your Database Name -h 127.0.0.1 -f database path\final_data.psql
    if your os is linux, you can use the command:
        > sudo -u postgres psql -d your Database Name -h 127.0.0.1 -f database path/final_data.psql

* Then go to project directory and run the following command:
    > python manage.py makemigrations
    > python manage.py migrate
    > python manage.py createsuperuser
        Enter the username for the superuser: example (admin)
        Enter the email for the superuser: example (admin@gmail.com) # Optional
        Enter the password for the superuser: example (admin)
    > python manage.py runserver
