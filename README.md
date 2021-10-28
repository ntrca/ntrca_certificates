* Git clone, you can use the command:
    if you want to clone the repository with https:
        git clone https://github.com/ntrca/ntrca_certificates.git
    if you want to clone the repository with ssh:
        git clone git@github.com:ntrca/ntrca_certificates.git
    if you want to clone the repository with GitHub CIL:
        git clone gh repo clone ntrca/ntrca_certificates

* Go to the directory:
    cd ntrca_certificates

* Create database:
    if your os is windows, you can use the command:
        > psql -U postgres
        > create database testdb;
    if your os is linux, you can use the command:
        > psql
    and then input the following command:
        > create database testdb;

* if you want to create postgres user, you can use the command:
    > psql -U postgres
    > create user testuser with encrypted password 'mypassword';
    > create database testdb;
    > grant all privileges on database testdb to testuser;


  
