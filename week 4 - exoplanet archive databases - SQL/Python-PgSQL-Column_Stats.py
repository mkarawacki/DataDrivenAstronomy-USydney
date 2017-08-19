# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 20:49:58 2017

@author: Mikołaj
"""

import psycopg2
import numpy as np
def column_stats(tbname,col):
  conn = psycopg2.connect(dbname='db', user='grok')
  cursor = conn.cursor()
  cursor.execute('SELECT '+str(col)+' FROM '+str(tbname)+';')
  records = cursor.fetchall()
  column=np.array(records)
  return column.mean(),np.median(column)
