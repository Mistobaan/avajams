import sys
sys.path.append("packages")

# Here is how to queue tasks from Python.
from iron_worker import *
import json
import csv 
with open(sys.argv[1]) as fd:
        dr = csv.DictReader(fd)
        cred = json.load(open("iron.json"))

        worker = IronWorker(project_id=cred['project_id'], token=cred['token'])

        for row in dr:
                print row.keys()
                task = worker.queue(code_name="mistobaan/hello",payload={"url": row['Link'] })
                print row
                print task.id
