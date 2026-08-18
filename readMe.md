*Ecommerce web application*
-> aimed at connecting sellers who heavily rely on social media applications like tiktok and instagram 
-> these sellers use these applications as their primary mode of accessing customers yet those applications dont come with tools that actually help with improving their sales, data analytics and  it is also only limited to people who only use the said application

*ecommerce entities*
    1.users -> id, email, password
    2.employees -> id, user_id,full_name,address,id_no,phone_number,role
    3.customers -> id, user_id,full_name,address,phone_number
    4.orders -> id, customer_id, employee_id,shipper_id, time_stamp
    5.orderdetails ->id, order_id, product_id,quantity 
    6.payments -> id, order_id,  payment_method, amount,status, date_of_payment
    7.shippers -> id, employee_id, time_of_activity
    8.cartegories -> id,brand_id,cartegory_name,description
    9.products -> id, cartegory_id, supplier_id, product_name, brand, unit, buying_price, selling_price,
    10.suppliers -> id,supplier_name,address,phone_number,city





**urban hotel entites**
    1.user(id, email, password)   
    2. customer(id, user_id, name, email, phone_no, address)              
    3. staff(id, user_id, name, email, phone_no, role)
    4. menu_cartegory(id, name, description)
    5. menu_item(id,m_cat_id,name,desc,price)
    6. order(id,customer_id,time_stamp)
    7. order_details(id, order_id, menu_item, quantity)
    8. payment(id, order_id, payment_method, amount,status, time_stamp)
    9. delivery(id, staff_id, order_id, status)
    10. review(id, customer_id, order_id, comment)