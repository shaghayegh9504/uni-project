class Member():
    
    def __init__(self,id,name,address,password,kind):
        self.id = id
        self.name=name
        self.address=address
        self.password = password
        self.kind=kind

    
    def save2Db(self):
        sql = ''' INSERT INTO Member(id,name,password,kind)
        VALUES(?,?,?,?) '''
        cur = conn.cursor()
        cur.execute(sql,self.id,self.name,self.password,self.kind)

    def __str__(self):
        return f'Id : {self.id} , Name : {self.name} , Address : {self.address} , Password : {self.password} , Kind : {self.kind}'



class Book():
    
    def __init__(self,id,name,edition,auther,status):
        self.id = id
        self.name=name
        self.edition = edition
        self.auther=auther
        self.status=status


    def save2Db(self):
        sql = ''' INSERT INTO Book(id,name,edition,auther,status)
        VALUES(?,?,?,?,?) '''
        cur = conn.cursor()
        cur.execute(sql,self.id,self.name,self.edition,self.auther,self.status)


    def __str__(self):
        return f'Id : {self.id} , Name : {self.name} , Edition : {self.edition} , Auther : {self.auther} , Status : {self.status}'
