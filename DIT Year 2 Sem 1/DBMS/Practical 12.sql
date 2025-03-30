-- question 1(i)
select * 
from customer;

-- question 1(ii)
select count(*) as total_customers 
from customer;

-- question 2(i)
select * 
from customer
where state_code = 'CA';

-- question 2(ii)
select count(*) as total_customer 
from customer
where state_code = 'CA';

-- question 3(i)
select order_num, ship_charge
from orders as o
inner join customer as c on o.customer_num = c.customer_num
where concat_ws(' ', fname, lname) = 'Anthony Higgins';

-- question 3(ii)
select count(order_num) as total_orders, sum(ship_charge) as total_shipping_charge
from orders as o
inner join customer as c on o.customer_num = c.customer_num
where concat_ws(' ', fname, lname) = 'Anthony Higgins';

-- question 4(i)
select unit_price 
from product;

-- question 4(ii)
select max(unit_price) 
from product;

-- question 5(i)
select p.prod_num, p.unit_price 
from product as p
inner join product_desc as pd on p.prod_num = pd.prod_num
where prod_desc = 'running shoes';

-- question 5(ii)
select count(*) as different_kinds, max(p.unit_price) as most_expensive, min(p.unit_price) as least_expensive, round(avg(p.unit_price), 2) as average_price
from product as p
inner join product_desc as pd on p.prod_num = pd.prod_num
where prod_desc = 'running shoes';

-- question 6(i)
select c.customer_num, count(*) as total_orders
from customer as c
inner join orders as o on c.customer_num = o.customer_num
group by c.customer_num;

-- question 6(ii)
select c.customer_num, concat(fname, ' ', lname) as full_name, count(*) as total_orders
from customer as c
inner join orders as o on c.customer_num = o.customer_num
group by c.customer_num, full_name;

-- question 6(iii)
select c.customer_num, concat(fname, ' ', lname) as full_name, count(*) as total_orders
from customer as c
inner join orders as o on c.customer_num = o.customer_num
group by c.customer_num, full_name
having count(*) > 1;

-- question 7(i)
select order_num, count(item_num) as total_items
from order_detail
group by order_num;

-- question 7(ii)
select order_num, count(item_num) as total_items, sum(total_price) as total_price
from order_detail
group by order_num;

-- question 7(iii)
select order_num, count(item_num) as total_items, sum(total_price) as total_price
from order_detail
group by order_num
having total_items > 3;

-- question 8
select p.prod_num, p.suppl_code, p.unit_price, prod_desc
from product as p
inner join product_desc as pd on p.prod_num = pd.prod_num
where unit_price = 
(select max(unit_price) 
from product);
-- limit 1( optional ) ;

-- question 9
select fname, lname 
from customer
where customer_num not in 
(select c.customer_num as total_orders
from customer as c
inner join orders as o on c.customer_num = o.customer_num
group by c.customer_num);

-- question 10
select order_num, item_num, prod_num, quantity
from order_detail
where order_num in 
(select order_num
from order_detail
group by order_num
having count(item_num) > 3);







