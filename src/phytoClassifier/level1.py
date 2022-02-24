# -*- coding = utf-8 -*-
# @Time : 2021/6/25 23:32
# @Author : TaoJay
# @File : level1.py
# @Software : PyCharm

import sqlite3
import pkg_resources

dbpath = pkg_resources.resource_filename(__name__, "data/mclk.db")


def main():
    print("this is program psmc -> level1")


def getClassById(Id):
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    sql = "select Class from level1 where Cid = '%s' " % (Id)
    qr = cursor.execute(sql).fetchone()
    conn.close()
    if qr is None:
        return "None"
    else:
        return str(qr[0])


def getClassByName(name):
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    sql = "select Synonym,Class from level1 where Synonym like '%s' " % (
        "%"+name+"%")
    qrs = cursor.execute(sql).fetchall()
    conn.close()
    if len(qrs) == 0:
        return "None"
    elif len(qrs) == 1:
        return str(qrs[0][1])
    else:
        return str(qrs)


def getClassBySmiles(smi):
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    sql = "select Class from level1 where Smiles = '%s' " % (smi)
    qr = cursor.execute(sql).fetchone()
    conn.close()
    if qr is None:
        return "None"
    else:
        return str(qr[0])


def getClassByInChI(inchi):
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    sql = "select Class from level1 where Inchi = '%s' " % (inchi)
    qr = cursor.execute(sql).fetchone()
    conn.close()
    if qr is None:
        return "None"
    else:
        return str(qr[0])


def getClassByInChiKey(inchikey):
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    sql = "select Class from level1 where Inchikey = '%s' " % (inchikey)
    qr = cursor.execute(sql).fetchone()
    conn.close()
    if qr is None:
        return "None"
    else:
        return str(qr[0])


if __name__ == "__main__":
    main()
