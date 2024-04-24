drop table if exists bk.message;

create table bk.message(
    'message_id' int not null,
    constraint 'game_session_id' foreign key(game_session_id) references bk.game_session,
    'from_user_id' text not null,
    'to_user_id' text,
    'content' text not null,
    'sys_created_at' timestamp
);