INSERT INTO users(id,name,email)
VALUES 
     (1,'Jenia','asmalina@gmail.com'),
     (2,'Egor','kupreichik@gmail.com'),
     (3,'Mixail','mishka@gmail.com'),
     (4,'Kate','katuxnik@gmail.com'),
     (5,'Bob','bobrik@gmail.com'),
     (6,'Sabina','saba@gmail.com'),
     (7,'Nina','kulesh@gmail.com'),
     (8,'Alex','xolod@gmail.com'),
     (9,'Piter','parker@gmail.com')

INSERT INTO products(id,price,category)
VALUES 
   (1,250,'Moloko'),
   (2,1000,'Bread'),
   (3,560,'Meat'),
   (4,780,'Fruits'),
   (5,2000,'Vegetables'),
   (6,370,'Soda'),
   (7,500,'Chips'), 
   (8,1050,'Candy'),
   (9,100,'Matches')
   
INSERT INTO orders(id,user_id,total)
VALUES 
   (1,1,100),
   (2,2,50),
   (3,3,30),
   (4,4,70),
   (5,3,200),
   (6,6,60),
   (7,1,120), 
   (8,8,80),
   (9,2,150)
   
INSERT INTO order_items(id,product_id,order_id,price,quantity)
VALUES 
   (1,1,100,1,1),
   (2,2,50,2,3),
   (3,3,30,4,5),
   (4,4,70,7,20),
   (5,3,200,5,5),
   (6,6,60,),
   (7,1,120), 
   (8,8,80),
   (9,2,150) 
   
INSERT INTO order_items(id,product_id,order_id,price,quantity)
VALUES 
    (1,1,1,30,2),
    (2,2,1,20,2),
    (3,3,2,25,2),
    (4,4,3,15,2),
    (5,5,4,35,2),
    (6,6,5,50,4),
    (7,7,6,30,2),
    (8,8,7,40,3),
    (9,9,8,80,1),
    (10,10,9,75,2)
 
SELECT * FROM users;

SELECT * FROM products 
WHERE price  = 1000;

SELECT * FROM orders 
ORDER BY total;

SELECT * FROM users 
ORDER BY name ASC;

UPDATE products  
SET category ="Choclate"
WHERE id = 2;

DELETE FROM users 
WHERE id = 6;

SELECT 
users.name,
orders.total
FROM users 
INNER JOIN orders 
  ON users.id = orders.user_id;

SELECT users.name,orders.total
FROM users 
RIGHT JOIN orders 
  ON users.id = orders.user_id;

SELECT users.name,
orders.total
FROM users 
LEFT JOIN orders
  ON users.id = orders.user_id
  
SELECT users.name,
orders.total
FROM users 
FULL JOIN orders 
 ON users.id = orders.user_id
 
SELECT COUNT(*) FROM users;
SELECT SUM(total) FROM orders;
SELECT AVG(total) FROM orders;
SELECT MIN(total) FROM orders;
SELECT MAX(total) FROM orders;

SELECT user_id,COUNT(*) AS orders_count
FROM orders 
GROUP BY user_id;

SELECT price,COUNT(*) AS product_max
FROM products
GROUP BY price;

CREATE INDEX idx_users_name ON users(name)
CREATE INDEX idx_products_category ON products(category)




