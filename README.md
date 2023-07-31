# sxtdemo_NYSE
Space and Time demo on pulling daily NYSE data, and loading into SxT-DB.
Currently only pulls stocks AAPL, MSFT, GOOGL, AMZN for from Jan 1st 2023, to end of July 2023 (572 rows).

TODOS:
- polish code and make more understandable (this is a rough-but-working v0.1)
- add delete before insert, or delta-processing logic so we can run more than once
- author some SxT SQL demonstrating the join of on-chain and off-chain data

