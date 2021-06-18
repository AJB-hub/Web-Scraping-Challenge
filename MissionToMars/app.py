from pymongo import MongoClient

import pandas as pd
import pprint
import typing

from bson.objectid import ObjectId

from flask import Flask, render_template

from scrape import scrape
from pushpull import get, push

# Create an instance of our Flask app.
app = Flask(__name__)

#Scrape Data to start
push()

# Set route
@app.route('/')
def index():

    return render_template('./html/index.html', 
                                        title = get('p0')[0]['news_title'],
                           
                                        para = get('p0')[0]['news_p'],

                                        img = get('p1')[0]['image_url'],

                                        table = get('p2')[0]['mars_table'],

                                        h_title = [get(f'p{i}')[0]['title'] for i in range(3,7)],

                                        h_url = [get(f'p{i}')[0]['img_url'] for i in range(3,7)],

                          )


@app.route('/scrape')
def ScrapeRequest():
    
    try:
        
        push()
        
    finally:
        
        return render_template('./html/index.html', 
                                            title = get('p0')[0]['news_title'],

                                            para = get('p0')[0]['news_p'],

                                            img = get('p1')[0]['image_url'],

                                            table = get('p2')[0]['mars_table'],

                                            h_title = [get(f'p{i}')[0]['title'] for i in range(3,7)],

                                            h_url = [get(f'p{i}')[0]['img_url'] for i in range(3,7)],

                              )

if __name__ == "__main__":
    app.run(debug=True)

