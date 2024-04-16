drop table if exists bk.message;

create table bk.message(
    'message_id' int not null,
    constraint 'game_session_id' foreign key(game_session_id) references bk.game_session,

);