drop table if exists bk.game_session_user;

create table bk.game_session(
    'game_session_user_id' int not null,
    constraint 'game_session_id' foreign key(game_session_id) references bk.game_session,
    constraint 'kicked_by_round' foreign key(game_session_round_id) references bk.game_session_round,
    constraint 'user_id' foreign key(user_id) references bk.user,
    'connected_at' timestamp,
    'user_score' int not null,
    'user_status' text not null
);