drop table if exists bk.game_session_round;

create table bk.game_session_round(
    'game_session_round_id' int not null,
    constraint 'game_session_id' foreign key(game_session_id) references bk.game_session;
    'round_number' int not null,
    'started_at' timestamp,
    'closed_at' timestamp
);