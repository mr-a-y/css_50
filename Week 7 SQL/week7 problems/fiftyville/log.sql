-- Keep a log of any SQL queries you execute as you solve the mystery.

CREATE TABLE crime_scene_reports (
    id INTEGER,
    year INTEGER,
    month INTEGER,
    day INTEGER,
    street TEXT,
    description TEXT,
    PRIMARY KEY(id)
);
CREATE TABLE interviews (
    id INTEGER,
    name TEXT,
    year INTEGER,
    month INTEGER,
    day INTEGER,
    transcript TEXT,
    PRIMARY KEY(id)
);
CREATE TABLE atm_transactions (
    id INTEGER,
    account_number INTEGER,
    year INTEGER,
    month INTEGER,
    day INTEGER,
    atm_location TEXT,
    transaction_type TEXT,
    amount INTEGER,
    PRIMARY KEY(id)
);
CREATE TABLE bank_accounts (
    account_number INTEGER,
    person_id INTEGER,
    creation_year INTEGER,
    FOREIGN KEY(person_id) REFERENCES people(id)
);
CREATE TABLE airports (
    id INTEGER,
    abbreviation TEXT,
    full_name TEXT,
    city TEXT,
    PRIMARY KEY(id)
);
CREATE TABLE flights (
    id INTEGER,
    origin_airport_id INTEGER,
    destination_airport_id INTEGER,
    year INTEGER,
    month INTEGER,
    day INTEGER,
    hour INTEGER,
    minute INTEGER,
    PRIMARY KEY(id),
    FOREIGN KEY(origin_airport_id) REFERENCES airports(id),
    FOREIGN KEY(destination_airport_id) REFERENCES airports(id)
);
CREATE TABLE passengers (
    flight_id INTEGER,
    passport_number INTEGER,
    seat TEXT,
    FOREIGN KEY(flight_id) REFERENCES flights(id)
);
CREATE TABLE phone_calls (
    id INTEGER,
    caller TEXT,
    receiver TEXT,
    year INTEGER,
    month INTEGER,
    day INTEGER,
    duration INTEGER,
    PRIMARY KEY(id)
);pe
CREATE TABLE people (
    id INTEGER,
    name TEXT,
    phone_number TEXT,
    passport_number INTEGER,
    license_plate TEXT,
    PRIMARY KEY(id)
);
CREATE TABLE bakery_security_logs (
    id INTEGER,
    year INTEGER,
    month INTEGER,
    day INTEGER,
    hour INTEGER,
    minute INTEGER,
    activity TEXT,
    license_plate TEXT,
    PRIMARY KEY(id)
);

there 5 reports on that day : SELECT COUNT(*) FROM crime_scene_reports WHERE year = 2024 AND day = 28 AND month = 7 ;
+----------+
| COUNT(*) |
+----------+
| 5        |
+----------+

SELECT COUNT(*) FROM crime_scene_reports WHERE year = 2024 AND day = 28 AND month = 7 ;

| 295 | 2024 | 7     | 28  | Humphrey Street | Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery. Interviews
                                                were conducted today with three witnesses who were present at the time –
                                                each of their interview transcripts mentions the bakery.

| Ruth    | Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery parking lot and drive away.
            If you have security footage from the bakery parking lot, you might want to look for cars that left the parking lot in that time frame.                                                          |

| Eugene  | I don't know the thief's name, but it was someone I recognized. Earlier this morning, before I arrived at Emmas
            bakery, I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money.                                                                                                 |

| Raymond | As the thief was leaving the bakery, they called someone who talked to them for less than a minute. In the call,
            I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow. The thief then
                asked the person on the other end of the phone to purchase the flight ticket.

** acomplice bout earliest ticket on july 29 2024
** call shorthen then a minute on july 28 2024 after 10:15 am
** crime happened between 10:15 am ans 16:36
** suspect withdreww money on atm on july 28 2024 on legget street
** suspect leaves 10 minute after crime

sqlite> SELECT * FROM  bakery_security_logs WHERE year = 2024 AND day = 28 AND month = 7 AND hour = 10  and activity = 'exit' ;
+-----+------+-------+-----+------+--------+----------+---------------+
| id  | year | month | day | hour | minute | activity | license_plate |
+-----+------+-------+-----+------+--------+----------+---------------+
| 260 | 2024 | 7     | 28  | 10   | 16     | exit     | 5P2BI95       |
| 261 | 2024 | 7     | 28  | 10   | 18     | exit     | 94KL13X       |
| 262 | 2024 | 7     | 28  | 10   | 18     | exit     | 6P58WS2       |
| 263 | 2024 | 7     | 28  | 10   | 19     | exit     | 4328GD8       |
| 264 | 2024 | 7     | 28  | 10   | 20     | exit     | G412CB7       |
| 265 | 2024 | 7     | 28  | 10   | 21     | exit     | L93JTIZ       |
| 266 | 2024 | 7     | 28  | 10   | 23     | exit     | 322W7JE       |
| 267 | 2024 | 7     | 28  | 10   | 23     | exit     | 0NTHK55       |
| 268 | 2024 | 7     | 28  | 10   | 35     | exit     | 1106N58       |
+-----+------+-------+-----+------+--------+----------+---------------+
sqlite>
sqlite> SELECT * FROM people  WHERE license_plate   IN (SELECT license_plate FROM  bakery_security_logs WHERE year = 2024 AND day = 28 AND month = 7 AND hour
 = 10  and activity = 'exit') ;
+--------+---------+----------------+-----------------+---------------+
|   id   |  name   |  phone_number  | passport_number | license_plate |
+--------+---------+----------------+-----------------+---------------+
| 221103 | Vanessa | (725) 555-4692 | 2963008352      | 5P2BI95       |
| 243696 | Barry   | (301) 555-4174 | 7526138472      | 6P58WS2       |
| 396669 | Iman    | (829) 555-5269 | 7049073643      | L93JTIZ       |
| 398010 | Sofia   | (130) 555-0289 | 1695452385      | G412CB7       |
| 449774 | Taylor  | (286) 555-6063 | 1988161715      | 1106N58       |
| 467400 | Luca    | (389) 555-5198 | 8496433585      | 4328GD8       |
| 514354 | Diana   | (770) 555-1861 | 3592750733      | 322W7JE       |
| 560886 | Kelsey  | (499) 555-9472 | 8294398571      | 0NTHK55       |
| 686048 | Bruce   | (367) 555-5533 | 5773159633      | 94KL13X       |
+--------+---------+----------------+-----------------+---------------+

SELECT * FROM people  WHERE license_plate   IN (SELECT license_plate FROM  bakery_security_logs WHERE year = 2024 AND day = 28 AND month = 7 AND hour = 10  and activity = 'exit' AND minute <= 25 AND minute >= 15) AND phone_number IN ( SELECT caller FROM phone_calls  WHERE year = 2024 AND day = 28 AND mont
h = 7 AND duration <= 60);
+--------+--------+----------------+-----------------+---------------+
|   id   |  name  |  phone_number  | passport_number | license_plate |
+--------+--------+----------------+-----------------+---------------+
| 398010 | Sofia  | (130) 555-0289 | 1695452385      | G412CB7       |
| 514354 | Diana  | (770) 555-1861 | 3592750733      | 322W7JE       |
| 560886 | Kelsey | (499) 555-9472 | 8294398571      | 0NTHK55       |
| 686048 | Bruce  | (367) 555-5533 | 5773159633      | 94KL13X       |
+--------+--------+----------------+-----------------+---------------+

SELECT * FROM passengers WHERE passport_number IN (SELECT passport_number FROM people  WHERE license_plate   IN (SELECT license_plate FROM bakery_security_logs WHERE year = 2024 AND day = 28 AND month = 7 AND hour = 10  and activity = 'exit' AND minute <= 25 AND minute >= 15) AND phone_number IN ( SELECT caller FROM phone_calls  WHERE year = 2024 AND day = 28 AND month = 7 AND duration <= 60));
+-----------+-----------------+------+
| flight_id | passport_number | seat |
+-----------+-----------------+------+
| 18        | 3592750733      | 4C   |
| 24        | 3592750733      | 2C   |
| 36        | 1695452385      | 3B   |
| 36        | 5773159633      | 4A   |
| 36        | 8294398571      | 6C   |
| 54        | 3592750733      | 6C   |
+-----------+-----------------+------+

SELECT * FROM flights WHERE year = 2024 AND month = 7 AND day = 29 AND id IN (SELECT flight_id FROM passengers WHERE passport_number IN (SELECT passport_number FROM people  WHERE license_plate   IN (SELECT license_plate FROM bakery_security_logs WHERE year = 2024 AND day = 28 AND month = 7 AND hour = 10  and activity = 'exit' AND minute <= 25 AND minute >= 15) AND phone_number IN ( SELECT caller FROM phone_calls  WHERE year = 2024 AND day = 28 AND month = 7 AND duration <= 60)));
+----+-------------------+------------------------+------+-------+-----+------+--------+
| id | origin_airport_id | destination_airport_id | year | month | day | hour | minute |
+----+-------------------+------------------------+------+-------+-----+------+--------+
| 18 | 8                 | 6                      | 2024 | 7     | 29  | 16   | 0      |
| 36 | 8                 | 4                      | 2024 | 7     | 29  | 8    | 20     |
+----+-------------------+------------------------+------+-------+-----+------+--------+

SELECT * FROM passengers WHERE passport_number IN (SELECT passport_number FROM people  WHERE license_plate   IN (SELECT license_plate FROM bakery_security_logs WHERE year = 2024 AND day = 28 AND month = 7 AND hour = 10  and activity = 'exit' AND minute <= 25 AND minute >= 15) AND phone_number IN ( SELECT
caller FROM phone_calls  WHERE year = 2024 AND day = 28 AND month = 7 AND duration <= 60)) AND flight_id = 36;
+-----------+-----------------+------+
| flight_id | passport_number | seat |
+-----------+-----------------+------+
| 36        | 1695452385      | 3B   |
| 36        | 5773159633      | 4A   |
| 36        | 8294398571      | 6C   |
+-----------+-----------------+------+

SELECT * FROM people WHERE passport_number IN (SELECT passport_number FROM passengers WHERE passport_number IN (SELECT passport_number FROM people  W
HERE license_plate   IN (SELECT license_plate FROM bakery_security_logs WHERE year = 2024 AND day = 28 AND month = 7 AND hour = 10  and activity = 'exit' AND
 minute <= 25 AND minute >= 15) AND phone_number IN ( SELECT caller FROM phone_calls  WHERE year = 2024 AND day = 28 AND month = 7 AND duration <= 60)) AND f
light_id = 36);
+--------+--------+----------------+-----------------+---------------+
|   id   |  name  |  phone_number  | passport_number | license_plate |
+--------+--------+----------------+-----------------+---------------+
| 398010 | Sofia  | (130) 555-0289 | 1695452385      | G412CB7       |
| 560886 | Kelsey | (499) 555-9472 | 8294398571      | 0NTHK55       |
| 686048 | Bruce  | (367) 555-5533 | 5773159633      | 94KL13X       |
+--------+--------+----------------+-----------------+---------------+

sqlite> SELECT * FROM atm_transactions  WHERE year = 2024 AND day = 28 AND month = 7 AND atm_location = 'Leggett Street' AND account_number IN (
   ...> SELECT account_number FROM bank_accounts WHERE person_id IN (
   ...> SELECT id FROM people WHERE passport_number IN (SELECT passport_number FROM passengers WHERE passport_number IN (SELECT passport_number FROM people  WHERE license_plate   IN (SELECT license_plate FROM bakery_security_logs WHERE year = 2024 AND day = 28 AND month = 7 AND hour = 10  and activity = 'exit' AND minute <= 25 AND minute >= 15) AND phone_number IN ( SELECT caller FROM phone_calls  WHERE year = 2024 AND day = 28 AND month = 7 AND duration <= 60)) AND flight_id = 36)));
+-----+----------------+------+-------+-----+----------------+------------------+--------+
| id  | account_number | year | month | day |  atm_location  | transaction_type | amount |
+-----+----------------+------+-------+-----+----------------+------------------+--------+
| 267 | 49610011       | 2024 | 7     | 28  | Leggett Street | withdraw         | 50     |
+-----+----------------+------+-------+-----+----------------+------------------+--------+

sqlite> SELECT * FROM people WHERE id IN (SELECT person_id FROM bank_accounts WHERE account_number = 49610011) ;
+--------+-------+----------------+-----------------+---------------+
|   id   | name  |  phone_number  | passport_number | license_plate |
+--------+-------+----------------+-----------------+---------------+
| 686048 | Bruce | (367) 555-5533 | 5773159633      | 94KL13X       | ---> thief
+--------+-------+----------------+-----------------+---------------+
sqlite>

sqlite> SELECT * FROM phone_calls WHERE  year = 2024 AND month = 7 AND day = 28 AND duration <= 60 AND caller = (SELECT phone_number FROM people WHERE id IN
(SELECT person_id FROM bank_accounts WHERE account_number = 49610011)) ;
+-----+----------------+----------------+------+-------+-----+----------+
| id  |     caller     |    receiver    | year | month | day | duration |
+-----+----------------+----------------+------+-------+-----+----------+
| 233 | (367) 555-5533 | (375) 555-8161 | 2024 | 7     | 28  | 45       |
+-----+----------------+----------------+------+-------+-----+----------+

sqlite> SELECT * FROM people WHERE phone_number ='(375) 555-8161';
+--------+-------+----------------+-----------------+---------------+
|   id   | name  |  phone_number  | passport_number | license_plate |
+--------+-------+----------------+-----------------+---------------+ --> accomplice
| 864400 | Robin | (375) 555-8161 | NULL            | 4V16VO0       |
+--------+-------+----------------+-----------------+---------------+

+----+--------------+-------------------+---------------+
| id | abbreviation |     full_name     |     city      |
+----+--------------+-------------------+---------------+
| 4  | LGA          | LaGuardia Airport | New York City | ----> Destination
+----+--------------+-------------------+---------------+
sqlite>


