from flask import Flask
from dbManager import dbManager

app = Flask('Group Project')
dbmgr = dbManager(app)

dbmgr.add(1.0)
dbmgr.add(2.0)
dbmgr.add(3.0)

#data = [r for r in dbmgr.retrieve()]

# move this stuff to the retreive function once it's done
#result = []
#for d in range(data.__len__()):
#    result.append((data[d].__dict__['id'], data[d].__dict__['duration']))



@app.route('/')
def index():
    return str(dbmgr.retrieve())

if __name__ == '__main__':
    app.run()