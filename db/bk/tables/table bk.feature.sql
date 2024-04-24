drop table if exists bk.feature;

create table bk.feature(
    'feture_id' int not null,
    'feature_name' text not null,
    'path_picture' text not null,
    'is_good' text not null
);