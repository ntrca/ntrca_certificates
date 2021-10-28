Step 01. Create database
    if your os is windows, you can use the command:
        > psql -U postgres
        > create database testdb;
    if your os is linux, you can use the command:
        > psql
    and then input the following command:
        > create database testdb;

if you want to create postgres user, you can use the command:
    > psql -U postgres
    > create user testuser with encrypted password 'mypassword';
    > create database testdb;
    > grant all privileges on database testdb to testuser;
  
