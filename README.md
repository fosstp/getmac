# getmac

抓 MAC address 和電腦名稱 丟資料庫的小 script

測試環境 windows 10 64bit enterprise with winpython 3.5



# known issue

**不支援多張網卡或是含有虛擬網卡**

換句話說如果系統內有多張網卡就有可能抓錯



# installation

* Server

  * 準備一台 mysql server
  * 開一個資料庫 匯入 net_data.sql
  * 設定 getmac.py 

  ```
  db_host = '' # mysql server hostname or IP
  db_name = '' # database name
  db_user = '' # database user name
  db_pwd = ''  # database password
  ```

* client

  - 安裝 python 3.x  ( [winpython](http://winpython.github.io/) )
  - 執行 WinPython Control Panel.exe 右上 Advanced / Register distribution... 
  - 環境變數 path 加上 winpython安裝位置\scripts



# usage

執行 getmac.py 搞定收工



# License 

[WTFPL 2.0](http://www.wtfpl.net/about/)

```
      DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE 
                    Version 2, December 2004 

 Copyright (C) 2004 Sam Hocevar <sam@hocevar.net> 

 Everyone is permitted to copy and distribute verbatim or modified 
 copies of this license document, and changing it is allowed as long 
 as the name is changed. 

            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE 
   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION 

  0. You just DO WHAT THE FUCK YOU WANT TO.
```

