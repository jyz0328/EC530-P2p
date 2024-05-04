# P2P insturction by JINGYI ZHANG jyz0328@bu.edu
# how to run code
- step 0: remember to install socket before running code . type [pip3 install socket] before running code.
- 1. download `database.db` , or download `database.py` and run [python3 database.py] to generate database
- 2. download `app.py`, run [python3 app.py] on terminal A and B seperately
- 3. Now you can see on both terminals about the local host information, local port information and selection request. For terminal A, input 2 to waiting for receive message. While for terminal B, input 1 to send message.
- 4. Now for terminal B, enter target host and target port (the host and port you want to send message to, in ths situation just enter host and port of terminal A), enter local host and port ( the host and port of this current terminal B ),and enter message you want to sent.
- 5. Now you can see the message has been sent to terminal A.
- I also upload a `P2P_report` for you to better understand my code.
