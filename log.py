#!/usr/bin/env python

import psycopg2


def connect(dbname="news"):
    """Connect to the PostgreSQL database and returns a database connection."""
    try:
        db = psycopg2.connect("dbname={}".format(dbname))
        c = db.cursor()
        return db, c
    except:
        print("Error in connecting to database")

def popular_article():
    """Prints most popular three articles of all time"""
    db, c = connect()
    query = "select * from popular_articles limit 3"
    c.execute(query)
    result = c.fetchall()
    db.close()
    print "\nPopular Articles:\n"
    for i in range(0, len(result), 1):
        print "\"" + result[i][0] + "\" - " + str(result[i][1]) + " views"


def popular_authors():
    """Prints most popular article authors of all time"""
    db, c = connect()
    query = "select * from popular_authors"
    c.execute(query)
    result = c.fetchall()
    db.close()
    print "\nPopular Authors:\n"
    for i in range(0, len(result), 1):
        print "\"" + result[i][0] + "\" - " + str(result[i][1]) + " views"


def log_status():
    """Print days on which more than 1% of requests lead to errors"""
    db, c = connect()
    query = "select * from log_status"
    c.execute(query)
    result = c.fetchall()
    db.close()
    print "\nDays with more than 1% of errors:\n"
    for i in range(0, len(result), 1):
        print str(result[i][0])+ " - "+str(round(result[i][3], 2))+"% errors"

if __name__ == '__main__':
    # uncomment the below code to make views
    '''
    view_popular_article()
    view_popular_authors()
    view_log_status()
    '''
    popular_article()
    popular_authors()
    log_status()
    print "\nSuccess!\n"
