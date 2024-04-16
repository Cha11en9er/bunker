drop table if exists bk.features_relation;

create table bk.features_relation(
    constraint 'right_features_id' foreign key(features_id) references bk.features,
    constraint 'left_features_id' foreign key(features_id) references bk.features,
    'total_points' int not null
);