# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 20:47:33 2017

@author: Mikołaj
"""

import psycopg2
def select_all(tbname):

  conn = psycopg2.connect(dbname='db', user='grok')

  cursor = conn.cursor()
  
  cursor.execute('SELECT * FROM '+str(tbname)+';')

  records = cursor.fetchall()
  return records