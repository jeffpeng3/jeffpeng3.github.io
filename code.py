import time
from random import uniform, random, randint
from wisepaasdatahubedgesdk.EdgeAgent import EdgeAgent
from wisepaasdatahubedgesdk.Model.Edge import EdgeAgentOptions, DCCSOptions, EdgeData, EdgeTag
from datetime import datetime,timezone,timedelta

class MyGateway():
    def __init__(self):
        options = EdgeAgentOptions(
            nodeId='3f81e8e6-4ecb-4034-9fb0-ecd8d10c5ea4',
            DCCS=DCCSOptions(
                apiUrl='https://api-dccs-ensaas.education.wise-paas.com/',
                credentialKey='730ea712eb6ca156dd6ce2db250530cv'
            )
        )
        self.agent = EdgeAgent(options)
        self.agent.connect()
        print("Init complete.")

    def generate_data(self) -> EdgeData:
        edgeData = EdgeData()
        edgeData.timestamp=datetime.now().astimezone(timezone(timedelta(hours=8)))
        status = 1 if random() > 0.2 else 0
        value = [
            ('dev1', 'Humidity', uniform(0, 100)),
            ('dev1', 'Temperature', uniform(10, 40)),
            ('dev1', 'PM2_5', uniform(0, 50)),
            ('dev2', 'Status', status),
            ('dev2', 'Cold_temp', uniform(10, 30) if status else 0),
            ('dev2', 'Hot_temp', uniform(90, 100) if status else 0),
            ('dev2', 'Warm_temp', uniform(30, 50) if status else 0),
            ('dev2', 'Water_level', randint(10, 20) if status else 0)
        ]
        edgeData.tagList=[*map(lambda x: EdgeTag(*x), value)]
        return edgeData

    def send(self):
        self.agent.sendData(data=self.generate_data())
if __name__ == '__main__':
    gateway = MyGateway()
    while True:
        gateway.send()
        time.sleep(2)