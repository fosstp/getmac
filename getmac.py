#!/usr/bin/env python3
import os
import uuid
import mysql.connector as sql

db_host = ''
db_name = ''
db_user = ''
db_pwd = ''

hostname = os.environ['COMPUTERNAME']
mac_addr = hex(uuid.getnode()).replace('0x', '').upper()
try:
    conn = sql.connect(host=db_host, database=db_name,
                       user=db_user, passwd=db_pwd)
except:
    # print ("資料庫連結失敗")
    input("資料庫連結失敗 請按 Enter 結束...")
    exit()

# insert


def ins(hostname, mac_addr):
    ins_data = (hostname, mac_addr)
    c = conn.cursor()
    q = ("INSERT INTO net_data (name, mac) VALUES (%s, %s)")
    a = c.execute(q, ins_data)
    conn.commit()
    c.close()

# update


def upd(hostname, mac_addr):
    upd_data = (hostname, mac_addr)
    c = conn.cursor()
    q = ("UPDATE net_data SET name = %s WHERE mac = %s")
    a = c.execute(q, upd_data)
    conn.commit()
    c.close()

# check duplicate


def is_duplicate(mac_addr):
    c = conn.cursor()
    q = ("SELECT id FROM net_data WHERE mac = %s")
    a = c.execute(q, (mac_addr,))
    r = c.fetchone()
    if r:
        return True
    else:
        return False


def main():
    if is_duplicate(mac_addr):
        upd(hostname, mac_addr)
    else:
        ins(hostname, mac_addr)
    pass

if __name__ == "__main__":
        main()

