This Docker container uses the data provided in the [Select Start SQL](https://selectstarsql.com) book so you can quickly and easy run the queries as you follow along with the chapters on your local computer. 

## Setting up the local environment

* Navigate to the directory on your local computer where you plan to store the app

    ```
    mkdir path\to\new_dir
    cd ~/new_dir
    ```

* Clone/fork the git repo

    `git clone https://github.com/schererjulie/SelectStarSQL.git`

* Create a `.env` file in the main dir and load global variables (see example below)

    ```
    POSTGRES_DB=postgres
    POSTGRES_USER=postgres
    POSTGRES_PASS=postgres
    POSTGRES_HOST=localhost
    POSTGRES_PORT=5432
    ```

## Running the Docker container

* To start the docker container, you'll need to execute the compose file with a reference to the .env file 

    `docker-compose --env-file .env up -d`

* Run Python script to create deathrow table

    `python3 scripts/csv_to_sql.py`

* Connect to postgres database from the command line

    `psql postgres`

    _Alternative_ (but note you'll need to use the login credentials from the .env file) <br>
    ```
    docker-compose exec postgres /bin/bash
    psql --host=localhost --username=admin --dbname=postgres
    ```

* List all tables using the `\dt` meta-command, and **double check the deathrow table was created**

    `postgres=# \dt`

* Assuming everything's gone as expected, now you can run queries in the command line! Try the statement below. Here's what you should see:

    `SELECT "index", "Execution", "Date of Offence", "Last Name", "Age at Execution" FROM deathrow LIMIT 5` <br>    

    ```
    postgres=# SELECT "index", "Execution", "Date of Offence", "Last Name", "Age at Execution" FROM deathrow LIMIT 5;
    index | Execution | Date of Offence |   Last Name   | Age at Execution 
    -------+-----------+-----------------+---------------+------------------
        0 |       553 | 2004-11-21      | Young         |               34
        1 |       552 | 1979-05-27      | Bible         |               66
        2 |       551 | 2003-12-03      | Castillo      |               37
        3 |       550 | 2008-04-06      | Davila        |               31
        4 |       549 | 2005-09-13      | Rodriguez III |               38
    (5 rows)
    ```


* Last but not least, don't forget to **stop the running container** before closing down!

    ```
    // exit out of psql using the \q command
    postgres=# \q

    // list all running containers
    docker ps

    // stop running container (get the container id from the line above)
    docker stop <container-id>

    // (optional) free up space by removing any unused resources
    docker container prune
    ```