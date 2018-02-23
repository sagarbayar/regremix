class Customer:

    def setcustomerid(self,id):
        self.customerid=id
    def settelephoneno(self,teleno):
        self.telephoneno=teleno
    def getcustomerid(self):
        return self.customerid
    def gettelephoneno(self):
        return self.telephoneno
custobj = Customer()
custobj.setcustomerid(1)
custobj.settelephoneno(9539563663)
print("Customer ID:",custobj.getcustomerid())
print("Customer Phone Number:",custobj.gettelephoneno())





class Student:
    def __init__(self):
        self.__studentid=0
        self.__telephoneno=[]
        
    def setstudentid(self,id):
        self.__studentid=id
    def settelephoneno(self,teleno):
        self.__telephoneno=teleno
    def getstudentid(self):
        return self.__studentid
    def gettelephoneno(self):
        return self.__telephoneno
studobj = Student()
studobj.setstudentid(10)
studobj.settelephoneno(1234567890)
print("Student ID:",studobj.getstudentid())
print("Customer Phone Number:",studobj.gettelephoneno()) 