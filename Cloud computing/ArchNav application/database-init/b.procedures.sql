Delimiter $$
create procedure archemy.insert_into_kad(
IN kad_name varchar(100), 
IN kad_link varchar(300),
IN kad_public_link varchar(300),
IN domain_id int(11), 
IN business_problem Integer,
OUT kad_id int(11))

BEGIN
insert into kads(kad_name,domain_id,kad_link,kad_link_public,RECURRING_BUS_PROBLEM_ID) 
values (kad_name,domain_id,kad_link,kad_public_link,business_problem);
select last_insert_id() into kad_id;
END $$
Delimiter ;

Delimiter $$
create procedure archemy.insert_into_kad_dim_area(
IN in_kad_id Integer, 
IN in_area_id Integer,
IN in_area_child_id Integer,
IN in_dimension_id Integer
)

BEGIN
insert into kad_dimensions_area(kad_id,dimension_id,area_id,area_parent_id) 
values (in_kad_id,in_dimension_id,in_area_child_id,in_area_id);
END $$
Delimiter ;

