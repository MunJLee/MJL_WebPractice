"""
This module is basically a model for MVC
Normally server access and data exchange should happen here,
but since I'm not using any server at this time, it will just read json and
return data as needed.
"""

import json

# read a local .json file
with open('./model/data.json', 'r') as datastore:
    data = datastore.read()

# parse the file content
content = json.loads(data)


# get all record
def getAllRecord():
    return content['libraryCard']


# get a single record with matching id
def getRecordWithID(idNum):
    for rec in content['libraryCard']:
        if int(rec['id']) == idNum:
            return rec


# get a collection of data from a single record
def getAllEntries(idNum, itemType):
    for rec in content['libraryCard']:
        if int(rec['id']) == idNum:
            return rec[itemType]


# get a single entry of data from a single record
def getEntryWithID(idNum, itemType, entryId):
    for rec in content['libraryCard']:
        if int(rec['id']) == idNum:
            items = rec[itemType]
            for ent in items:
                if int(ent['entry']) == entryId:
                    return ent


def getTest():
    return content['libraryCard'][0]

