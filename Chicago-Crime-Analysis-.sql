create database if not exists chicago_crime;
use chicago_crime;

create table crimes (
    id int primary key,
    case_number varchar(20),
    date_occurred varchar(30),
    block varchar(100),
    iucr varchar(10),
    primary_type varchar(50),
    description varchar(100),
    location_description varchar(50),
    arrest varchar(10),
    domestic varchar(10),
    beat int,
    district int,
    ward int,
    community_area int,
    fbi_code varchar(10),
    x_coordinate double,
    y_coordinate double,
    year int,
    updated_on varchar(30),
    latitude double,
    longitude double,
    location varchar(50)
);
select count(*) from crimes;
select * from crimes limit 5;
select count(*) from crimes;

select primary_type, count(*) as total
from crimes
group by primary_type
order by total desc;

select year, count(*) as total
from crimes 
group by year
order by year desc;

select primary_type,
count(*) as total_crime,
sum(case when arrest = 'true' then 1 else 0 end) as arrests,
round(sum(case when arrest = 'true' then 1 else 0 end)/count(*) * 100, 1) as arrest_rate_pct
from crimes
group by primary_type
order by total_crime desc;

select hour(str_to_date(date_occurred, '%m/%d/%Y %h:%i:%s %p')) as hour_of_day,
count(*) as total
from crimes
group by hour_of_day
order by hour_of_day;

select district, 
count(*) as total 
from crimes
group by district
order by total desc
limit 5;
