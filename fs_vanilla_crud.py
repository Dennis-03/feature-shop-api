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
import requests
import json

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

def isAdmin(conn,user_id):

    sql = ''' select fs_user.user_name from fs_user where fs_user.fsuid = :user_id and fs_user.user_role = 1 ; '''
    
    user_obj = {
        'user_id': user_id
    }

    cur = conn.cursor()
    cur.execute(sql, user_obj)

    rows = cur.fetchall()

    # print('rows count : '+str(len(rows)))

    if(len(rows) <= 0):
        print('Not a admin')
        return False
    
    return True


def update_user_to_admin(conn, user_id):
    sql = ''' select * from fs_user where fsuid = :user_id '''
    update_sql  = ''' update fs_user set user_role = 1 where fsuid = :user_id;'''

    user_obj = {
        'user_id' : user_id,
    }

    cur = conn.cursor()
    cur.execute(update_sql, user_obj)
    conn.commit()
    cur = conn.cursor()
    cur.execute(sql, user_obj)
    rows = cur.fetchall()
    return rows[0]






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
    sql = ''' SELECT fsfeatureid FROM fs_feature ORDER BY fsfeatureid DESC LIMIT 1; '''

    insert_sql = ''' INSERT INTO fs_feature (
		title,
		content,
		created_at,
		updated_at,
        coins,
        given_by)
        VALUES (
        :title,
		:content,
		:created_at,
		:updated_at,
        :coins,
        :given_by) ''' 
    
    try:
        cur.execute(insert_sql,fs_feature_obj)
        conn.commit()
        cur.execute(sql,fs_feature_obj)
        rows = cur.fetchall()



    except sqlite3.IntegrityError as sqle:
        return("SQLite error : {0}".format(sqle))
    
    print("fs_feature Inserted successfully")
    return rows[0][0]


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
        conn.commit()


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
    
    sql = ''' select fs_team.team_name as Team , fs_tact_coins.feature_coins as TotalAmount from fs_team 
              inner join fs_tact_coins on fs_team.fsteamid = fs_tact_coins.team_id 
              where fs_tact_coins.status = 'pending' and fs_team.team_name = :team_name and fs_tact_coins.feature_id IN 
              (select fs_feature_holder.feature_id from fs_feature_holder where fs_feature_holder.status = 'Completed');  '''
    
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


def find_max_coins_collected_in_week_by_team(conn,start_date,end_date):
    
    # sql = """
    # SELECT
	#     PA.AID AS 'ARTIST_ID'
    # FROM PUBLIC_ARTIST PA
    # WHERE PA.ARTIST_NAME = :actor_name COLLATE NOCASE;
    # """
    
    sql = ''' select team_id,sum(feature_coins) as fc from fs_tact_coins 
              inner join fs_feature on fsfeatureid = feature_id where updated_at between :start_date and :end_date and fs_tact_coins.status = 'done'
              group by team_id order by fc DESC; '''
    
    date_obj = {
        'start_date' : start_date ,
        'end_date' : end_date
    }

    cur = conn.cursor()
    cur.execute(sql, date_obj)

    rows = cur.fetchall()

    # print('rows count : '+str(len(rows)))

    if(len(rows) <= 0):
        print('No Data available , May be no Pending !!')
        return -1
    
    print(rows)
 
    res = []
    max_coins = rows[0][1]
    for row in rows:
        if row[1] == max_coins:
            team_id = row[0]
            team_name = get_team_name_by_id(conn,team_id)
            res.append(team_name)

    return res

def get_team_name_by_id(conn,team_id):

    cur = conn.cursor()

    sql = '''
          select team_name from fs_team where fsteamid = :team_id;
          '''
    id_obj = {
        'team_id' : team_id
    }

    cur.execute(sql, id_obj)

    rows = cur.fetchall()

    # print('rows count : '+str(len(rows)))

    if(len(rows) <= 0):
        print('No Data available')
        return -1
    
    return rows[0][0]


def get_number_of_features_in_period_of_time(conn,start_date,end_date):
    
    # sql = """
    # SELECT
	#     PA.AID AS 'ARTIST_ID'
    # FROM PUBLIC_ARTIST PA
    # WHERE PA.ARTIST_NAME = :actor_name COLLATE NOCASE;
    # """
    
    sql = ''' select count(fsfeatureid) as feature_count from fs_feature where created_at BETWEEN :start_date and :end_date '''
    
    date_obj = {
        'start_date' : start_date ,
        'end_date' : end_date
    }

    cur = conn.cursor()
    cur.execute(sql, date_obj)

    rows = cur.fetchall()

    # print('rows count : '+str(len(rows)))

    if(len(rows) <= 0):
        print('No Data available !!')
        return -1
    
    #print(rows[0][0])

    return rows[0][0]

def get_total_number_of_features(conn):
    sql = ''' select count(fsfeatureid) as feature_count from fs_feature'''
    

    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()

    # print('rows count : '+str(len(rows)))

    if(len(rows) <= 0):
        print('No Data available !!')
        return -1
    return rows[0][0]

def get_teams_of_a_user(conn,user_id):
    
    # sql = """
    # SELECT
	#     PA.AID AS 'ARTIST_ID'
    # FROM PUBLIC_ARTIST PA
    # WHERE PA.ARTIST_NAME = :actor_name COLLATE NOCASE;
    # """
    
    
    sql = ''' select fs_team.fsteamid, fs_team.team_name from fs_team inner join fs_team_members on fs_team.fsteamid = fs_team_members.team_id 
              where fs_team_members.member_id = :user_id  '''
    # sql = ''' select fs_team.team_name from fs_team inner join fs_team_members on fs_team.fsteamid = fs_team_members.team_id 
    #           where fs_team_members.member_id = (select fs_user.fsuid 
    #           from fs_user where fs_user.user_name = :user_name); '''          
    
    user_obj = {
        'user_id' : user_id
    }

    cur = conn.cursor()
    cur.execute(sql, user_obj)

    rows = cur.fetchall()

    # print('rows count : '+str(len(rows)))

    if(len(rows) <= 0):
        print('No Data available !!')
        return -1
    results = []
    for row in rows:
        result = {
            'team_id': row[0],
            'team_name': row[1]
        }
        results.append(result)
    return results

    #print(rows[0][0])

def get_number_of_features_completed_for_all_teams(conn):
    
    sql = ''' select team_name,count(feature_id) as feature_count from fs_team inner join 
              fs_feature_holder on fsteamid = team_id group by team_id having status = 'Completed'; '''
    
    cur = conn.cursor()
    cur.execute(sql)

    rows = cur.fetchall()

    if(len(rows) <= 0):
        print('No Data available !!')
        return -1

    return rows

def get_number_of_features_completed_by_team_name(conn,team_name):
    sql = ''' select count(fs_feature_holder.feature_id) as feature_count from fs_team inner join fs_feature_holder on fs_team.fsteamid = fs_feature_holder.team_id group by fs_feature_holder.team_id having fs_feature_holder.status = 'Completed' and fs_team.team_name = :team_name '''
    
    cur = conn.cursor()
    name_obj = {
        'team_name' : team_name
    }

    cur.execute(sql, name_obj)

    rows = cur.fetchall()

    # print('rows count : '+str(len(rows)))

    if(len(rows) <= 0):
        print('No Data available')
        return -1
    
    return rows[0][0]


def get_tact_coins_by_feature_name(conn,feature_name):
    sql = ''' select feature_coins from fs_tact_coins join fs_feature on fs_feature.fsfeatureid = fs_tact_coins.feature_id where title = :feature_name; '''
    
    cur = conn.cursor()
    feature_obj = {
        'feature_name' : feature_name
    }

    cur.execute(sql, feature_obj)
    rows = cur.fetchall()

    # print('rows count : '+str(len(rows)))

    if(len(rows) <= 0):
        print('No Data available')
        return -1
    
    return rows[0][0]
    


def get_members_of_team(conn,team_name):
    
    # sql = """
    # SELECT
	#     PA.AID AS 'ARTIST_ID'
    # FROM PUBLIC_ARTIST PA
    # WHERE PA.ARTIST_NAME = :actor_name COLLATE NOCASE;
    # """
    
    sql = ''' select fs_user.user_name from fs_user inner join fs_team_members on fs_user.fsuid = fs_team_members.member_id 
              where fs_team_members.team_id = (select fs_team.fsteamid from fs_team where fs_team.team_name = :team_name); '''
    
    team_obj = {
        'team_name' : team_name
    }

    cur = conn.cursor()
    cur.execute(sql, team_obj)

    rows = cur.fetchall()

    # print('rows count : '+str(len(rows)))

    if(len(rows) <= 0):
        print('No Data available')
        return -1
    
    #print(rows[0][0])
    #print('Inside Func : ',rows)
    return rows

# select fs_feature.fsfeatureid,fs_feature.title,fs_feature.status,fs_feature.created_at from fs_feature;

def get_all_features(conn):
    
    sql = ''' select fs_feature.fsfeatureid,fs_feature.title,fs_feature.status,fs_feature.created_at,fs_feature.content from fs_feature; '''

    cur = conn.cursor()
    cur.execute(sql)

    rows = cur.fetchall()

    if(len(rows) <= 0):
        print('No Data available')
        return -1

    results =[]
    for row in rows:
        result = {
            'fsfeatureid': row[0],
            'title': row[1],
            'status': row[2],
            'created_at': row[3],
            'content': row[4]
        }
        results.append(result)
    return results

def get_features_of_user(conn,user_id):
    
    sql = ''' select fs_feature.fsfeatureid, fs_feature.title, fs_feature_holder.status from fs_feature inner join 
              fs_feature_holder on fs_feature.fsfeatureid=fs_feature_holder.feature_id where 
              fs_feature.fsfeatureid in (select fs_feature_holder.feature_id from fs_feature_holder 
              where fs_feature_holder.team_id in (select fs_team_members.team_id from fs_team_members 
              where fs_team_members.member_id = :user_id)); '''

    user_obj = {
        'user_id' : user_id
    }

    cur = conn.cursor()
    cur.execute(sql, user_obj)

    rows = cur.fetchall()

    if(len(rows) <= 0):
        print('No Data available')
        return -1

    results =[]
    for row in rows:
        result = {
            'feature_id': row[0],
            'feature_title': row[1],
            'feature_status': row[2]
        }
        results.append(result)
    return results

def get_feature_details(conn,feature_id):
    user_sql = '''SELECT user_name from fs_user where fsuid=:user_id;'''
    sql = ''' select * FROM fs_feature where fsfeatureid = :feature_id; '''

    
    feature_obj = {
        'feature_id' : feature_id
    }
    cur = conn.cursor()
    cur.execute(sql, feature_obj)

    rows = cur.fetchall()
    user_obj = {
        'user_id' : rows[0][7]
    }

    if(len(rows) <= 0):
        print('No Data available')
        return -1

    cur = conn.cursor()
    cur.execute(user_sql, user_obj)
    user_name = cur.fetchall()
    user_name = user_name[0][0]

    if(len(rows) <= 0):
        print('No Data available')
        return -1

    results = []
    for row in rows:
        result = {
            'feature_id': row[0],
            'title': row[1],
            'content': row[2],
            'team_id': row[3],
            'created_at': row[4],
            'updated_at': row[5],
            'status': row[6],
            'given_by_user_id': row[7],
            'given_by_user_name':user_name,
            'coins': row[8]
        }
        results.append(result)
    return results

def get_user_details(conn,user_id):
    
    sql = ''' select fs_user.fsuid, fs_user.user_name, fs_user.email, fs_user.location, 
              fs_user.country, fs_user.registered_at, fs_user.updated_at, fs_user.user_role, fs_user.bio, fs_user.github_handle, fs_user.linkedin_handle 
              from fs_user where fs_user.fsuid = :user_id;  '''

    user_obj = {
        'user_id' : user_id
    }

    cur = conn.cursor()
    cur.execute(sql, user_obj)

    rows = cur.fetchall()

    if(len(rows) <= 0):
        print('No Data available')
        return -1

    results =[]
    for row in rows:
        # try:
        #     handle = row[9].split('/')
        #     handle = handle[-1]
        #     req = requests.get('https://github-turtle-score.herokuapp.com/api?gitlink={}'.format(handle))
        #     result = json.loads(req.content)
        #     git_score = result.get('git_turtle_score')
        #     req = requests.get('http://ml-score.herokuapp.com/api/{}'.format(handle))
        #     result = json.loads(req.content)
        #     ml_score = result.get('ML_Score')
        #     if(git_score == -1):
        #         git_score = 0
        #     if(ml_score == -1):
        #         ml_score = 0
        # except:
        #     git_score = 0
        #     ml_score = 0
        result = {
            'user_id': row[0],
            'user_name': row[1],
            'email': row[2],
            'location': row[3],
            'country': row[4],
            'registered_at': row[5],
            'updated_at': row[6],
            'user_role' : row[7],
            'bio' : row[8],
            'github_handle' : row[9],
            'linkedin_handle' : row[10]
        }
        results.append(result)
    return results

def get_feature_links(conn,feature_id):
    sql = ''' select primary_link,secondary_links from fs_feature_holder where feature_id = :feature_id '''

    feature_obj = {
        'feature_id' : feature_id
    }

    cur = conn.cursor()
    cur.execute(sql, feature_obj)

    rows = cur.fetchall()
    print("printing rows",rows)
    if(len(rows) <= 0):
        print('No Data available')
        return -1
    return rows

def update_feature_links(conn,feature_id,primary_link,secondary_links):
    sql = ''' select primary_link,secondary_links from fs_feature_holder where feature_id = :feature_id '''
    update_sql = ''' update fs_feature_holder set primary_link = :primary_link,secondary_links = :secondary_links where feature_id = :feature_id '''

    feature_obj = {
        'feature_id' : feature_id,
        'primary_link' : primary_link,
        'secondary_links' : secondary_links
    }

    cur = conn.cursor()
    cur.execute(update_sql, feature_obj)
    conn.commit()
    cur = conn.cursor()
    cur.execute(sql, feature_obj)
    rows = cur.fetchall()
    return rows[0]


def count_team_members(conn,team_id):

    sql = ''' select count(team_id) from fs_team_members where team_id = :team_id; '''

    team_obj = {
        'team_id' : team_id
    }

    cur = conn.cursor()
    cur.execute(sql, team_obj)

    rows = cur.fetchall()

    if(len(rows) <= 0):
        print('No Data available')
        return -1

    return rows[0][0]

def count_team_members(conn,team_id):

    sql = ''' select count(team_id) from fs_team_members where team_id = :team_id; '''

    team_obj = {
        'team_id' : team_id
    }

    cur = conn.cursor()
    cur.execute(sql, team_obj)

    rows = cur.fetchall()

    if(len(rows) <= 0):
        print('No Data available')
        return -1

    return rows[0][0]

def get_user_tactcoins(conn,user_id):
    
    teams = get_teams_of_a_user(conn,user_id)
    team_id_list = []
    for obj in teams:
        team_id_list.append(obj.get('team_id'))
    total_done = 0
    total_pending = 0
    overall_total = 0
    for team_id in team_id_list:
        count = count_team_members(conn,team_id)
        sql_done = ''' select sum(feature_coins)/:count from fs_tact_coins where status='done' and team_id=:team_id; '''
        sql_pending = ''' select sum(feature_coins)/:count from fs_tact_coins where status='pending' and team_id=:team_id; '''
        # sql = ''' select sum(fs_tact_coins.feature_coins) from fs_tact_coins where 
        #           fs_tact_coins.status='done' and fs_tact_coins.team_id in (select fs_team_members.team_id 
        #           from fs_team_members where fs_team_members.member_id = :user_id); '''

        team_obj = {
            'team_id' : team_id,
            'count' : count
        }

        cur = conn.cursor()
        cur.execute(sql_done, team_obj)

        rows = cur.fetchall()

        if(len(rows) <= 0):
            print('No Data available')
        else:
            if rows[0][0]:
                total_done+=rows[0][0]
            
        cur = conn.cursor()
        cur.execute(sql_pending, team_obj)

        rows = cur.fetchall()

        if(len(rows) <= 0):
            print('No Data available')
        else:
            if rows[0][0]:
                total_pending+=rows[0][0]
    overall_total = total_done + total_pending
    result = {
        'received_tact_coins': total_done,
        'pending_tact_coins': total_pending,
        'total_tact_coins': overall_total
    }
    return result

def get_user_tactcoins_history(conn,user_id):

    teams = get_teams_of_a_user(conn,user_id)
    team_id_list = []
    results =[]
    for obj in teams:
        team_id_list.append(obj.get('team_id'))
    for team_id in team_id_list:
        count = count_team_members(conn,team_id)
        sql = ''' select fs_tact_coins.feature_id, fs_feature.title, fs_tact_coins.feature_coins, 
                fs_tact_coins.feature_coins/:count, fs_tact_coins.status from fs_tact_coins inner join 
                fs_feature on fs_tact_coins.feature_id = fs_feature.fsfeatureid where 
                fs_tact_coins.team_id = :team_id; '''

        team_obj = {
            'team_id' : team_id,
            'count' : count
        }

        cur = conn.cursor()
        cur.execute(sql, team_obj)

        rows = cur.fetchall()

        if(len(rows) <= 0):
            print('No Data available')
            return -1

    
        for row in rows:
            result = {
                'feature_id': row[0],
                'title': row[1],
                'team_feature_coins': row[2],
                'user_share' : row[3],
                'team_members_count' : count,
                'status': row[4]
            }
            results.append(result)
    return results

def authenticate_user(conn, email, password):
    
    sql = ''' select fsuid,user_name,user_role from fs_user where email=:email and password=:password '''

    user_cred_obj = {
        'email' : email,
        'password' : password
    }

    cur = conn.cursor()
    cur.execute(sql, user_cred_obj)

    rows = cur.fetchall()

    if(len(rows) <= 0):
        print('Invalid credentials')
        return -1,None,None
    print(rows)
    return rows[0][0],rows[0][1],rows[0][2]

def insert_user(conn, username, email, password, location, country,bio):
    
    sql = ''' select * from fs_user where email=:email '''
    insert_sql  = ''' insert into fs_user(user_name,email,password, location, country,registered_at,updated_at,bio) 
                      values (:username,:email,:password,:location,:country,:registered_at,:updated_at,:bio)'''

    current_date = datetime.date.today()
    Date = current_date.strftime("%d-%m-%Y") 

    user_cred_obj = {
        'username' : username,
        'email' : email,
        'password' : password,
        'location' : location,
        'country' : country,
        'registered_at' : Date,
        'updated_at' : Date,
        'bio' : bio
    }

    cur = conn.cursor()
    cur.execute(sql, user_cred_obj)

    rows = cur.fetchall()

    if(len(rows) <= 0):
        cur = conn.cursor()
        cur.execute(insert_sql, user_cred_obj)
        conn.commit()
        cur = conn.cursor()
        cur.execute(sql, user_cred_obj)
        rows = cur.fetchall()
        return rows[0]
    else:
        print('Email already exists')
        return -1

def add_tactcoins(conn, team_id, tactcoins, feature_id, comments):
    
    sql = ''' select * from fs_tact_coins where feature_id=:feature_id '''
    insert_sql  = ''' insert into fs_tact_coins(team_id, feature_id, feature_coins, status, comments) 
               values (:team_id,:feature_id,:feature_coins,:status,:comments)'''

    tactcoins_obj = {
        'team_id' : team_id,
        'feature_id' : feature_id,
        'feature_coins' : tactcoins,
        'status' : 'pending',
        'comments' : comments
    }

    cur = conn.cursor()
    cur.execute(insert_sql, tactcoins_obj)
    conn.commit()
    cur = conn.cursor()
    cur.execute(sql, tactcoins_obj)
    rows = cur.fetchall()
    return rows[0]

def update_user_handle(conn, user_id, github_handle, linkedin_handle):
    
    sql = ''' select * from fs_user where fsuid=:user_id '''
    update_sql  = ''' update fs_user set github_handle = :github_handle , linkedin_handle = :linkedin_handle where fsuid = :user_id;'''

    user_handle_obj = {
        'user_id' : user_id,
        'github_handle' : github_handle,
        'linkedin_handle' : linkedin_handle
    }

    cur = conn.cursor()
    cur.execute(update_sql, user_handle_obj)
    conn.commit()
    cur = conn.cursor()
    cur.execute(sql, user_handle_obj)
    rows = cur.fetchall()
    return rows[0]
    
def update_user_bio(conn, user_id, bio):
    
    sql = ''' select * from fs_user where fsuid=:user_id '''
    update_sql  = ''' update fs_user set bio = :bio where fsuid = :user_id;'''

    user_bio_obj = {
        'user_id' : user_id,
        'bio' : bio
    }

    cur = conn.cursor()
    cur.execute(update_sql, user_bio_obj)
    conn.commit()
    cur = conn.cursor()
    cur.execute(sql, user_bio_obj)
    rows = cur.fetchall()
    return rows[0]

def update_feature_progress(conn, feature_id, status):
    
    sql = ''' select * from fs_feature_holder where feature_id=:feature_id '''
    update_sql  = ''' update fs_feature_holder set status = :status where feature_id = :feature_id;'''

    feature_obj = {
        'feature_id' : feature_id,
        'status' : status
    }

    cur = conn.cursor()
    cur.execute(update_sql, feature_obj)
    conn.commit()
    cur = conn.cursor()
    cur.execute(sql, feature_obj)
    rows = cur.fetchall()
    return rows[0]

def update_feature_availability(conn, feature_id, status):
    
    sql = ''' select * from fs_feature where fsfeatureid=:feature_id '''
    update_sql  = ''' update fs_feature set status = :status where fsfeatureid = :feature_id;'''

    feature_obj = {
        'feature_id' : feature_id,
        'status' : status
    }

    cur = conn.cursor()
    cur.execute(update_sql, feature_obj)
    conn.commit()
    cur = conn.cursor()
    cur.execute(sql, feature_obj)
    rows = cur.fetchall()
    return rows[0]

def engage_feature(conn, feature_id, user_id):

    check_sql = ''' select * from fs_feature where fsfeatureid = :feature_id ''' 
    user_sql = ''' select team_id from fs_team_members where member_id = :user_id '''
    #update_sql  = ''' update fs_feature set status = 'Taken' where fsfeatureid = :feature_id and status = 'Available';'''
    
    feature_obj = {
        'feature_id' : feature_id,
        'user_id': user_id
    }
    
    cur = conn.cursor()
    cur.execute(check_sql, feature_obj)
    rows = cur.fetchall()
    
    #stat = rows[0][6]
    #if stat == 'Available':

    
    cur = conn.cursor()
    print("printing rows ------>",rows)
    cur.execute(user_sql, feature_obj)
    # rows = cur.fetchall()
    team_id = rows[0][0]
    current_date = datetime.date.today()
    Date = current_date.strftime("%d-%m-%Y") 
    fs_feature_holder_obj = {
            
            'team_id' : team_id,
            'feature_id' : feature_id,
            'added_at' : Date,
            'status' : 'OnProcess'
            
            }


    # conn.commit()
    
    insert_into_fs_feature_holder(conn,fs_feature_holder_obj)

    # cur = conn.cursor()
    # cur.execute(check_sql, feature_obj)
    # rows = cur.fetchall()
    
    return rows


def update_feature_details(conn,feature_id,title,content,coins):
    content_update_sql = '''update fs_feature set title = :title,content = :content where fsfeatureid = :feature_id'''
    coins_update_sql = '''update fs_tact_coins set feature_coins = :coins where feature_id = :feature_id'''

    feature_obj = {
        'feature_id' : feature_id,
        'title' : title,
        'content' : content,
        'coins' : coins
    }

    cur = conn.cursor()
    cur.execute(content_update_sql, feature_obj)
    conn.commit()

    cur.execute(coins_update_sql, feature_obj)
    conn.commit()
    return feature_id

def get_all_features_by_admin(conn,user_id):

    sql = '''select fs_feature.fsfeatureid,fs_feature.title,fs_feature.status from fs_feature where fs_feature.given_by in (SELECT fs_user.user_name from fs_user where fs_user.fsuid = :user_id)'''

    user_obj = {
        'user_id' : user_id
    }

    cur = conn.cursor()
    cur.execute(sql,user_obj)
    rows = cur.fetchall()
    if(len(rows) <= 0):
        print('No Data available')
        return -1

    results = []
    for row in rows:
        result = {
            'feature_id': row[0],
            'title': row[1],
            'status' :row[2]
        }
        results.append(result)
    return results

# def update_user_handle(conn, user_id, github_handle, linkedin_handle):
    
#     sql = ''' select * from fs_user where fsuid=:user_id '''
#     update_sql  = ''' update fs_user set github_handle = :github_handle , linkedin_handle = :linkedin_handle where fsuid = :user_id;'''

#     user_handle_obj = {
#         'user_id' : user_id,
#         'github_handle' : github_handle,
#         'linkedin_handle' : linkedin_handle
#     }

#     cur = conn.cursor()
#     cur.execute(update_sql, user_handle_obj)
#     conn.commit()
#     cur = conn.cursor()
#     cur.execute(sql, user_handle_obj)
#     rows = cur.fetchall()
#     return rows[0]




def main():

    # create a database connection
    conn = db_con.create_connection(database)

    with conn:
        pass
        
        # user_name = input("User Name : ")
        # team_list = get_teams_of_a_user(conn,user_name)
        # print(team_list)
        #get_user_details(conn, 1)
        # team_name = input("Team Name : ")
        # member_list = get_members_of_team(conn,team_name)
        # print(member_list)

        # team_name = input("Team_name: ")
        # coins = get_tact_coins_collected_by_team_name(conn,team_name)
        # coins = find_pending_coins_for_team(conn,team_name)
        # print(coins)
        #print("TEST-select all movies ")
        #select_all_movies_1(conn)

        # start_date = input('Start Date : ')
        # end_date = input('End Date : ')
        # result = find_max_coins_collected_in_week_by_team(conn,start_date,end_date)
        # print('Teams which collected maximum coins in this week : ', result)

        # result = get_number_of_features_in_period_of_time(conn,start_date,end_date)
        # print('Number of features in a particular period of time : ',result)

        # result = get_total_number_of_features(conn)
        # print('Total number of features : ',result)

        # result = get_number_of_features_completed_for_all_teams(conn)
        # print('Total number of features : ',result)
        # team_name = input("Team name: ")

        # result = get_number_of_features_completed_by_team_name(conn, team_name)
        # print(result)

        # feature_name = input("Feature title: ")

        # result = get_team_name_by_feature_name(conn, feature_name)
        # print(result)

        # result = get_tact_coins_by_feature_name(conn, feature_name)
        # print(result)
        #start_date = input('Start Date : ')
        #end_date = input('End Date : ')
        # result = find_max_coins_collected_in_week_by_team(conn,start_date,end_date)
        # print('Teams which collected maximum coins in this week : ', result)

        #result = get_number_of_features_in_period_of_time(conn,start_date,end_date)
        #print('Number of features in a particular period of time : ',result)

        
        
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
        # # }
        # #print("Insert stmt test")
        # insert_into_fs_user(conn, fs_user_obj)

        # for i in range(6):

        #     user_name = input('user_name : ')
        #     email = input('email : ')
        #     password = input('password : ')
        #     location = input('location : ')
        #     country = input('country : ')
        #     registered_at = input('registered_at : ')
        #     updated_at = input('updated_at : ')
        #     fs_user_obj = {
            
        #     'user_name' : user_name , 
		#     'email' : email,
		#     'password':password ,
		#     'location' : location,
		#     'country' : country,
		#     'registered_at' : registered_at,
		#     'updated_at' : updated_at
        #     }
        #     #print("Insert stmt test")
        #     insert_into_fs_user(conn, fs_user_obj)


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
            # fs_feature_obj = {
            
            # 'title' : title,
            # 'content' : content,
            # 'created_by' : created_by,
            # 'created_at' : created_at,
            # 'updated_at' : updated_at
            
            # }
        #     #print("Insert stmt test")
        #     insert_into_fs_feature(conn, fs_feature_obj)
        # for i in range(6):
            
        #     team_id = input('team_id : ')
        #     feature_id = input('feature_id :')
        #     added_at = input('added_at:')
        #     status = input('status :')
            
            # fs_feature_holder_obj = {
            
            # 'team_id' : team_id,
            # 'feature_id' : feature_id,
            # 'added_at' : added_at,
            # 'status' : status
            
            # }
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
