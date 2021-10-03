# -*- coding: utf-8 -*-
import pyodbc
from datetime import datetime
import csv
from decimal import Decimal
import logging
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

CLIE= '?,'*102+'?'
ARTS = '?,'*84+'?'
VENT = '?,'*10+'?'
CLIV = '?,'*11+'?'
IPLC = '?,'*5+'?'
ARVI = '?,'*6+'?'
ARCO = '?,'*20+'?'
ARVE = '?,'*34+'?'
AUCO = '?,'*8+'?'
AUVE = '?,'*10+'?'
LIPV = '?,'*13+'?'
DCLI = '?,'*30+'?'
VECL = '?,'*3+'?'

conn = pyodbc.connect('DRIVER={SQL Server};SERVER=PLATAFORMASRV;DATABASE=dbCABAÑASM;UID=sa;PWD=CSMclaypole01')
#conn = pyodbc.connect('DRIVER={SQL Server};SERVER=PLATAFORMASRV;DATABASE=dbCABAÑAPRUEBA;UID=sa;PWD=CSMclaypole01')
cursor = conn.cursor()
logging.basicConfig(filename='C:\dbLoval\error-log.log', filemode='w', level=logging.DEBUG)

def convertir(n_archivo,n_table,n):
    f = open(n_archivo, 'rU')
    next(f, None)
    reader = csv.reader(f, delimiter=';')
    cursor.execute("ALTER TABLE "+n_table+" NOCHECK CONSTRAINT ALL")
    cursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '"+n_table+"'")
   # cursor.execute("DELETE FROM VENT_LIPV")
    table = cursor.fetchall()
    column_sub = [str(x).replace("(u'", "[") for x in table]
    column_name = [str(x).replace("', )", "]") for x in column_sub]
    tamano = len(table)
    if n_table == 'VENT_ARPV':
       cursor.execute("DELETE FROM [dbo].[VENT_ARPV]")
    

    for row in reader:
        
   
        compuesta = " AND " + column_name[1] + " = " + row[1] + "" if n_table == 'VENT_ARPV' else ""
        compuesta = " AND " + column_name[1] + " = " + "'"+row[1]+"'"+" AND "+ column_name[2] + " = " +"'"+ row[2] +"'"+ "" if n_table == 'CCOB_IPCL' else compuesta
        compuesta = " AND " + column_name[1] + " = " + row[1] + "" if n_table == 'STOC_AUCO' else compuesta
        compuesta = " AND " + column_name[1] + " = " + row[1] + "" if n_table == 'STOC_AUVE' else compuesta
        compuesta = " AND " + column_name[1] + " = " + row[1] + "" if n_table == 'CCOB_DCLI' else compuesta
        compuesta = " AND " + column_name[1] + " = " + "'"+row[1]+"'"+" AND "+ column_name[2] + " = " +"'"+ row[2] +"'"+ "" if n_table == 'VENT_ARVI' else compuesta
        cursor.execute("SELECT * FROM [dbo].["+n_table+"] WHERE "+column_name[0]+" = " + row[0] + "" + compuesta)
        row = [x.decode('UTF8') for x in row]
        row =[None if x == 'None' else x for x in row]
        row = [None if x == '' else x for x in row]     
       

        if n_table == 'CCOB_CLIE':
               
               row[46] = None if row[46] == "0" or row[46] == None else datetime.strptime(row[46][0:19], '%Y-%m-%d %H:%M:%S')
               row[47] = None if row[47] == "0" or row[47] == None else datetime.strptime(row[47][0:19], '%Y-%m-%d %H:%M:%S')
               row[56] = None if row[56] == "0" or row[56] == None else datetime.strptime(row[56][0:19], '%Y-%m-%d %H:%M:%S')
               row[57] = None if row[57] == "0" or row[57] == None else datetime.strptime(row[57][0:19], '%Y-%m-%d %H:%M:%S')
               row[58] = None if row[58] == "0" or row[58] == None else datetime.strptime(row[58][0:19], '%Y-%m-%d %H:%M:%S')
               row[59] = None if row[59] == "0" or row[59] == None else datetime.strptime(row[59][0:19], '%Y-%m-%d %H:%M:%S')
               row[68] = None if row[68] == "0" or row[68] == None else datetime.strptime(row[68][0:19], '%Y-%m-%d %H:%M:%S')
               row[69] = None if row[69] == "0" or row[69] == None else datetime.strptime(row[69][0:19], '%Y-%m-%d %H:%M:%S')
            
                

        if n_table =='STOC_ARTS':
           
        
               row[34] = None if row[34] == "0" or row[34] == None else datetime.strptime(row[34][0:19], '%Y-%m-%d %H:%M:%S')
               row[35] = None if row[35] == "0" or row[35] == None else datetime.strptime(row[35][0:19], '%Y-%m-%d %H:%M:%S')
              # if row[23] != None:
              #    row[23] = float(row[23].replace(",", ".")) if row[23].find(",") != -1 else float(row[23])
               if row[41] != None:
                  row[41] = float(row[41].replace(",", ".")) if row[41].find(",") != -1 else float(row[41])
               if row[59] != None:
                  row[59] = float(row[59].replace(",", ".")) if row[59].find(",") != -1 else float(row[59])
               if row[67] != None:
                  row[67] = float(row[67].replace(",", ".")) if row[67].find(",") != -1 else float(row[67])
               if row[38] != None:
                  row[38] = float(row[38].replace(",", ".")) if row[38].find(",") != -1 else float(row[38])
               if row[39] != None:
                  row[39] = float(row[39].replace(",", ".")) if row[39].find(",") != -1 else float(row[39])
               if row[46] != None:
                  row[46] = float(row[46].replace(",", ".")) if row[46].find(",") != -1 else float(row[46])
       
               

        
        if n_table == 'VENT_ARPV':
       
               row[6] = None if row[6] == "0" or row[6] == None else datetime.strptime(row[6][0:19], '%Y-%m-%d %H:%M:%S')
               if row[2] != None:
                  row[2] = float(row[2].replace(",", ".")) if row[2].find(",") != -1 else float(row[2])
               if row[4] != None:
                  row[4] = float(row[4].replace(",", ".")) if row[4].find(",") != -1 else float(row[4])   
              


        if n_table == 'VENT_CLIV':

              if row[2] != None:
                  row[2] = float(row[2].replace(",", ".")) if row[2].find(",") != -1 else float(row[2])
              if row[3] != None:
                  row[3] = float(row[3].replace(",", ".")) if row[3].find(",") != -1 else float(row[3])
              if row[4] != None:
                  row[4] = float(row[4].replace(",", ".")) if row[4].find(",") != -1 else float(row[4])
              if row[5] != None:
                  row[5] = float(row[5].replace(",", ".")) if row[5].find(",") != -1 else float(row[5])


        if n_table == 'CCOB_IPCL':
               row[3] = None if row[3] == "0" or row[3] == None else datetime.strptime(row[3][0:19], '%Y-%m-%d %H:%M:%S')
               row[4] = None if row[4] == "0" or row[4] == None else datetime.strptime(row[4][0:19], '%Y-%m-%d %H:%M:%S')

        if n_table == 'STOC_ARCO':
               if row[9] != None:
                  row[9] = float(row[9].replace(",", ".")) if row[9].find(",") != -1 else float(row[9])
               if row[16] != None:
                  row[16] = float(row[16].replace(",", ".")) if row[16].find(",") != -1 else float(row[16])

        if n_table == 'STOC_ARVE':
               row[3] = None if row[3] == "0" or row[3] == None else datetime.strptime(row[3][0:19], '%Y-%m-%d %H:%M:%S')
               if row[9] != None:
                  row[9] = float(row[9].replace(",", ".")) if row[9].find(",") != -1 else float(row[9])

        if n_table == 'STOC_AUCO':
               if row[3] != None:
                  row[3] = float(row[3].replace(",", ".")) if row[3].find(",") != -1 else float(row[3])

        if n_table == 'STOC_AUVE':
               if row[3] != None:
                  row[3] = float(row[3].replace(",", ".")) if row[3].find(",") != -1 else float(row[3])

        if n_table == 'VENT_LIPV':          
               row[5] = None if row[5] == "0" or row[5] == None else datetime.strptime(row[5][0:19], '%Y-%m-%d %H:%M:%S')
               row[6] = None if row[6] == "0" or row[6] == None else datetime.strptime(row[6][0:19], '%Y-%m-%d %H:%M:%S')

        if n_table == 'STOC_ARCO':          
               row[3] = None if row[3] == "0" or row[3] == None else datetime.strptime(row[3][0:19], '%Y-%m-%d %H:%M:%S')


        if len(cursor.fetchall()) == 0:
            print('insert: ', row)
            try:
               
                cursor.execute("INSERT INTO [dbo].["+n_table+"] VALUES (" + n + ")", row)
            except Exception as exc:
              #  print 'error en: ' + "INSERT INTO [dbo].["+n_table+"] VALUES (" + n + ")"
                logging.info("--------------")
                logging.info('error en: ' + "INSERT INTO [dbo].["+n_table+"] VALUES (" + n + ")")
                logging.info(row)
                logging.info(exc)
                logging.info("--------------")
                print exc
                pass
        else:
            print('update: ', row)
            
            for x in range(tamano):
                if x > 0:
                    try:
                        cursor.execute(
                            "UPDATE [dbo].["+n_table+"] SET " + str(column_name[x]) + " = ?  WHERE "+column_name[0]+" = " +
                            row[0] + "" + compuesta,
                            row[x])                        
                    except Exception as exc:
                       
                        print 'error en: ' + "UPDATE [dbo].["+n_table+"] SET " + str(column_name[x]) + " = ?" \
                            "  WHERE "+column_name[0]+" = " +  row[0] + "" + compuesta
                        logging.info("--------------")
                        logging.info('error en: ' + "UPDATE [dbo].["+n_table+"] SET " + str(column_name[x]) + " = ?" \
                            "  WHERE "+column_name[0]+" = " +  row[0] + "" + compuesta)
                        logging.info('value:')
                        logging.info(row[x])
                        logging.info(exc)
                        logging.info("--------------")
                        print exc
                        pass
        
    cursor.execute("ALTER TABLE "+n_table+" CHECK CONSTRAINT ALL")
    conn.commit()
   



convertir('C:\\visionaris\\owncloud\\compartir_archivos\\CCOB_CLIE.csv','CCOB_CLIE',CLIE)
convertir('C:\\visionaris\\owncloud\\compartir_archivos\\VENT_ARPV.csv','VENT_ARPV',VENT)
convertir('C:\\visionaris\\owncloud\\compartir_archivos\\VENT_CLIV.csv','VENT_CLIV',CLIV)
convertir('C:\\visionaris\\owncloud\\compartir_archivos\\STOC_ARTS.csv','STOC_ARTS',ARTS)
convertir('C:\\visionaris\\owncloud\\compartir_archivos\\CCOB_IPCL.csv','CCOB_IPCL',IPLC)
convertir('C:\\visionaris\\owncloud\\compartir_archivos\\VENT_ARVI.csv','VENT_ARVI',ARVI)
convertir('C:\\visionaris\\owncloud\\compartir_archivos\\STOC_ARCO.csv','STOC_ARCO',ARCO)
convertir('C:\\visionaris\\owncloud\\compartir_archivos\\STOC_ARVE.csv','STOC_ARVE',ARVE)
convertir('C:\\visionaris\\owncloud\\compartir_archivos\\STOC_AUCO.csv','STOC_AUCO',AUCO)
convertir('C:\\visionaris\\owncloud\\compartir_archivos\\STOC_AUVE.csv','STOC_AUVE',AUVE)
convertir('C:\\visionaris\\owncloud\\compartir_archivos\\VENT_LIPV.csv','VENT_LIPV',LIPV)
convertir('C:\\visionaris\\owncloud\\compartir_archivos\\CCOB_DCLI.csv','CCOB_DCLI',DCLI)
convertir('C:\\visionaris\\owncloud\\compartir_archivos\\CCOB_VECL.csv','CCOB_VECL',VECL)

conn.close()
