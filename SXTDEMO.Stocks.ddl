/*
# read/write:
BISCUIT=Ep0CCrIBCg5zeHQ6Y2FwYWJpbGl0eQoKZHFsX3NlbGVjdAoOc3h0ZGVtby5zdG9ja3MKCmRtbF9pbnNlcnQKCmRtbF91cGRhdGUKCWRtbF9tZXJnZQoKZG1sX2RlbGV0ZRgDIg8KDQiACBIDGIEIEgMYgggiDwoNCIAIEgMYgwgSAxiCCCIPCg0IgAgSAxiECBIDGIIIIg8KDQiACBIDGIUIEgMYgggiDwoNCIAIEgMYhggSAxiCCBIkCAASILUgtm8mLLuBpIwFCZP21r3a4O59_-e3hIPw5oesCQVnGkAHvoXKuaMOF0KvV2xT2GF57t-lyq4woJUoIg66tM-qk_RKdQqPkz0Zd1ua8y3sb-8JF62wuFNb59skFPxSd5YHIiIKIPJSFK0dTWKSfhFexG5qNBRd7VC_F-fmsXDQTptV6HRs
*/

CREATE TABLE SXTDEMO.STOCKS 
( Symbol         VARCHAR
 ,Stock_Date     DATE 
 ,Stock_Open     DECIMAL(18,2)
 ,Stock_High     DECIMAL(18,2)
 ,Stock_Low      DECIMAL(18,2)
 ,Stock_Close    DECIMAL(18,2)
 ,Stock_AdjClose DECIMAL(18,2)
 ,Stock_Volume   BigInt
 ,PRIMARY KEY (Symbol,Stock_Date)
 ) WITH "public_key=2646D857E6EEE7B2DA19BCDBD4C834F5C4DC71BFB937D4588BD318181BB047F4, access_type=public_read"

