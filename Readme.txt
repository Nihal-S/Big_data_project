load database_name/table_name.csvload as (car,mpg.....,hp);

select max(mpg) from cars/cars.csv where hp = 75;

delete database_name;



python 3 reducer.py<output_map.txt 75 1

python3 mapper.py<data/cars.csv car,mpg,hp cars hp



Year;Length;Title;Subject;Actor;Actress;Director;Popularity;Awards;*Image
INT;INT;STRING;CAT;CAT;CAT;CAT;INT;BOOL;STRING