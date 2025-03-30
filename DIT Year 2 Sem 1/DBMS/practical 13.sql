insert into g231691N_booking
values ("H111", "G001", "2003-01-01","2003-01-03", 1001),
("H111", "G002", "2003-02-05","2003-02-07", 1001),
("H111", "G003", "2003-01-15","2003-01-17", 1003);

update g231691N_guest
set guest_addr = "Manchester"
where guest_name = "John Smith";

update 	g231691n_room
set price = price * 1.05;

alter table g231691n_hotel
add Phone varchar(12) null;

alter table g231691n_hotel
add HOTEL_MANAGER varchar(20) not null;

alter view Gx_HOTEL_GUEST as 
select h.Hotel_Name, g.Guest_Name, r.Room_Type, b.Date_From, datediff(b.date_to, b.date_from) as Booking_Duration
from g231691n_booking as b
inner join g231691n_guest as g
on b.guest_no = g.guest_no
inner join g231691n_hotel as h
on b.hotel_no = h.hotel_no
inner join g231691n_room as r
on b.room_no = r.room_no;

INSERT INTO g231691n_Guest VALUES ('G111', 'John Smith', 'London');
INSERT INTO g231691n_Guest VALUES ('G112', 'Mike Tan', 'London');
INSERT INTO g231691n_Guest VALUES ('G113', 'Alice', 'London');
INSERT INTO g231691n_Guest VALUES ('G114', 'Ben Wang', 'London');
INSERT INTO g231691n_Guest VALUES ('G115', 'Thomas', 'London');
INSERT INTO g231691n_Guest VALUES ('G116', 'Shirly', 'London');
INSERT INTO g231691n_Guest VALUES ('G117', 'Zoe ', 'London');


SELECT * from g231691n_guest as g
where Guest_Name = 'Shirly';

create index Gx_GUEST_NAME_231691N
on g231691N_guest(guest_name);


