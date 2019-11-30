load database_name/table_name.csv (car,mpg.....,hp);

select max(mpg) from cars/cars.csv where hp = 75;

delete database_name;

python3 mapper.py car,mpg,hp cars hp 
