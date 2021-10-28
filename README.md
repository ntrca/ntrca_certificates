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
        > psql -U postgres
    and then input the following command:
        > create database testdb;
    if your os is linux, you can use the command:
        > sudo -u postgres psql
    and then input the following command:
        > create database testdb;

* if you want to create postgres user, you can use the command:
    > psql -U postgres
    > create user testuser with encrypted password 'mypassword';
    > create database testdb;
    > grant all privileges on database testdb to testuser;

* Go to DB Directory and copy final_data.psql
    if your os is windows, you can use the command:
        > C:\Program Files\PostgreSQL\postgres version\bin

![alt text](https://ibb.co/ZBVng67)
