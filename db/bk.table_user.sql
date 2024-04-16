drop table if exists bk.user;

create table bk.user(
    'user_id' int not null,
    'login' text not null,
    'password' text not null
);