
CREATE TABLE SXTDEMO.STOCKS 
( Symbol         VARCHAR
 ,Stock_Date     DATE 
 ,Stock_Open     DECIMAL
 ,Stock_High     DECIMAL
 ,Stock_Low      DECIMAL
 ,Stock_Close    DECIMAL
 ,Stock_AdjClose DECIMAL
 ,Stock_Volume   BigInt
 ,PRIMARY KEY (Symbol,Stock_Date)
 ) WITH "public_key=2646D857E6EEE7B2DA19BCDBD4C834F5C4DC71BFB937D4588BD318181BB047F4, access_type=public_read"

