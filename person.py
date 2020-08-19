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