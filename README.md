# DBexport.py

script reads from mysql db and outputs with custom formating to unload.txt

## Setup

`pip install mysql-connector-python`

## run

USE python3!

`python3 DBexport.py`

## MYSQL Schema

```
mysql> INSERT INTO Properties (id, name, title, description) VALUES (2, 'haus2', '2.5 zimmer wohnung', 'mit waschturm und seperatem eingang!')
    -> ;
Query OK, 1 row affected (0.03 sec)

mysql> SELECT * FROM Properties;
+------+-------+--------------------+--------------------------------------+
| id   | name  | title              | description                          |
+------+-------+--------------------+--------------------------------------+
|    1 | haus1 | schönes haus       | what a view!                         |
|    2 | haus2 | 2.5 zimmer wohnung | mit waschturm und seperatem eingang! |
+------+-------+--------------------+--------------------------------------+
2 rows in set (0.00 sec)

mysql> D
```
