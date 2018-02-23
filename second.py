'''
Created on Feb 23, 2018

@author: Sagar Bayar
'''
class Customer:
    def setcustomerid(self,id):
        self._customerid=id
    def setcustomername(self,teleno):
        self._telephoneno=teleno
    def getcustomerid(self):
        return self._customerid
    def getcustomername(self):
        return self._telephoneno

class privilagedcustomer(Customer):
    def __init__(self):
        memCardType=""  
    def setmemcardtype(self,typ):
        self._memCardType=typ
    def getmemcardtype(self):
        return self._memCardType
    
pcustobj = privilagedcustomer()
pcustobj.setcustomerid(1)
pcustobj.setcustomername("sagar bayar")
pcustobj.setcustomerid("permanent")
print("Customer ID:",pcustobj.getcustomerid())
print("Customer Name:",pcustobj.getcustomername())
print("Customer mem Card type:",pcustobj.getmemcardtype())