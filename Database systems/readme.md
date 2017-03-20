# Database Systems

## Assignment 1
Design of an ER diagram according to provided specifications, using Visio 2010.

The resulting *VSD* file is [Assignment_1_ERDiagram.vsd](Assignment_1_ERDiagram.vsd)

It looks like the following:

![Assignment_1_ERDiagram.jpg](screenshots/Assignment_1_ERDiagram.jpg)

## Assignment 2
Design of a relational database diagram using Crow's feet notation from
a provided ER diagram (similar to assignment 1).

The resulting *VSD* file is [Assignment_2.vsd](Assignment_2.vsd)

It looks like the following:

![Assignment_2.jpg](screenshots/Assignment_2.jpg)

## Assignment 3
Design of a SQL script to create a database on Oracle and query results.

The database implemented follows the following diagram:

![Assignment_3.jpg](screenshots/Assignment_3.jpg)

The resulting *SQL* file is [Assignment_3.sql](Assignment_3.sql)

It looks like the following:

```sql
/* ... */

CREATE TABLE ANSWER01 AS
    SELECT DISTINCT p.LNUMBER AS PERSON_LNUMBER, p.NAME AS PERSON_NAME
    FROM PERSON p, LIBRARIAN l, PATRON q
    WHERE p.LNUMBER = l.LNUMBER and l.LNUMBER = q.LNUMBER
    ORDER BY p.LNUMBER ASC;
    
/* ... */
```

## Assignment 4