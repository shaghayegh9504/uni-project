class Librarian():
    
    def __init__(self,id,name,password):
        self.id = id
        self.name=name
        self.password = password



    def save2Db(self):
        sql = ''' INSERT INTO Librarian(id,name,password)
        VALUES(?,?,?) '''
        cur = conn.cursor()
        cur.execute(sql,self.id,self.name,self.password)


    def __str__(self):
        return f'Id : {self.id} , Name : {self.name} , Password : {self.password}'


    def __repr__(self):
        pass

