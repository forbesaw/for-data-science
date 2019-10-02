While SQL does not need to be formatted for it to run, we need other people to read it. Consistency is key for this to work and these conventions are designed to be readable & simple to execute. Consider these strong guidelines so that we all can read each others’ queries.

TODO: format this page and scrape 

Conventions
Capitalize SQL Keywords; everything else should be lowercase
Aliasing & naming 
To name an expression or subquery use AS
To name a table do NOT use AS  
Table alias may be short, but should suggest the original table; avoid single letter names if they are ambiguous or unclear. E.g., mongodb.users u (GOOD) vs mongodb.users t1 (BAD)
Reference source table if there is more than one source
Prefix notation whenever possible
Including commas:

, source_table.source_column1 AS col_alias1
, source_table.source_column2 AS col_alias2
instead of

source_table.source_column1 AS col_alias1,
source_table.source_column2 AS col_alias2,


Modularize judiciously (WITH statements vs SUBQUERIES) 
Use WITH statements for complex queries; for simple queries use SUBQUERIES to avoid indirection
Definitely use a WITH if you’re referencing the subquery more than once
Probably use a WITH if you have multiple nested statements
Remember a WITH statement creates a VIEW and may represent a query optimization barrier 
Prefix notation is still valid, use a comma before the alias to make it easy to comment out WITH statement:

)
, CTE_QUERY AS (
  ...


Whitespace 
2 space indents 
NO hanging indents:

this_is_not(
  a_hanging
  , expression
)
instead of

this_is_a(
  hanging
  , expression)


Open parenthesis immediately after function:

func(
  ...
)
instead of

func 
( 
  ...
)


General Query Structure 
This should be the general structure of your queries:

SELECT
  a.foo
  , b.bar AS baz
FROM a
JOIN b 
ON 
  a.bing = b.bong
  AND ...  
WHERE 
  1 = 1 
  AND ...   
GROUP BY 
  a.lorem
  , b.ipsum  
ORDER BY ...  
LIMIT 10
Note that this structure is similar to a set of “function calls” with arguments:

func(
  arg1
  , arg2
)
Collapsed Query Structure
Optionally, if there are VERY FEW (one) “argument” in these clauses, you may abbreviate them like so:

SELECT my_table.foo
FROM my_table
JOIN other_table 
ON my_table.bing = other_table.bong
WHERE my_table.baz = other_table.buzz    
GROUP BY my_table.lorem  
ORDER BY ...  
LIMIT 10
Subqueries
Use subqueries to isolate data & logic pulled from specific sources. Name your subqueries in an explanatory fashion. Good practice is to add a comment explaining the subquery when the name is not sufficient:

SELECT
  foo
  , bar AS baz
FROM my_table
JOIN (
  -- note the recursive structure here 
  SELECT
    i 
    , like_turtles
  FROM turtles 
  WHERE is_cute
) AS cute_turtles 
ON 
  my_table_or_subquery.bing = cute_turtles.bong
  AND ...  
...
Nested Expressions
Use non-hanging indents to add nested expressions:

WHERE 
  1 = 1 
  AND (
    turtle = frog 
    OR tadpole = butterfly
  )  
CASE Statements
The common CASE expression should be split into clauses using the same clause logic as above:

CASE
  WHEN 
    1=1
    OR 2=2 
  THEN 2
  ELSE 4
END
Collapsed Case
If each clause fits on one short line (usually just one argument), the CASE may be collapsed:

CASE WHEN 1=1 THEN 2 ELSE 3 END 
GROUP BY Numeric Arguments
GROUP BY accepts positional arguments. If you are using ONLY positional arguments, collapse them onto one line:

GROUP BY 1
or

GROUP BY 
  1, 2, 3, 4 
Grouping and Query Grains
Aggregate sooner, join later 

This is a query smell:

...
GROUP BY 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17
It means that the tables you are joining do not have the same grain (level of aggregation) and you are generating potentially huge intermediate data, which makes your query slower and may result in a failure. Additionally, this type of queries hide duplicates very well, because you cannot know whether all the values you are pulling from intermediate tables can be collapsed.

Please make sure joins are clean by pre-aggregating tables to a common grain. E.g, when the final table is at a user and date level, pre-group all the joins to also be at the user and date level (instead of doing the grouping at the end):

SELECT
  x_data.id
  , x_data.date
  , x_data.max_of_x
  , y_data.max_of_y
FROM (
  SELECT
    a.id
    , b.date
    , MAX(x) AS max_of_x
  FROM …
  GROUP BY 1, 2
) AS x_data
LEFT JOIN (
  SELECT
    c.id
    , d.date
    , MAX(y) AS max_of_y
  FROM …
  GROUP BY 1, 2
) AS y_data
ON
  x_data.id = y_data.id
  AND x_data.date = y_data.date
Rules:

No GROUP BY at the final query level (after any subqueries or WITH statements)
All joins should be 1:1 for INNER JOINS, or 1:1 or 1:0 FOR LEFT JOINS.
Join sequences matter. Pay extra attention to join sequence and evaluate if a full join is needed.
Comments
Single line:

-- this is a single line comment 
Multi-line:

/*
  This is a 
  long 
  multiline 
  comment 
*/
Naming Conventions
Commonly used fields should be named similarly 

Dates
Use ds (short for datestamp) 
Avoid dt (ambiguous for datetimes) 
Timestamps:
Use ts (short for timestamp) 
