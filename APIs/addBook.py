import requests
from Utilities.Configuration import *
from Utilities.Resources import *
from Utilities.payload import *
from Utilities import custom_logging as cl


class addBook:
    log= cl.log(logging.DEBUG)
    gquery = 'select * from Books'

    def validatemessage(self):
        aurl= getconfig()['API']['endpoint']+Resources.addbook
        #gquery = 'select * from Books'
        res= requests.post(aurl,json=payload(self.gquery))
        self.log.info(res)
        res_json= res.json()
        self.log.info(res_json)
        if res_json['Msg'] == 'successfully added' and res_json['ID'] is not None:
            return True
        else:
            return False

    def updatebook(self):
        row=getdataquery(self.gquery)
        uquery = "update Books set aisle = %s where BookName = %s"
        data=(int(row[2])+1,row[0])
        updatequery(uquery, data)

