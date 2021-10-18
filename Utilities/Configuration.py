import configparser
import logging

import mysql.connector
from mysql.connector import Error
from Utilities import custom_logging as cl

#class Config:
log = cl.log(logging.DEBUG)

def getconfig():
    config = configparser.ConfigParser()
    config.read("C:\\Users\\Punam\\workspace_python\\apipy\\Utilities\\Properties.ini")
    return config

connsett= {
    'host': getconfig()['SQL']['hostname'],
    'database': getconfig()['SQL']['database'],
    'user': getconfig()['SQL']['username'],
    'password': getconfig()['SQL']['password']
    }

def getconnection():
    try:
        conn = mysql.connector.connect(**connsett)
        if conn.is_connected():
            log.info("DB connected")
            return conn
    except Error as e:
            log.error(e)

def updatequery(uquery, data):
    conn=getconnection()
    cursor=conn.cursor()
    cursor.execute(uquery, data)
    conn.commit()
    conn.close()

def getdataquery(gquery):
    conn = getconnection()
    cursor=conn.cursor()
    cursor.execute(gquery)
    row= cursor.fetchone()
    conn.close()
    return row

