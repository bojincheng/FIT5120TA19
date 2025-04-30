CREATE TABLE drowning_injury(
    id SERIAL PRIMARY KEY,
    location VARCHAR(50),
    icd_10_am_code VARCHAR(10),
    age_0_4_cases INT,
    age_5_14_cases INT,
    age_15_24_cases INT,
    age_25_44_cases INT,
    age_45_64_cases INT,
    age_65_plus_cases INT,
    total_cases INT,
    age_0_4_rate DECIMAL(3,1),
    age_5_14_rate DECIMAL(3,1),
    age_15_24_rate DECIMAL(3,1),
    age_25_44_rate DECIMAL(3,1),
    age_45_64_rate DECIMAL(3,1),
    age_65_plus_rate DECIMAL(3,1),
    total_rate DECIMAL(3,1)
);

INSERT INTO drowning_injury (location, icd_10_am_code, age_0_4_cases, age_5_14_cases, age_15_24_cases, age_25_44_cases, age_45_64_cases, age_65_plus_cases, total_cases, age_0_4_rate, age_5_14_rate, age_15_24_rate, age_25_44_rate, age_45_64_rate, age_65_plus_rate, total_rate) VALUES
('Swimming pool', 'W67 & W68', 106, 38, 7, 5, 11, 8, 175, 7.0, 1.2, NULL, NULL, 0.2, NULL, 0.7),
('Bathtub', 'W65 & W66', 23, 1, 0, 0, 0, 0, 24, 1.5, NULL, 0.0, 0.0, 0.0, 0.0, 0.1),
('Other or unspecified', 'W73 & W74', 55, 20, 24, 20, 19, 22, 160, 3.6, 0.6, 0.8, 0.3, 0.3, 0.5, 0.6),
('Natural water', 'W69 & W70', 20, 18, 27, 46, 30, 15, 156, 1.3, 0.6, 0.9, 0.6, 0.5, 0.3, 0.6),
('Total', NULL, 204, 77, 58, 71, 60, 45, 515, 13.5, 2.4, 1.9, 1.0, 1.0, 1.0, 2.0);

CREATE TABLE drowning_deaths ( 
    id SERIAL PRIMARY KEY,
    location VARCHAR(50),
    icd_10_code VARCHAR(10),
    age_0_4_deaths INT,
    age_5_14_deaths INT,
    age_15_24_deaths INT,
    age_25_44_deaths INT,
    age_45_64_deaths INT,
    age_65_plus_deaths INT,
    total_deaths INT,
    age_0_4_rate DECIMAL(3,1),
    age_5_14_rate DECIMAL(3,1),
    age_15_24_rate DECIMAL(3,1),
    age_25_44_rate DECIMAL(3,1),
    age_45_64_rate DECIMAL(3,1),
    age_65_plus_rate DECIMAL(3,1),
    total_rate DECIMAL(3,1),
    male_rate DECIMAL(3,1) NULL,
    female_rate DECIMAL(3,1) NULL,
    persons_rate DECIMAL(3,1) NULL,
    total_persons_rate DECIMAL(3,1)
);

INSERT INTO drowning_deaths (
    location, icd_10_code, age_0_4_deaths, age_5_14_deaths, age_15_24_deaths, 
    age_25_44_deaths, age_45_64_deaths, age_65_plus_deaths, total_deaths, 
    age_0_4_rate, age_5_14_rate, age_15_24_rate, age_25_44_rate, age_45_64_rate, 
    age_65_plus_rate, total_rate, male_rate, female_rate, persons_rate, total_persons_rate
) VALUES
('Swimming pool', 'W67 & W68', 7, 3, 3, 6, 5, 9, 33, 0.5, 0.1, 0.1, 0.1, 0.1, 0.2, 0.1, 0.2, NULL, 0.1, 0.1),
('Natural water', 'W69 & W70', 6, 7, 21, 40, 32, 33, 139, 0.4, 0.2, 0.7, 0.6, 0.5, 0.8, 0.5, 0.9, NULL, 0.5, 0.5),
('Bathtub', 'W65 & W66', 1, 2, 1, 3, 3, 6, 16, 0.1, 0.1, 0.0, 0.0, 0.0, 0.1, 0.1, NULL, NULL, NULL, 0.1),
('Other or unspecified', 'W73 & W74', 2, 0, 0, 6, 6, 9, 23, 0.1, 0.0, 0.0, 0.1, 0.1, 0.2, 0.1, NULL, NULL, 0.1, 0.1),
('Elsewhere classified', 'T75.1', 2, 0, 5, 15, 20, 19, 61, 0.1, 0.0, 0.2, 0.2, 0.3, 0.5, 0.2, 0.4, NULL, 0.2, 0.2),
('Total', 'Total', 18, 12, 30, 70, 66, 76, 272, 1.2, 0.4, 0.9, 1.0, 1.1, 1.8, 1.1, 1.6, 0.4, 1.0, 1.0);
