drop table if exists bk.game_session_user_featres;

create table bk.game_session_user_featres(
    'game_session_user_featres_id' int not null,
    constraint 'game_session_round_id' foreign key (game_session_round_id) references bk.game_session_round,
    constraint 'game_session_user_id' foreign key (game_session_user_id) references bk.game_session_user,
    constraint 'features_id' foreign key (features_id) references bk.features,
    'opened_at' timestamp,
    'is_open' text not null
);