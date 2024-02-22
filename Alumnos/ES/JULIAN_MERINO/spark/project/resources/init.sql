DROP TABLE IF EXISTS utmb_all;
DROP TABLE IF EXISTS Top3_byGender_byYear;
DROP TABLE IF EXISTS Top1_Male;
DROP TABLE IF EXISTS Top1_Female;

CREATE TABLE public.utmb_all (
    Rank int4 NULL,
    YearComp int4 NULL,
    TimeComplete varchar(50) NULL,
    Surname_Name varchar(50) NULL,
    Club varchar(50) NULL,
    Country varchar(50) NULL, 
    YOB int4 NULL, 
    Gender varchar(50) NULL
);

CREATE TABLE public.Top3_byGender_byYear (
    Rank int4 NULL,
    YearComp int4 NULL,
    TimeComplete varchar(50) NULL,
    Surname_Name varchar(50) NULL,
    Club varchar(50) NULL,
    Country varchar(50) NULL, 
    YOB int4 NULL, 
    Gender varchar(50) NULL,
    GenRank int4 NULL
);

CREATE TABLE public.Top1_Male (
    Rank int4 NULL,
    YearComp int4 NULL,
    TimeComplete varchar(50) NULL,
    Surname_Name varchar(50) NULL,
    Club varchar(50) NULL,
    Country varchar(50) NULL, 
    YOB int4 NULL, 
    Gender varchar(50) NULL,
    GenRank int4 NULL,
    WinnerRank int4 NULL
);

CREATE TABLE public.Top1_Female (
    Rank int4 NULL,
    YearComp int4 NULL,
    TimeComplete varchar(50) NULL,
    Surname_Name varchar(50) NULL,
    Club varchar(50) NULL,
    Country varchar(50) NULL, 
    YOB int4 NULL, 
    Gender varchar(50) NULL,
    GenRank int4 NULL,
    WinnerRank int4 NULL
);