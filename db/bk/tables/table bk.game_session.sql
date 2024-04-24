drop table if exists bk.game_session;

create table bk.game_session(
    'game_session_id' int not null,
    constraint 'created_by_user_id' foreign key(user) references bk.user,
    'current_status' text not null,
    'game_result' text not null,
    'sys_created_at' timestamp,
    'sys_closed_at' timestamp
);