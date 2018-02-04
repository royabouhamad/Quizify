drop table if exists questions;
create table questions(
  id integer primary key autoincrement,
  question text not null,
  option_A text not null,
  option_B text not null,
  option_C text not null,
  option_D text not null,
  answer text not null
);
