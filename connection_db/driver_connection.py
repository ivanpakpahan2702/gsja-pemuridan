import pymysql


# Buat Database
def create_db(db_name):
    conn = pymysql.connect(host="localhost", user="root", password="")
    connection = conn.cursor()
    queri = "CREATE DATABASE IF NOT EXISTS %s"
    connection.execute(queri % (db_name))
    conn.close()


# Membuat Tabel
def create_table(db_name, tbl_name):
    conn = pymysql.connect(host="localhost", user="root", password="")
    connection = conn.cursor()
    connection.execute("USE %s" % (db_name))
    queri = "CREATE TABLE IF NOT EXISTS %s (id_user int(11) NOT NULL, nama varchar(20) NOT NULL)"
    connection.execute(queri % (tbl_name))
    conn.close()


# Membuat Data
def create_data(db_name, tbl_name, data):
    conn = pymysql.connect(host="localhost", user="root", password="")
    connection = conn.cursor()
    connection.execute("USE %s" % (db_name))
    queri = "INSERT INTO "+str(tbl_name)+" (id_user, nama) VALUES (%s, '%s')"
    try:
        print(queri % data)
        connection.execute(queri % data)
        conn.commit()
    except:
        print("Sesuatu Salah")
        conn.rollback()
    finally:
        conn.close()


# Delete Data
def delete_data(db_name, tbl_name, id):
    conn = pymysql.connect(host="localhost", user="root", password="")
    connection = conn.cursor()
    connection.execute("USE %s" % (db_name))
    queri = "DELETE FROM "+str(tbl_name)+" WHERE %s%s"
    nama_kolom = "id_user="
    value_kolom = id
    try:
        connection.execute(queri % (
            nama_kolom, value_kolom))
        conn.commit()
    except:
        print("Sesuatu Salah")
        conn.rollback()
    finally:
        conn.close()
        print("-")


# Show 1 Data
def show_one_data(db_name, tbl_name, id):
    conn = pymysql.connect(host="localhost", user="root", password="")
    connection = conn.cursor()
    connection.execute("USE %s" % (db_name))
    queri = "SELECT * FROM "+str(tbl_name)+" WHERE %s%s"
    nama_kolom = "id_user="
    value_kolom = id
    try:
        connection.execute(queri % (
            nama_kolom, value_kolom))
        results = connection.fetchall()
    except:
        print("Sesuatu Salah")
    finally:
        conn.close()
    return results

# Show All Data
def show_data(db_name, tbl_name):
    conn = pymysql.connect(host="localhost", user="root", password="")
    connection = conn.cursor()
    connection.execute("USE %s" % (db_name))
    connection = conn.cursor()
    queri = "SELECT * FROM "+str(tbl_name)
    try:
        connection.execute(queri)
        results = connection.fetchall()
    except:
        print("Sesuatu Salah")
    finally:
        conn.close()
    return results


# res = show_data("db_gereja_gsja", "tabel_jadwal_kegiatan")
# db_path = []
# for i in range(len(res)):
#     db_path.append(res[i][1])
# print(res[0][2])

# a = list_data[0]
# print(a[1])
# delete_data("db_pymysql", "tbl_user", 6)

# data = (6, 'Sullivan')
# create_data("db_pymysql", "tbl_user", data)

# https://www.databasejournal.com/mysql/the-10-most-common-mysql-queries/
