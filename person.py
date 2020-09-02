class Person():
    def __init__(self,fname , lname , age , pid):
        self.fname = fname
		self.lname = lname
		self.age = age
		self.id = fpid
		
	def searchbook(self,book_name):
		if book_name in ['4 tappeh' , 'adam va havva' , 'mardi be name ove' ]
			print(book_name)
		else :
			print('Not found!!!')
		
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



    def Get_book(self):
        pass

    def return_book(self):
        pass