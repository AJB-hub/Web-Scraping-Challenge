from pymongo import MongoClient
from scrape import scrape
import pandas as pd
import pprint
import typing

from bson.objectid import ObjectId

def push(col):
    
    maguffin = scrape()
    
    #Insert first three dictionaries
    for i in range(0, len(maguffin) - 1):
        col.insert_one(maguffin[i])

    #Insert list of dictionaries
    for i in range(0, len(maguffin[3])):
        col.insert_one(maguffin[3][i])


def get(request:str, col) -> list:  #must be run after push

    document = [i for i in col.find()]
    
    translator = {f'p{i}': document[i]['_id'] for i in range(0, len(document))}
    
    post_id = translator[request]
    
    query = {"_id": post_id}

    document = [i for i in col.find(query)]

    return [val for val in document]
    

