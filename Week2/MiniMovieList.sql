DROP TABLE IF EXISTS movierating;

CREATE TABLE movierating 
(
  ID int NOT NULL AUTO_INCREMENT,
  title varchar(100) NOT NULL,
  releaseDate datetime NOT NULL,
  miniRate varchar(100) NOT NULL,
  review double NULL,
  imgurl  varchar(255) not null,
  
  PRIMARY KEY (ID)
);

insert into movierating (title, releaseDate, miniRate, review,imgurl) values('The Adventurers (2017)', '2017-08-18', 'Not Yet Rated',6.3,"https://upload.wikimedia.org/wikipedia/en/thumb/6/6f/TheAdventurers2017.jpg/220px-TheAdventurers2017.jpg");

insert into movierating (title, releaseDate, miniRate, review,imgurl) values('The Nut Job 2: Nutty by Nature', '2017-08-11',  'PG',4,"https://upload.wikimedia.org/wikipedia/en/thumb/c/cb/The_Nut_Job_2_poster.jpg/220px-The_Nut_Job_2_poster.jpg");

insert into movierating (title, releaseDate, miniRate, review,imgurl) values('A taxi driver(2017)', '2017-08-18', 'Not Yet Rated',7,"https://upload.wikimedia.org/wikipedia/en/thumb/2/23/A_Taxi_Driver.jpg/220px-A_Taxi_Driver.jpg");

insert into movierating (title, releaseDate, miniRate, review,imgurl) values('The Emoji Movie', '2017-08-18', 'Not Yet Rated',2,"https://upload.wikimedia.org/wikipedia/en/6/63/The_Emoji_Movie_film_poster.jpg");

insert into movierating (title, releaseDate, miniRate, review,imgurl) values('Lady Macbeth', '2017-07-14', 'R',4, "https://upload.wikimedia.org/wikipedia/en/3/3a/Lady_Macbeth_%28film%29.png");

insert into movierating (title, releaseDate, miniRate, review,imgurl) values('Transformers: The Last Knight', '2017-06-21', 'PG-13',2,"https://upload.wikimedia.org/wikipedia/en/2/26/Transformers_The_Last_Knight_poster.jpg");




select * from movierating
