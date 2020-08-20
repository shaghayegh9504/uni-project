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

	
	# Feature12
	def new_feature (self):
		print('+++++++++++++++++++++++')
		print('everything is ok')