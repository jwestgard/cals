drop table if exists meals;
create table meals (
  id integer primary key autoincrement,
  title text not null,
  'text' text not null
);
