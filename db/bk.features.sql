drop table if exists bk.features;

create table bk.features(
    'fetures_id' int not null,
    'features_name' text not null,
    'path_picture' text not null,
    'is_good' text not null
);