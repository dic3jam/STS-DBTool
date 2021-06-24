# STS-DbTool

A GUI interface I am building for my internship at SuperThinSaws. STS-DbTool will provide an easy to use GUI to run custom queries on the STS database, as well as import new versions of the database.

They currently have the problem where their data is "locked" into a system called JobBoss E2. JobBoss is not friendly to people trying to get custom information out of the system. However you can download a gzip of your data in a .sql file. This application will accomplish 3 tasks:

1. push button pre-configured queries
2. custom query tool
3. import new database tool (unzips the gzip file, opens a database connection and uploads the new version of the database)

In iteration 1 all query results will export to .csv files

Iteration 2 will present the option to open the outputted file in Microsoft Excel