from Utilities.Configuration import *
def payload(gquery):
    row=getdataquery(gquery)
    input = {}
    input['name'] = row[0]
    input['isbn'] = row[1]
    input['aisle'] = row[2]
    input['author'] = row[3]
    return input
