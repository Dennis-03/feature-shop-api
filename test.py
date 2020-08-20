#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 

Course work: 

@author:

Source:
    
'''
import sqlite3
import random
from sqlite3 import Error
import datetime

import zenv
import db_con

database = zenv.DB_LOCATION



''' DB TEAM WORK STARTED '''


# def select_all_movies_1(conn):
#     cur = conn.cursor()
#     sql = ''' SELECT * FROM MOVIE '''

#     try:
#         cur.execute(sql)

#     except sqlite3.IntegrityError as sqle:
#         return("SQLite error : {0}".format(sqle))
    
#     rows = cur.fetchall()
#     print(rows)

''' SCHEMA STARTED '''


def create_fs_user_table_schema(conn):
    cur = conn.cursor()
    sql = ''' CREATE TABLE "fs_user" (
	"fsuid"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"user_name"	TEXT NOT NULL,
	"email"	TEXT NOT NULL UNIQUE,
	"password"	TEXT,
	"location"	TEXT,
	"country"	TEXT,
	"registered_at"	TEXT,
	"updated_at"	TEXT
); '''

    try:
        cur.execute(sql)

    except sqlite3.IntegrityError as sqle:
        return("SQLite error : {0}".format(sqle))
    
    print("fs_user table created successfully")


def create_fs_team_table_schema(conn):
    cur = conn.cursor()
    sql = ''' CREATE TABLE "fs_team" (
	"fsteamid"	INTEGER NOT NULL,
	"team_name"	TEXT NOT NULL UNIQUE,
	"added_at"	TEXT,
	"updated_at"	TEXT,
	PRIMARY KEY("fsteamid" AUTOINCREMENT)
    );  '''

    try:
        cur.execute(sql)

    except sqlite3.IntegrityError as sqle:
        return("SQLite error : {0}".format(sqle))
    
    print("fs_team table created successfully")
    
def create_fs_team_members_table_schema(conn):
    cur = conn.cursor()
    sql = ''' CREATE TABLE "fs_team_members" (
	"fstmid"	INTEGER NOT NULL,
	"team_id"	INTEGER NOT NULL,
	"member_id"	INTEGER NOT NULL,
	"added_at"	TEXT,
	PRIMARY KEY("fstmid" AUTOINCREMENT)
);
  '''

    try:
        cur.execute(sql)

    except sqlite3.IntegrityError as sqle:
        return("SQLite error : {0}".format(sqle))
    
    print("fs_team_members table created successfully")


def create_fs_feature_table_schema(conn):
    cur = conn.cursor()
    sql = ''' CREATE TABLE "fs_feature" (
	"fsfeatureid"	INTEGER NOT NULL,
	"title"	TEXT NOT NULL UNIQUE,
	"content"	TEXT NOT NULL,
	"created_by"	TEXT,
	"created_at"	TEXT,
	"updated_at"	TEXT,
	PRIMARY KEY("fsfeatureid" AUTOINCREMENT)
); '''

    try:
        cur.execute(sql)

    except sqlite3.IntegrityError as sqle:
        return("SQLite error : {0}".format(sqle))
    
    print("fs_feature table created successfully")

def create_fs_feature_holder_table_schema(conn):
    cur = conn.cursor()
    sql = ''' CREATE TABLE "fs_feature_holder" (
	"fsfhid"	INTEGER NOT NULL,
	"team_id"	INTEGER NOT NULL,
	"feature_id"	INTEGER NOT NULL,
	"added_at"	TEXT,
	"status"	TEXT,
	PRIMARY KEY("fsfhid" AUTOINCREMENT)
);
 '''

    try:
        cur.execute(sql)

    except sqlite3.IntegrityError as sqle:
        return("SQLite error : {0}".format(sqle))
    
    print("fs_feature_holder table created successfully")

def create_fs_tact_coins_table_schema(conn):
    cur = conn.cursor()
    sql = ''' CREATE TABLE "fs_tact_coins" (
	"fstcid"	INTEGER NOT NULL,
	"team_id"	INTEGER NOT NULL,
	"feature_id"	INTEGER NOT NULL,
	"feature_coins"	INTEGER NOT NULL,
	"status"	TEXT,
	PRIMARY KEY("fstcid" AUTOINCREMENT)
); '''
    
    try:
        cur.execute(sql)

    except sqlite3.IntegrityError as sqle:
        return("SQLite error : {0}".format(sqle))
    
    print("fs_tact_coins table created successfully")


'''SCHEMA ENDED '''

# def get_actor_id(conn, actor_name):
#     """
#     Query all rows in the MOVIE table
#     :param conn: the Connection object
#     :return:
#     """

#     sql = """
#     SELECT
# 	    PA.AID AS 'ARTIST_ID'
#     FROM PUBLIC_ARTIST PA
#     WHERE PA.ARTIST_NAME = :actor_name COLLATE NOCASE;
#     """

#     actor_obj = {
#         'actor_name': actor_name
#     }

#     cur = conn.cursor()
#     cur.execute(sql, actor_obj)

#     rows = cur.fetchall()

#     # print('rows count : '+str(len(rows)))

#     if(len(rows) <= 0):
#         print('No Data available')
#         return -1

#     for row in rows:
#         # print(row)

#         return row[0]

#     return -1

def insert_into_fs_user(conn,fs_user_obj):
   # print(artist_obj['name'])
    
    #id = get_actor_id(conn,artist_obj['name'])

    cur = conn.cursor()

    #artist_obj['id'] = id

    sql = ''' INSERT INTO fs_user (
		user_name,
		email,
		password,
		location,
		country,
		registered_at,
		updated_at)
              VALUES (
        :user_name,
		:email,
		:password,
		:location,
		:country,
		:registered_at,
		:updated_at) ''' 
    
    try:
        cur.execute(sql,fs_user_obj)

    except sqlite3.IntegrityError as sqle:
        return("SQLite error : {0}".format(sqle))
    
    print("fs_user Inserted successfully")

def insert_into_fs_team(conn,fs_team_obj):
   # print(artist_obj['name'])
    
    #id = get_actor_id(conn,artist_obj['name'])

    cur = conn.cursor()

    #artist_obj['id'] = id

    sql = ''' INSERT INTO fs_team (
		team_name,
		added_at,
		updated_at)
              VALUES (
        :team_name,
		:added_at,
		:updated_at) ''' 
    
    try:
        cur.execute(sql,fs_team_obj)

    except sqlite3.IntegrityError as sqle:
        return("SQLite error : {0}".format(sqle))
    
    print("fs_team Inserted successfully")


def insert_into_fs_team_members(conn,fs_team_members_obj):
   # print(artist_obj['name'])
    
    #id = get_actor_id(conn,artist_obj['name'])

    cur = conn.cursor()

    #artist_obj['id'] = id

    sql = ''' INSERT INTO fs_team_members (
		team_id,
		member_id,
		added_at)
              VALUES (
        :team_id,
		:member_id,
		:added_at) ''' 
    
    try:
        cur.execute(sql,fs_team_members_obj)

    except sqlite3.IntegrityError as sqle:
        return("SQLite error : {0}".format(sqle))
    
    print("fs_team_members Inserted successfully")

def insert_into_fs_feature(conn,fs_feature_obj):
   # print(artist_obj['name'])
    
    #id = get_actor_id(conn,artist_obj['name'])

    cur = conn.cursor()

    #artist_obj['id'] = id

    sql = ''' INSERT INTO fs_feature (
		title,
		content,
		created_by,
		created_at,
		updated_at)
        VALUES (
        :title,
		:content,
		:created_by,
		:created_at,
		:updated_at) ''' 
    
    try:
        cur.execute(sql,fs_feature_obj)

    except sqlite3.IntegrityError as sqle:
        return("SQLite error : {0}".format(sqle))
    
    print("fs_feature_holder Inserted successfully")

def insert_into_fs_feature_holder(conn,fs_feature_holder_obj):
   # print(artist_obj['name'])
    
    #id = get_actor_id(conn,artist_obj['name'])

    cur = conn.cursor()

    #artist_obj['id'] = id

    sql = ''' INSERT INTO fs_feature_holder (
		team_id,
		feature_id,
		added_at,
		status )
        VALUES (
        :team_id,
		:feature_id,
		:added_at,
		:status 
        ) ''' 
    
    try:
        cur.execute(sql,fs_feature_holder_obj)

    except sqlite3.IntegrityError as sqle:
        return("SQLite error : {0}".format(sqle))
    
    print("fs_feature_holder Inserted successfully")

def insert_into_fs_tact_coins(conn,fs_tact_coins_obj):
   # print(artist_obj['name'])
    
    #id = get_actor_id(conn,artist_obj['name'])

    cur = conn.cursor()

    #artist_obj['id'] = id

    sql = ''' INSERT INTO fs_tact_coins (
		team_id,
		feature_id,
		feature_coins,
		status )
        VALUES (
        :team_id,
		:feature_id,
		:feature_coins,
		:status 
        ) ''' 
    
    try:
        cur.execute(sql,fs_tact_coins_obj)

    except sqlite3.IntegrityError as sqle:
        return("SQLite error : {0}".format(sqle))
    
    print("fs_tact_coins Inserted successfully")


def get_tact_coins_collected_by_team_name(conn,team_name):
    
    # sql = """
    # SELECT
	#     PA.AID AS 'ARTIST_ID'
    # FROM PUBLIC_ARTIST PA
    # WHERE PA.ARTIST_NAME = :actor_name COLLATE NOCASE;
    # """
    
    sql = ''' select team_name,feature_coins from 
            (select fs_team.team_name, fs_tact_coins.feature_coins
            from fs_team inner join fs_tact_coins 
            on fs_team.fsteamid = fs_tact_coins.team_id 
            where fs_tact_coins.status = 'done') where team_name = :team_name;  '''
    
    team_obj = {
        'team_name': team_name
    }

    cur = conn.cursor()
    cur.execute(sql, team_obj)

    rows = cur.fetchall()

    # print('rows count : '+str(len(rows)))

    if(len(rows) <= 0):
        print('No Data available , May be Pending !!')
        return -1
    
    total_coins = 0

    print(rows)

    for row in rows:
        total_coins += row[1]

    return total_coins



def find_pending_coins_for_team(conn,team_name):
    
    # sql = """
    # SELECT
	#     PA.AID AS 'ARTIST_ID'
    # FROM PUBLIC_ARTIST PA
    # WHERE PA.ARTIST_NAME = :actor_name COLLATE NOCASE;
    # """
    
    sql = ''' select team_name,feature_coins from 
            (select fs_team.team_name, fs_tact_coins.feature_coins
            from fs_team inner join fs_tact_coins 
            on fs_team.fsteamid = fs_tact_coins.team_id 
            where fs_tact_coins.status = 'pending') where team_name = :team_name;  '''
    
    team_obj = {
        'team_name': team_name
    }

    cur = conn.cursor()
    cur.execute(sql, team_obj)

    rows = cur.fetchall()

    # print('rows count : '+str(len(rows)))

    if(len(rows) <= 0):
        print('No Data available , May be no Pending !!')
        return -1
    
    total_coins = 0

    print(rows)

    for row in rows:
        total_coins += row[1]

    return total_coins



# def insert_into_artist_score(conn,artist_obj):
#     print(artist_obj['name'])
#     id = get_actor_id(conn,artist_obj['name'])

#     cur = conn.cursor()

#     artist_obj['id'] = id

#     sql = ''' INSERT INTO ARTIST_SCORE (ARTIST_ID,YEAR,CRITIC_SCORE,AUDIENCE_SCORE,BOX_OFFICE_SCORE,USER_IP,USERID,UPDATED_AT) 
#               VALUES (:id,:year,:c_score,:a_score,:b_score,:user_ip,:user_id,:updated_at) ''' 
    
#     try:
#         cur.execute(sql,artist_obj)

#     except sqlite3.IntegrityError as sqle:
#         return("SQLite error : {0}".format(sqle))
    
#     print("AS Inserted successfully")

# def insert_into_public_artist(conn,public_artist_obj):
#     print(artist_obj['name'])
#     id = get_actor_id(conn,artist_obj['name'])

#     cur = conn.cursor()

#     artist_obj['id'] = id

#     sql = ''' INSERT INTO PUBLIC_ARTIST (ARTIST_NAME,ORIGINAL_NAME,DOB,LOCATION,COUNTRY,DESCRIPTION,PIC_LOCATION) 
#               VALUES (:name,:original-_name,:dob,:location,:country,:description,:pic_loc) ''' 
    
#     try:
#         cur.execute(sql,artist_obj)

#     except sqlite3.IntegrityError as sqle:
#         return("SQLite error : {0}".format(sqle))
    
#     print("AS Inserted successfully")



# ''' DB TEAM WORK ENDED '''


# def select_all(conn):
#     """
#     Query all rows in the MOVIE table
#     :param conn: the Connection object
#     :return:
#     """
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM MOVIE")

#     rows = cur.fetchall()

#     # return('rows count : '+str(len(rows)))

#     if(len(rows) <= 0):
#         return('No Data available')
#     return rows
#     # for row in rows:
#     #     print(row)


# def select_all_by_actor(conn, actor_name):
#     """
#     Query all rows in the MOVIE table
#     :param conn: the Connection object
#     :return:
#     """
#     cur = conn.cursor()
#     cur.execute(
#         "SELECT * FROM COARTIST_BUBBLE WHERE ARTIST_NAME LIKE '%"+actor_name+"%'")

#     rows = cur.fetchall()

#     #print('rows count : '+str(len(rows)))

#     if(len(rows) <= 0):
#         return('No Data available')

#     for row in rows:
#         return(row)


# def add_coartist_bubble(conn, bubble_obj):
#     """
#     Create a movie
#     :param task:
#     :return: task id
#     """

#     sql = ''' INSERT INTO COARTIST_BUBBLE (ARTIST_NAME, COARTIST_CATEGORY, COARTIST_NAME, BUBBLE_SCORE) 
#             VALUES (:artist_name, :coartist_category, :coartist_name, :bubble_score) '''
#     cur = conn.cursor()

#     lastrowid = -1
#     try:
#         cur.execute(sql, bubble_obj)

#         lastrowid = cur.lastrowid
#     except sqlite3.IntegrityError as sqle:
#         return("SQLite error : {0}".format(sqle))
#     finally:
#         conn.commit()

#     return lastrowid


# def update_movie(conn, bubble_obj):
#     """
#     Create a movie
#     :param movie object:
#     :return: None
#     """

#     sql = ''' UPDATE MOVIE
#     SET MOVIE_NAME = :new_name, 
#     STARRING = :starring,
#     RELEASE_DATE = :release_date 
#     WHERE MOVIE_NAME = :name '''
#     cur = conn.cursor()

#     try:
#         cur.execute(sql, bubble_obj)

#     except sqlite3.IntegrityError as sqle:
#         return("SQLite error : {0}".format(sqle))
#     finally:
#         conn.commit()

#     return('Updated')


# def delete_movie(conn, name):
#     """
#     Delete a movie
#     :param movie object:
#     :return: None
#     """

#     sql = ''' DELETE FROM MOVIE    
#     WHERE MOVIE_NAME = ?'''
#     cur = conn.cursor()

#     try:
#         cur.execute(sql, (name,))

#     except sqlite3.IntegrityError as sqle:
#         return("SQLite error : {0}".format(sqle))
#     finally:
#         conn.commit()

#     return('Deleted')


def main():

    # create a database connection
    conn = db_con.create_connection(database)

    with conn:
        team_name = input("Team_name: ")
        coins = get_tact_coins_collected_by_team_name(conn,team_name)
        # coins = find_pending_coins_for_team(conn,team_name)
        print(coins)
        #print("TEST-select all movies ")
        #select_all_movies_1(conn)
        
        # current_date = datetime.date.today()
        # date = current_date.strftime("%d-%m-%Y")

        # fs_user_obj = {
        
		# 'user_name' : 'Sameena' , 
		# 'email' : 'sameena23@gmail.com' ,
		# 'password': '124' ,
		# 'location' : 'Toronto',
		# 'country' : 'Cannada',
		# 'registered_at' : '13-08-2020',
		# 'updated_at' : '15-08-2020'
        # }
        # #print("Insert stmt test")
        # insert_into_fs_user(conn, fs_user_obj)


        # for i in range(6):
            
        #     team_name = input('team name : ')
        #     added_at = input('added at :')
        #     updated_at = input('updated at :')
        #     fs_team_obj = {
            
        #     'team_name' : team_name,
        #     'added_at' : added_at,
        #     'updated_at' : updated_at
        #     }
        #     #print("Insert stmt test")
        #     insert_into_fs_team(conn, fs_team_obj)

        # for i in range(6):
            
        #     team_id = input('team id : ')
        #     member_id = input('member id :')
        #     added_at = input('added at :')
        #     fs_team_members_obj = {
            
        #     'team_id' : team_id,
        #     'member_id' : member_id,
        #     'added_at' : added_at,
            
        #     }
        #     #print("Insert stmt test")
        #     insert_into_fs_team_members(conn, fs_team_members_obj)

        # for i in range(6):
            
        #     title = input('title : ')
        #     content = input('content :')
        #     created_by = input('created by:')
        #     created_at = input('created at :')
        #     updated_at = input('updated at:')
        #     fs_feature_obj = {
            
        #     'title' : title,
        #     'content' : content,
        #     'created_by' : created_by,
        #     'created_at' : created_at,
        #     'updated_at' : updated_at
            
        #     }
        #     #print("Insert stmt test")
        #     insert_into_fs_feature(conn, fs_feature_obj)
        # for i in range(6):
            
        #     team_id = input('team_id : ')
        #     feature_id = input('feature_id :')
        #     added_at = input('added_at:')
        #     status = input('status :')
            
        #     fs_feature_holder_obj = {
            
        #     'team_id' : team_id,
        #     'feature_id' : feature_id,
        #     'added_at' : added_at,
        #     'status' : status
            
        #     }
        #     #print("Insert stmt test")
        #     insert_into_fs_feature_holder(conn, fs_feature_holder_obj)
        # for i in range(6):
            
        #     team_id = input('team_id : ')
        #     feature_id = input('feature_id :')
        #     feature_coins = input('feature_coins:')
        #     status = input('status :')
            
        #     fs_tact_coins_obj = {
            
        #     'team_id' : team_id,
        #     'feature_id' : feature_id,
        #     'feature_coins' : feature_coins,
        #     'status' : status
            
        #     }
        #     #print("Insert stmt test")
        #     insert_into_fs_tact_coins(conn, fs_tact_coins_obj)
        
        # CREATE
        # :artist_name, :coartist_category, :coartist_name, :bubble_score
        #print('Create Coartist Bubble')
        #bubble_obj = { 'artist_name': 'Dhanush', 'coartist_category': 'actress', 'coartist_name': 'Kajal Agarwal','bubble_score': 70} 
        #'''result = add_coartist_bubble(conn, bubble_obj)
        #print(result)
        #print('---------------\n')

        # READ
        # print('Read Movie')
        # select_all(conn)
        # print('---------------\n')

        # READ by Name
        #print('Read Coartist Bubble by Name')
        #select_all_by_actor(conn, 'Dhanush')
        #print('---------------\n')

        # UPDATE
        # print('Update Movie')
        # city_new_obj = {
        #     'name' : 'Asuran',
        #     'new_name' : 'Asuran',
        #     'starring' : 'Dhanush, TeeJay, Ken Karunas',
        #     'release_date' : '4 Oct 2019'
        # }
        # update_movie(conn, city_new_obj)
        # print('---------------\n')

        # DELETE
        # print('Delete Movie')
        # delete_movie(conn, 'Kadal')
        # print('---------------\n') '''


if __name__ == '__main__':
    main()
