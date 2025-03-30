-- question 1
select concat(fname, ' ', lname) as Customer_Name, substr(zipcode, 3, 3) as zipcode
from customer
where state_code = 'CA' or
state_code = 'NJ' or
state_code = 'AZ'; -- 22 rows returned

-- question 2
select order_num, ship_charge, round(ship_charge * 0.9) as new_ship_charge
from orders; -- 23 rows returned

-- question 3
select order_num, customer_num, order_date, paid_date, datediff(paid_date, order_date) as date_span
from orders
where paid_date is not null; -- 17 rows returned

-- question 4
select c.customer_num, fname, lname, order_num, order_date
from customer as c
inner join orders as o on c.customer_num = o.customer_num
order by fname; -- 23 rows returned

-- question 5
select s.suppl_name, count(prod_num) as product_supplied
from supplier as s
inner join order_detail as o on s.suppl_code = o.suppl_code
where lead_time_in_days > 7
group by s.suppl_name; -- 4 rows returned

-- question 6
select c.customer_num, fname, lname, count(*)
from customer as c
inner join orders as o on c.customer_num = o.customer_num
where month(order_date) = 6 and year(order_date) = 1994
group by c.customer_num, fname, lname
having count(*) > 1 ; -- 2 rows returned

-- question 7
select prod_desc, suppl_name, count(*), sum(total_price)
from order_detail as o
inner join product_desc as p on o.prod_num = p.prod_num
inner join supplier as s on o.suppl_code = s.suppl_code
group by prod_desc, suppl_name; -- 39 rows returned

-- question 8
update product
set unit_price = unit_price * 1.2
where prod_num = 102 and suppl_code = 'HSK'; -- changed 2
 


