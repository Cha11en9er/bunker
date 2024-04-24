drop table if exists bk.game_session_vote;

create table bk.game_session_vote(
    'game_session_vote_id' int not null,
    constraint 'game_session_round_id' foreign key (game_session_round_id) references bk.game_session_round,
    'vote_from_user_id' int not null,
    'vote to user_id' int not null
);