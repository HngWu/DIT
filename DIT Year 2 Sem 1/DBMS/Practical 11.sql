-- 1(i)
select * from customer

-- 1(ii)
select count(*) as total from customer

-- 2(i)
select * from customer
inner join state
on state.state_code = customer.state_code
where state_name = "California"

-- 2(ii)
select count(*) from customer
inner join state
on state.state_code = customer.state_code
where state_name = "California"

-- 3(i)
select order_num,ship_charge from orders
inner join customer
on orders.customer_num = customer.customer_num

-- 3(ii)
select count(order_num), sum(ship_charge) from orders
inner join customer
on orders.customer_num = customer.customer_num
where concat(fname, " ", lname) = "Anthony Higgins"

-- 4(i)
select * from product

-- 4(ii)
select max(unit_price) from product

-- 5(i)
	select product.prod_num, unit_price from product
	inner join product_desc
	on product.prod_num = product_desc.prod_num
	where prod_desc = "running shoes"
    
-- 5(ii)
select count(product.prod_num), max(unit_price) , min(unit_price), avg(unit_price) from product
	inner join product_desc
	on product.prod_num = product_desc.prod_num
	where prod_desc = "running shoes"
    
-- 6(i)-(ii)-(iii)
select orders.customer_num, count(orders.customer_num), customer.fname, customer.lname from orders
inner join customer
on orders.customer_num = customer.customer_num
group by orders.customer_num
having count(orders.customer_num) > 1

-- 7(i)- (ii)
select order_num, count(item_num) from order_detail
group by order_num

-- 7(iii)
select order_num, count(item_num), sum(total_price) from order_detail
group by order_num
having count(item_num) > 3

-- 8
select * from product
where unit_price = (select max(unit_price) 
					from product)

-- 9
select fname, lname from customer
where customer.customer_num not in (select orders.customer_num from orders
group by orders.customer_num
having count(orders.customer_num) >= 1)

select * from order_detail
where order_num in (
select order_num from order_detail
group by order_num
having count(item_num) > 3)