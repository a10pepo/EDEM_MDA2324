# This Spark deliverable processes UTMB (Ultra-Trail du Mont Blanc) datasets and ranks some results in different DFs, which are then inserted into a PostgrSQL database.
1.  Datasets (CSVs) for the past 5 editions.
2.  Each edition has two CSVs: one with basic info (Rank, athlete's surname/name and finish time) and another with extended info (Rank, team/club, gender, country, YOB)
3.  Spark: 
    1.  Joins each pair of datasets and then stacks all 5 resulting datasets into a full DF.
    2.  Creates 1 DF, which contains the top 3 athletes per gender and edition
    3.  Creates 1 DF per gender, which contains the top 1 athletes in the past 5 editions. 
    4.  Inserts the DFs into the PostgreSQL database using the PostgreSQL JDBC driver.
        1.  In order to successfully run the database data insertion, --jar parameter was entered in the execution command.
4. Enter 'docker-compose up --build -d' to bring the container up. It will execute unattendedly (via entrypoint.sh) and the result can be checked using DBeaver (or any other PostgreSQL viewer) using the following connection parameters:
   1. host: localhost
   2. database: postgres
   3. username: postgres
   4. pass: Welcome01
   5. port: 5432

Any question or doubt, ask Julián Merino (jumepe@edem.es)