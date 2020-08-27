from flask import Flask, jsonify, request, make_response

import fs_vanilla_crud as fvc

# import sqlite3
# from sqlite3 import Error

import zenv
import db_con

database = zenv.DB_LOCATION

app = Flask(__name__)


def get_db_conn():

    conn = db_con.create_connection(database)
    return conn




'''
http://127.0.0.1:5000/api/get-teams-of-member/2

'''

@app.route("/api/get-teams-of-member/<user_id>", methods=['GET'])
def get_teams_of_member(user_id):
    # result = bc.select_all(get_db())
    conn = get_db_conn()
    result = fvc.get_teams_of_a_user(conn,user_id)

    res = {
        "member_id": user_id,
        "teams": result
    }
    
    print("Inside Route : ",result)


    return make_response(jsonify(res), 200)


'''
http://127.0.0.1:5000/api/get-all-features

'''

@app.route("/api/get-all-features", methods=['GET'])
def get_all_features_from_db():
    # result = bc.select_all(get_db())
    conn = get_db_conn()
    result = fvc.get_all_features(conn)

    res = {
        "features": result
    }
    
    print("Inside Route : ",result)


    return make_response(jsonify(res), 200)


'''
http://127.0.0.1:5000/api/get-features-of-user/2

'''

@app.route("/api/get-features-of-user/<user_id>", methods=['GET'])
def get_features_of_user(user_id):
    # result = bc.select_all(get_db())
    conn = get_db_conn()
    result = fvc.get_features_of_user(conn,user_id)

    res = {
        "features": result
    }
    
    print("Inside Route : ",result)


    return make_response(jsonify(res), 200)

'''
http://127.0.0.1:5000/api/login

'''

@app.route("/api/login", methods=['POST'])
def login():
    # result = bc.select_all(get_db())
    email = request.json['email']
    password = request.json['password']
    conn = get_db_conn()
    user_id, user_name = fvc.authenticate_user(conn, email, password)

    if(user_id == -1):
        authenticated = 'Invalid Credentials'
    else:
        authenticated = 'Authentication successful'
        
    res = {
        "user_name": user_name,
        "user_id": user_id,
        "authenticated": authenticated
    }
    
    print("Inside Route : ",res)


    return make_response(jsonify(res), 200)

'''
http://127.0.0.1:5000/api/get-feature-details/2

'''
@app.route("/api/get-feature-details/<feature_id>", methods=['GET'])
def get_feature_details(feature_id):
    # result = bc.select_all(get_db())
    conn = get_db_conn()
    result = fvc.get_feature_details(conn,feature_id)

    res = {
        "feature_details": result
    }
    
    print("Inside Route : ",result)


    return make_response(jsonify(res), 200)

'''
http://127.0.0.1:5000/api/get-user-details/2

'''
@app.route("/api/get-user-details/<user_id>", methods=['GET'])
def get_user_details(user_id):
    # result = bc.select_all(get_db())
    conn = get_db_conn()
    result = fvc.get_user_details(conn,user_id)

    res = {
        "user_details": result
    }
    
    print("Inside Route : ",result)


    return make_response(jsonify(res), 200)

'''
http://127.0.0.1:5000/api/get-user-tactcoins/2

'''
@app.route("/api/get-user-tactcoins/<user_id>", methods=['GET'])
def get_user_tactcoins(user_id):
    # result = bc.select_all(get_db())
    conn = get_db_conn()
    result = fvc.get_user_tactcoins(conn,user_id)

    res = {
        "user_id": user_id,
        "user_tactcoins": result
    }
    
    print("Inside Route : ",result)


    return make_response(jsonify(res), 200)

'''
http://127.0.0.1:5000/api/get-user-tactcoins-history/2

'''
@app.route("/api/get-user-tactcoins-history/<user_id>", methods=['GET'])
def get_user_tactcoins_history(user_id):
    # result = bc.select_all(get_db())
    conn = get_db_conn()
    result = fvc.get_user_tactcoins_history(conn,user_id)

    res = {
        "user_id": user_id,
        "user_tactcoins_history": result
    }
    
    print("Inside Route : ",result)


    return make_response(jsonify(res), 200)

'''
http://127.0.0.1:5000/api/signup

'''

@app.route("/api/signup", methods=['POST'])
def signup():
    # result = bc.select_all(get_db())
    username = request.json['user_name']
    email = request.json['email']
    password = request.json['password']
    location = request.json['location']
    country = request.json['country']
    bio = request.json['bio']

    conn = get_db_conn()
    row = fvc.insert_user(conn, username, email, password, location, country,bio)
    print("user obj:",row)
    err_msg = None

    if(row == -1):
        err_msg = 'Email already exists'
        err_code = 1
        res = {
            "err_code":err_code,
            "err_msg":err_msg
        }
    else:
        err_code = 0   
        res = {
            "user_id": row[0],
            "user_name": row[1],
            "email": row[2],
            "location":row[4],
            "country":row[5],
            "registered_at":row[6],
            "updated_at":row[7],
            "user_role":row[8],
            "bio":row[9],
            "err_code":err_code,
            "err_msg":err_msg
        }
    
    print("Inside Route : ",res)


    return make_response(jsonify(res), 200)


'''
http://127.0.0.1:5000/api/add-tactcoins

'''

@app.route("/api/add-tactcoins", methods=['POST'])
def add_tactcoins():
    # result = bc.select_all(get_db())
    team_id = request.json['team_id']
    tactcoins = request.json['tactcoins']
    feature_id = request.json['feature_id']
    comments = request.json['comments']

    conn = get_db_conn()
    row = fvc.add_tactcoins(conn, team_id, tactcoins, feature_id, comments)
    res = {
        "fs_tactcoins_id": row[0],
        "team_id": row[1],
        "feature_id": row[2],
        "feature_coins":row[3],
        "status":row[4],
        "comments":row[5]
    }
    
    print("Inside Route : ",res)


    return make_response(jsonify(res), 200)

'''
http://127.0.0.1:5000/api/update-user-handle

'''

@app.route("/api/update-user-handle", methods=['PUT'])
def update_user_handle():
    # result = bc.select_all(get_db())
    user_id = request.json['user_id']
    github_handle = request.json['github_handle']
    linkedin_handle = request.json['linkedin_handle']

    conn = get_db_conn()
    row = fvc.update_user_handle(conn, user_id, github_handle, linkedin_handle)
    print("user obj:",row)
    res = {
        "user_id": row[0],
        "github_handle": row[10],
        "linkedin_handle": row[11]
    }
    
    print("Inside Route : ",res)


    return make_response(jsonify(res), 200)

'''
http://127.0.0.1:5000/api/update-user-handle

'''

@app.route("/api/update-user-bio", methods=['PUT'])
def update_user_bio():
    # result = bc.select_all(get_db())
    user_id = request.json['user_id']
    bio = request.json['bio']

    conn = get_db_conn()
    row = fvc.update_user_bio(conn, user_id, bio)
    print("user obj:",row)
    res = {
        "user_id": row[0],
        "bio": row[9]
    }
    
    print("Inside Route : ",res)


    return make_response(jsonify(res), 200)

'''
http://127.0.0.1:5000/api/update-feature-status

'''

@app.route("/api/update-feature-status", methods=['PUT'])
def update_feature_status():
    # result = bc.select_all(get_db())
    feature_id = request.json['feature_id']
    status = request.json['status']

    conn = get_db_conn()
    row = fvc.update_feature_status(conn,feature_id, status)
    res = {
        "feature_id": row[2],
        "status": row[4]
    }
    
    print("Inside Route : ",res)


    return make_response(jsonify(res), 200)




# '''
# http://0.0.0.0:5001/start

# '''

# @app.route("/", methods=['GET'])
# def index():
#     result = bc.select_all(get_db())
#     return make_response(jsonify(result), 200)
# '''
# Started by-Vyshnavi Katikala

# '''


# '''
# http://0.0.0.0:5001/start

# '''

# @app.route("/start", methods=['GET'])
# def start():
#     result = d.start()
#     return make_response(jsonify(result=result), 200)

# '''
# http://0.0.0.0:5001/delete_all

# '''
    
# @app.route("/delete_all", methods=['GET'])
# def delete_all():
#     result = delete.delete_all()
#     return make_response(jsonify(result=result), 200)

# '''
# http://0.0.0.0:5001/select_1

# '''

# @app.route("/select_1", methods=['GET'])
# def select_1():
#     result = sel.select_1()
#     return make_response(jsonify(result=result), 200)

# '''
# http://0.0.0.0:5001/update

# '''
# @app.route("/update", methods=['GET'])
# def update():
#     result = up.update()
#     return make_response(jsonify(result=result), 200)


# '''
# http://0.0.0.0:5001/movie_collector_wiki

# '''
# @app.route("/movie_collector_wiki", methods=['GET'])
# def movie_collector_wiki():
#     result = movie.movie_collector_wiki()
#     return make_response(jsonify(result=result), 200)


# '''ended - Vyshnavi Kaatikala'''


# '''Started - Gokul'''
# '''artist_score_crud - Gokul'''

# '''
# select_all
# http://0.0.0.0:5001/select_all
# '''


# @app.route("/select_all", methods=['GET'])
# def select_all():
#     result = ASCO.select_all(get_db())
#     return make_response(jsonify(result), 200)


# '''
# get_actor_id
# http://0.0.0.0:5001/get_actor_id/Dhanush
# '''


# @app.route("/get_actor_id/<actor_name>", methods=['GET'])
# def get_actor_id(actor_name):
#     result = ARCRUD.get_actor_id(get_db(), actor_name)
#     return make_response(jsonify(result), 200)


# '''
# get_actor_details_by_name
# http://0.0.0.0:5001/get_actor_details_by_name/Dhanush
# '''


# @app.route("/get_actor_details_by_name/<actor_name>", methods=['GET'])
# def get_actor_details_by_name(actor_name):
#     result = ARCRUD.get_actor_details_by_name(get_db(), actor_name)
#     return make_response(jsonify(result), 200)


# '''
# select_all_artits
# http://0.0.0.0:5001/select_all_artits/10/5
# NameError: name 'actor_name' is not defined
# '''


# @app.route("/select_all_artits/<limit>/<offset>", methods=['GET'])
# def select_all_artits(limit, offset):
#     result = ASCO.select_all_artits(get_db(), limit, offset)
#     return make_response(jsonify(result), 200)


# '''movie_basic_crud - Gokul'''

# '''
# select_all_movies_with_artists_by_movie_name
# http://0.0.0.0:5001/select_all_movies_with_artists_by_movie_name/Asuran
# '''


# @app.route("/select_all_movies_with_artists_by_movie_name/<movie_name>", methods=['GET'])
# def select_all_movies_with_artists_by_movie_name(movie_name):
#     result = MBC.select_all_movies_with_artists_by_movie_name(
#         get_db(), movie_name)
#     return make_response(jsonify(result), 200)


# '''
# select_all_movies_by_actor_name
# http://0.0.0.0:5001/select_all_movies_by_actor_name/Dhanush
# '''


# @app.route("/select_all_movies_by_actor_name/<actor_name>", methods=['GET'])
# def select_all_movies_by_actor_name(actor_name):
#     result = MBC.select_all_movies_by_actor_name(get_db(), actor_name)
#     return make_response(jsonify(result), 200)


# '''
# add_movie
# http://0.0.0.0:5001/add_movie
# '''


# @app.route("/add_movie", methods=['GET'])
# def add_movie_mbc():
#     obj = request.get_json(force=True)
#     result = MBC.add_movie(get_db(), obj)
#     return make_response(jsonify(result), 200)


# '''
# update_movie
# http://0.0.0.0:5001/update_movie
# '''


# @app.route("/update_movie", methods=['GET'])
# def update_movie_mbc():
#     obj = request.get_json(force=True)
#     result = MBC.update_movie(get_db(), obj)
#     return make_response(jsonify(result), 200)


# '''
# delete_movie
# http://0.0.0.0:5001/delete_movie/Asuran
# '''


# @app.route("/delete_movie/<name>", methods=['GET'])
# def delete_movie_mbc(name):
#     result = MBC.delete_movie(get_db(), name)
#     return make_response(jsonify(result), 200)





# '''Ended - Gokul'''

# '''Started - Vaishnavi V'''

# '''
#     http://127.0.0.1:5001/select-all-by-actor/<actor_name>
# '''


# @app.route("/select-all-by-actor/<actor_name>")
# def select_all_by_actor(actor_name):
#     result = bc.select_all_by_actor(get_db(), actor_name)
#     return make_response(jsonify(result), 200)


# '''
#     http://127.0.0.1:5001/add-coartist-bubble
# '''


# @app.route("/add-coartist-bubble")
# def add_coartist_bubble():
#     obj = request.get_json(force=True)
#     print("JSON INPUT ::::  \n", obj)
#     result = bc.add_coartist_bubble(get_db(), obj)
#     return make_response(jsonify(result), 200)


# '''
#     http://127.0.0.1:5001/update-movie
# '''


# @app.route("/update-movie")
# def update_movie_bc():
#     obj = request.get_json(force=True)
#     print("JSON INPUT ::::  \n", obj)
#     result = bc.update_movie(get_db(), obj)
#     return make_response(jsonify(result), 200)


# '''
# http://127.0.0.1:5001/delete-movie/<name>
# '''


# @app.route("/delete-movie/<name>")
# def delete_movie_bc(name):
#     result = bc.delete_movie(get_db(), name)
#     return make_response(jsonify(result), 200)



# '''
# http://127.0.0.1:5001/add-movie/<name>/<releasedate>/<starring>
# '''


# @app.route("/add-movie/<name>/<releasedate>/<starring>")
# def add_movie_bc(name, releasedate, starring):
#     result = ins.add_movie(name, releasedate, starring)
#     return make_response(jsonify(result), 200)


# '''Ended - Vaishnavi V'''


# ''' START OF MY WORK - KARTHIK '''

# ''' artist_score_crud'''

# ''' Routes '''

# ''' select all by actor name : route - /select-all-by-actor-name/Dhanush'''


# @app.route("/select-all-by-actor-name/<actor_name>")
# def select_all_by_actor_name(actor_name):
#     result = ASCO.select_all_by_actor(get_db(), actor_name)
#     return make_response(jsonify(result), 200)


# ''' select coartist bubble by artist : route - /select-coartist-bubble-by-artist '''


# @app.route("/select-coartist-bubble-by-artist/<actor_name>")
# def select_coartist_bubble_by_artist(actor_name):
#     result = ASCO.select_coartist_bubble_by_artist(get_db(), actor_name)
#     return make_response(jsonify(result), 200)


# ''' /add-artist-score-crud '''


# @app.route("/add-artist-score-crud")
# def add_artist_score_crud():
#     obj = request.get_json(force=True)
#     result = ASCO.add_artist_score_crud(get_db(), obj)
#     return make_response(jsonify(result), 200)


# ''' /update-movie-asco '''


# @app.route("/update-movie-asco")
# def update_movie_asco():
#     obj = request.get_json(force=True)
#     result = ASCO.update_movie(get_db(), obj)
#     return make_response(jsonify(result), 200)


# '''  /delete-movie-asco/Asuran  '''


# @app.route("/delete-movie-asco/<movie_name>")
# def delete_movie(movie_name):
#     result = ASCO.delete_movie(get_db(), movie_name)
#     return make_response(jsonify(result), 200)


# '''  /delete-all-movies-asco '''


# @app.route("/delete-all-movies-asco")
# def delete_all_movies():
#     result = ASCO.delete_all_movies(get_db())
#     return make_response(jsonify(result), 200)


''' END OF MY WORK - KARTHIK '''

# def select_all():
#     """
#     Query all rows in the MOVIE table
#     :param conn: the Connection object
#     :return:
#     """
#     cur = get_db().cursor()
#     cur.execute("SELECT * FROM MOVIE")

#     rows = cur.fetchall()

#     print('rows count : '+str(len(rows)))

#     if(len(rows) <= 0):
#         print('No Data available')
#         return ('No Data available')
#     return jsonify(rows)


if __name__ == "__main__":
    app.run(debug=True)
