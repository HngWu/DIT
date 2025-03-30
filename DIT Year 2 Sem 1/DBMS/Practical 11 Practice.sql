-- question 1(i)
select * from orders;

-- question 1(ii)
-- in ascending order of order_num

-- question 1(iii)
select * from orders
order by customer_num;

-- question 2(i)
select concat(fname, ' ', lname) as fullname, concat_ws(' ', address1, address2, city, state_code, zipcode) as full_address
from customer;

-- question 2(ii)
select distinct state_code from customer;
-- answer: CA, NJ, AZ, DE, FL, OK, MA, CO, NY

-- question 2(iii)
select concat(fname, ' ', lname) as fullname, concat_ws(' ', address1, address2, city, state_code, zipcode) as full_address
from customer
order by lname;

-- question 3(i)
select order_num, ship_charge, (ship_charge * 1.1) as new_ship_charge
from orders;

-- question 3(ii)
select order_num, ship_charge, round(ship_charge * 1.1) as new_ship_charge
from orders;

-- question 4(i)
select concat(fname, ' ', lname) as full_name 
from customer;

-- question 4(ii)
select substr(zipcode, 3,3) as zip
from customer;

-- question 5(i)
select concat(fname, ' ', lname) as fullname, concat_ws(' ', address1, address2, city, state_code, zipcode) as full_address
from customer
where state_code = 'AZ';

-- question 5(ii)
select * 
from orders
where paid_date is null;

-- question 5(iii)
select * 
from product
where suppl_code = 'HRO';

-- question 5(iv)
select prod_num, prod_desc
from product_desc
where prod_desc like '%tennis%';
-- or
select prod_num, prod_desc
from product_desc
where prod_desc regexp 'tennis';

-- question 5(v)
select suppl_code, suppl_name 
from supplier
where suppl_name like 'H%';
-- or
select suppl_code, suppl_name 
from supplier
where substr(suppl_name, 1, 1) = 'H';

-- question 6
select c.customer_num, fname, lname, order_num, order_date
from customer as c
inner join orders as o on c.customer_num = o.customer_num;
-- where fname = 'Anthony'; -- for finding the answer to the question below
-- What are the orders placed by customer 104 (Anthony Higgins) ?
-- ans: 1001, 1003, 1011, 1013

-- question 7
select o.order_num, order_date, prod_num, quantity
from orders as o 
inner join order_detail as od on o.order_num = od.order_num;
-- where o.order_num = 1022; -- for finding the answer to the question below
-- What are the products bought in order 1022 ?
-- ans: 309, 303, 6

-- question 8
select p.prod_num, prod_desc, p.suppl_code, suppl_name
from product as p
inner join prod_desc as pd on p.prod_num = pd.prod_num
inner join supplier as s on p.suppl_code = s.suppl_code;

-- question 9
select  concat_ws(' ', c1.fname, c1.lname) as Customer_Name, concat_ws(' ', c2.fname, c2.lname) as Referral
from customer as c1
inner join customer as c2 on c1.referred_by = c2.customer_num
order by concat_ws(' ', c1.fname, c1.lname);
-- Which customers are referred by customer 102 (Carole Sadler)?
-- ans: Jason Walack, Marvin Hanlon

-- question 10
select state_name, count(customer_num)
from state as s
left join customer as c on s.state_code = c.state_code
group by state_name;
-- Which are the state names starting with ‘A’ where there are no customers yet?
-- ans: Alaska, Alabama, Arkansas