import pymysql


class db_connection:

    def __init__(self):
        self.Database = 'db_gereja_gsja'
        self.User     = 'root'
        self.Password = ''
        self.Hostname = 'localhost'

        self.connection_database = pymysql.connect(host=self.Hostname, user=self.User, password=self.Password)
        self.connection          = self.connection_database.cursor()
        self.connection.execute("USE %s" % (self.Database))
    

    # Beranda

    def show_carousel(self, coloumn_names = [], table_name = '', statement = {}):
        queri = 'SELECT '
        col = ''
        state = ''
        for i in coloumn_names:
            col = col + ',' + i  
        col = col[1:]
        if statement:
            for x in statement:
                if(type(statement[x]))==str:
                    statement[x] = '"'+str(statement[x])+'"'
                state = state + (str(x) +" = "+str(statement[x])) + ' AND '
            state = state[:-5]
            queri = queri + col + ' FROM ' + table_name + ' WHERE '+ state
        else:
            queri = queri + col + ' FROM ' + table_name
        print(queri)
        try:
            self.connection.execute(queri)
            results = self.connection.fetchall()
        except:
            print("Something Wrong!")
        finally:
            self.connection.close()
        return results





    # Tentang

    




    # Blog

    def show_post(self, coloumn_names = [], table_name = '', statement = {}):
        queri = 'SELECT '
        col = ''
        state = ''
        for i in coloumn_names:
            col = col + ',' + i  
        col = col[1:]
        if statement:
            for x in statement:
                if(type(statement[x]))==str:
                    statement[x] = '"'+str(statement[x])+'"'
                state = state + (str(x) +" = "+str(statement[x])) + ' AND '
            state = state[:-5]
            queri = queri + col + ' FROM ' + table_name + ' WHERE '+ state + ' ORDER BY tanggal DESC'
        else:
            queri = queri + col + ' FROM ' + table_name + ' ORDER BY tanggal DESC'
        print(queri)
        try:
            self.connection.execute(queri)
            results = self.connection.fetchall()
        except:
            print("Something Wrong!")
        finally:
            self.connection.close()    
        return results
    
    def search_post(self, coloumn_names = [], table_name = '', statement = {}):
        queri = 'SELECT '
        col = ''
        state = ''
        order_state = ''
        for i in coloumn_names:
            col = col + ',' + i  
        col = col[1:]
        if statement:
            for x in statement:
                if(type(statement[x]))==str:
                    statement[x] = '"'+str(statement[x])+'"'
                state = state + (str(x) +" IN "+str(statement[x])) + ' AND '
            state = state[:-5]
            j = 1
            for i in statement['id_postingan']:
                order_state = order_state + 'WHEN id_postingan = '+str(i)+' then '+str(j)+' '
                j = j + 1
            order_state = order_state + 'END ASC'
            queri = queri + col + ' FROM ' + table_name + ' WHERE '+ state+' ORDER BY CASE '+ order_state
        else:
            queri = queri + col + ' FROM ' + table_name 
        print(queri)
        try:
            self.connection.execute(queri)
            results = self.connection.fetchall()
        except:
            print("Something Wrong!")
        finally:
            self.connection.close()    
        return results

    def show_category(self, coloumn_names = [], table_name = '', statement = {}):
        queri = 'SELECT '
        col = ''
        state = ''
        for i in coloumn_names:
            col = col + ',' + i  
        col = col[1:]
        if statement:
            for x in statement:
                if(type(statement[x]))==str:
                    statement[x] = '"'+str(statement[x])+'"'
                state = state + (str(x) +" = "+str(statement[x])) + ' AND '
            state = state[:-5]
            queri = queri + col + ' FROM ' + table_name + ' WHERE '+ state
        else:
            queri = queri + col + ' FROM ' + table_name
        
        print(queri)
        try:
            self.connection.execute(queri)
            results = self.connection.fetchall()
        except:
            print("Something Wrong!")
        finally:
            self.connection.close()
        return results

    def show_comment(self, coloumn_names = [], table_name = '', statement = {}):
        queri = 'SELECT '
        col = ''
        state = ''
        for i in coloumn_names:
            col = col + ',' + i  
        col = col[1:]
        if statement:
            for x in statement:
                if(type(statement[x]))==str:
                    statement[x] = '"'+str(statement[x])+'"'
                state = state + (str(x) +" = "+str(statement[x])) + ' AND '
            state = state[:-5]
            queri = queri + col + ' FROM ' + table_name + ' WHERE '+ state + ' ORDER BY tanggal DESC'
        else:
            queri = queri + col + ' FROM ' + table_name + ' ORDER BY tanggal DESC'
        print(queri)
        try:
            self.connection.execute(queri)
            results = self.connection.fetchall()
        except:
            print("Something Wrong!")
        finally:
            self.connection.close()    
        return results
    
    def send_comment(self, table_name = '', data = ()):
        queri = 'INSERT INTO ' + str(table_name) + " (id_komentar, penulis, status_komentar, tanggal, isi, postingan) VALUES " + str(data) 
        try:
            print(queri)
            self.connection.execute(queri)
            self.connection_database.commit()
            result = 'Successed'
        except:
            print("Something Wrong!")
            self.connection_database.rollback()
            result = 'Failed'
        finally:
            self.connection.close()
        return result


    # Kegiatan
    
    def show_activity_carousel(self, coloumn_names = [], table_name = '', statement = {}):
        queri = 'SELECT '
        col = ''
        state = ''
        for i in coloumn_names:
            col = col + ',' + i  
        col = col[1:]
        if statement:
            for x in statement:
                if(type(statement[x]))==str:
                    statement[x] = '"'+str(statement[x])+'"'
                state = state + (str(x) +" = "+str(statement[x])) + ' AND '
            state = state[:-5]
            queri = queri + col + ' FROM ' + table_name + ' WHERE '+ state
        else:
            queri = queri + col + ' FROM ' + table_name
        print(queri)
        try:
            self.connection.execute(queri)
            results = self.connection.fetchall()
        except:
            print("Something Wrong!")
        finally:
            self.connection.close()
        return results
    
    def show_activity_schedule(self, coloumn_names = [], table_name = '', statement = {}):
        queri = 'SELECT '
        col = ''
        state = ''
        for i in coloumn_names:
            col = col + ',' + i  
        col = col[1:]
        if statement:
            for x in statement:
                if(type(statement[x]))==str:
                    statement[x] = '"'+str(statement[x])+'"'
                state = state + (str(x) +" = "+str(statement[x])) + ' AND '
            state = state[:-5]
            queri = queri + col + ' FROM ' + table_name + ' WHERE '+ state
        else:
            queri = queri + col + ' FROM ' + table_name
        print(queri)
        try:
            self.connection.execute(queri)
            results = self.connection.fetchall()
        except:
            print("Something Wrong!")
        finally:
            self.connection.close()
        return results




    # Galeri


    def show_gallery(self, coloumn_names = [], table_name = '', statement = {}):
        queri = 'SELECT '
        col = ''
        state = ''
        for i in coloumn_names:
            col = col + ',' + i  
        col = col[1:]
        if statement:
            for x in statement:
                if(type(statement[x]))==str:
                    statement[x] = '"'+str(statement[x])+'"'
                state = state + (str(x) +" = "+str(statement[x])) + ' AND '
            state = state[:-5]
            queri = queri + col + ' FROM ' + table_name + ' WHERE '+ state + ' ORDER BY tanggal DESC'
        else:
            queri = queri + col + ' FROM ' + table_name + ' ORDER BY tanggal DESC'
        print(queri)
        try:
            self.connection.execute(queri)
            results = self.connection.fetchall()
        except:
            print("Something Wrong!")
        finally:
            self.connection.close()
        return results

    # Download

    def show_download(self, coloumn_names = [], table_name = '', statement = {}):
        queri = 'SELECT '
        col = ''
        state = ''
        for i in coloumn_names:
            col = col + ',' + i  
        col = col[1:]
        if statement:
            for x in statement:
                if(type(statement[x]))==str:
                    statement[x] = '"'+str(statement[x])+'"'
                state = state + (str(x) +" = "+str(statement[x])) + ' AND '
            state = state[:-5]
            queri = queri + col + ' FROM ' + table_name + ' WHERE '+ state + ' ORDER BY tanggal DESC'
        else:
            queri = queri + col + ' FROM ' + table_name + ' ORDER BY tanggal DESC'
        print(queri)
        try:
            self.connection.execute(queri)
            results = self.connection.fetchall()
        except:
            print("Something Wrong!")
        finally:
            self.connection.close()
        return results

    # Alkitab

    # Kontak
