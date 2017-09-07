#what is a database?

#Tabels
  Tables should store data related to one thing, such as customers
  If the database belongs to a larger entity, such as a business, thin it may store related data in separate tables
  For example: customers, items, purchases, stores, etc.

#Related data
  We can model these relationships between tabels and columns in database systems designed for it.
  There are other database systems which do not allow for relational data
  They have other advantages, such as increased speed or simpler scalability

#Scalability
  A database management system is installed and runs on a computer
  Application connect ot hat computer and ask it to retrieve data for them
  If there are too many requests for data, the computer can end up unable to cope with the load.
  Relational database management systems (RDBMSs) tend to not scale as well as non-relational database management systems
  Scalability is important becuase it enables the servers to serve more clients (applications)
  However, RDBMSs allow you to interact and retrieve data easily.
  For example, using the tables shown earlier, it is easy to get "revenue generated per customer" using an RDBMNS than a non-relational system.

## THE SELECT COMMAND
SELECT * FROM customers;

SELECT customers.first_name FROM customers;

## multiple queries separated by commas also using the alias command AS to rename the columns

SELECT customers.first_name AS "First Name", customers.last_name AS "Last Name" FROM customers;

## THE WHERE COMMAND
    # This will get any customer's from the customers table if they have the first name 'Rolf' 
 SELECT customers.first_name AS "First Name", customers.last_name AS "Last Name" FROM customers
 WHERE customers.first_name = 'Rolf';


## THE OR/AND COMMANDS

SELECT customers.first_name, customers.last_name FROM customers
WHERE customers.first_name = 'Rolf' OR customers.last_name = 'Watson';

## LIMITING - create a limit of the amount of rows to return
SELECT customers.first_name, customers.last_name FROM customers LIMIT 1;

## THE UPDATE COMMAND
UPDATE {tablename} SET {columnname and value} WHERE {filterparameter};

## THE DELETE COMMAND
DELETE FROM items WHERE id=4;

## THE LIKE COMMAND and also WILDCARDS
 The percent symbol is a wildcard or everything
 The underscore symbol is an arbitrary placeholder
// Gets any customers with a last name that has 5 letters and an o in the middle.
SELECT * FROM customers WHERE last_name LIKE '__o__'; 

// Gets any customers with a last name that has any number of letters and has a t in it.
// will return Smith and Scott.
SELECT * FROM customers WHERE last_name LIKE '%t_'; 


# WHAT IS A JOIN
JOINs are one of the key element of relational DBs
They allow us to retrieve data from multiple tables at once
Essential to relational data, as it lets us get data from various tabels.
JOINs are quick.
The most common JOINs are INNER JOIN, followed by LEFT JOIN.


JOINs are like sets
  Unordered groups of unique elements
  JOINs treat rows of data as if they were Sets

  INTERSECT
    Set intersection is the elements common to two sets

  INNER JOIN is akin to Set Intersection

  INNER JOIN selects rows from table1 and table2 where they match the selecting column

    SELECT * FROM customers 
    INNER JOIN purchases
    ON customers.id = purchases.customer_id;

  LEFT JOIN selects all rows from table1, on the left, the rows from table2, on the right, if they match
    SELECT * FROM customers
    LEFT JOIN purchases
    ON customers.id = purchases.customer_id;

  RIGHT JOIN selects all rows from table1, on the right, the rows from table2, on the left, if they match
    SELECT * FROM customers
    RIGHT JOIN purchases
    ON customers.id = purchases.customer_id;
  
  FULL JOIN selects all rows from both tables, matching them if there is a match on the selecting column
  Similar to a LEFT and a RIGHT JOIN
    SELECT * FROM customers
    FULL JOIN purchases
    ON customers.id = purchases.customer_id;

  PERFORMING MULTIPLE JOINS IS POSSIBLE!
    SELECT first_name, last_name FROM items
    INNER JOIN purchases
    ON items.id = purchases.item_id
    INNER JOIN customers ON purchases.customer_id = customers.id;





































