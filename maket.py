import sqlite3
import random
db_path = 'bot_db.db'
db = sqlite3.connect(db_path)
c = db.cursor()
db.commit()
db.close()


def update_avatar(user_id, photo_data):
    db = sqlite3.connect(db_path)
    c = db.cursor()
    c.execute("""UPDATE users SET avatar = '{}' WHERE user_id = '{}'""".format(photo_data, user_id))
    db.commit()
    db.close()


def get_random_profile(user_id):
    db = sqlite3.connect(db_path)
    c = db.cursor()
    c.execute("""SELECT user_id FROM users""")
    all_ids = set(c.fetchall())
    c.execute("""SELECT liked_id FROM '{}'""".format(user_id))
    liked_ids = set(c.fetchall())
    to_choose_ids = all_ids - liked_ids - {(user_id, ), }
    try:
        random_profile = random.sample(sorted(to_choose_ids), 1)[0][0]
    except ValueError:
        random_profile = 'error'
    db.close()

    return random_profile

def create_user(user_id, photo_data):
    db = sqlite3.connect(db_path)
    c = db.cursor()
    c.execute('''CREATE TABLE '{}' (
                liked_id TEXT
                )'''.format(user_id))
    query_2 = """INSERT INTO users VALUES (?, ?)"""
    params_2 = (user_id, photo_data)
    c.execute(query_2, params_2)
    db.commit()
    db.close()

def get_avatar(user_id):
    db = sqlite3.connect(db_path)
    c = db.cursor()
    c.execute("SELECT avatar FROM users WHERE user_id = '{}'".format(user_id))
    avatar = c.fetchone()[0]
    db.close()

    return avatar

def new_liked(user_id, liked_user_id):
    db = sqlite3.connect(db_path)
    c = db.cursor()
    query = """INSERT INTO '{}' VALUES (?)""".format(user_id)
    params = (liked_user_id, )
    c.execute(query, params)
    db.commit()
    db.close()

def check_sympathy(user_id, liked_user_id):
    db = sqlite3.connect(db_path)
    c = db.cursor()
    for liked_id in c.execute("SELECT liked_id FROM '{}'".format(liked_user_id)).fetchall():
        if liked_id[0] == user_id:
            return True
            break
        else:
            pass
    return False

def check_new(user_id):
    db = sqlite3.connect(db_path)
    c = db.cursor()
    try:
        for exist_id in c.execute("SELECT user_id FROM users").fetchall():
            if exist_id[0] == user_id:
                db.close()
                return False
                break
        db.close()
        return True
    except Exception:
        db.close()
        return True



