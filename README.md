This Docker container uses the data provided in the [Select Start SQL](https://selectstarsql.com) book so you can quickly and easily run the queries as you follow along with the chapters on your local computer. 

## Setting up the local environment

* Navigate to the directory where you plan to store the repo on your local computer

    ```
    mkdir path\to\new_dir
    cd ~/new_dir
    ```

* Clone/fork the git repo

    ```
    git clone https://github.com/schererjulie/SelectStarSQL.git
    ```

* Copy+paste env_temp to `.env` file and add credentials


## Running the Docker container

* Use the command line to execute the docker compose file

    ```
    docker-compose config
    docker-compose up -d
    ```

* Create the executions table in the postgres db

    ```
    python3 scripts/csv_to_sql.py
    ```

* Connect to the database from the command line

    ```
    psql postgres
    ```

* List all tables using the `\dt` meta-command and **make sure the deathrow table was created**

    ```
    postgres=# \dt
    ```

* Assuming everything's gone as expected, now you can run SQL queries in the command line! Try the statement below. 

    ```
    postgres=# SELECT "index", "Execution", "Date of Offence", "Last Name", "Age at Execution" FROM executions LIMIT 5;
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
    docker ps -a

    // stop (and remove) running container
    docker stop db
    docker rm db

    // (optional) free up space by removing any unused resources
    docker container prune
    ```