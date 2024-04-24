drop table if exists bk.feature_relation;

create table bk.feature_relation(
    constraint 'right_feature_id' foreign key(feature_id) references bk.feature,
    constraint 'left_feature_id' foreign key(feature_id) references bk.feature,
    'total_points' int not null
);