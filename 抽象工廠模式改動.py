class User:
    
    _name : str 
    _id : int
    name : str 
    id : int

    def get_id(self):
        return self._id
    
    def set_id(self,val:int):
        self._id = val
    
    def get_name(self):
        return self._name
    
    def set_id(self,val:str):
        self._name = val
    
class Department:
    _name : str 
    _id : int
    name : str 
    id : int

    def get_id(self):
        return self._id
    
    def set_id(self,val:int):
        self._id = val
    
    def get_name(self):
        return self._name
    
    def set_id(self,val:str):
        self._name = val

class IUserInterface:

    def insert(self,user:User):
        pass
    
    def get_user(self,id:int):
        pass

class IDepartmentInterface:

    def insert(self,depart:Department):
        pass
    
    def get_deparment(self,id:int):
        pass

class SqlServer(IUserInterface):
    
    def insert(self, user: User):
        print("在SQL中給Server插入一個User資料",flush=True)

    def get_user(self, id: int):
        print("從Sql獲得User資料表",flush=True)
        return None

class AccessServer(IUserInterface):

    def insert(self, user: User):
        print("在Access中給Server插入一個User資料",flush=True)

    def get_user(self, id: int):
        print("從Access獲得User資料表",flush=True)
        return None

class SqlDepartment(IDepartmentInterface):
    
    def insert(self, department: Department):
        print("在SQL中給Server插入一個Department資料",flush=True)
    
    def get_deparment(self, id: int):
        print("從Sql獲得Department資料表",flush=True)
        return None

class AccessDepartment(IDepartmentInterface):

    def insert(self, depart: Department):
        print("在Access中給Server插入一個Department資料",flush=True)

    def get_deparment(self, id: int):
        print("從Access獲得Department資料表",flush=True)
        return None

class IFactory:

    def createUser(self):
        pass

    def createDepartment(self):
        pass

class SqlFactory(IFactory):

    def createUser(self):
        return SqlServer()
    
    def createDepartment(self):
        return SqlDepartment()
    
class AccessFacotry(IFactory):
    
    def createUser(self):
        return AccessServer()
    
    def createDepartment(self):
        return AccessDepartment()

class DataAccess:
    _db : str = "SqlServer"

    @classmethod 
    def createUser(cls):
        if cls._db == "SqlServer":
            return SqlServer()
        elif cls._db == "AccessServer":
            return AccessServer()
        
    @classmethod
    def createDepartment(cls):
        if cls._db == "SqlServer":
            return SqlDepartment()
        elif cls._db == "AccessServer":
            return AccessDepartment()

if __name__ == '__main__':
    department = Department()
    user = User()
    sqlUser = DataAccess.createUser()
    sqlUser.insert(user)
    sqlUser.get_user(2)