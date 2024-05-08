

class ACSensor:
    def __init__(self, temprature, humidity, pressure, position, flow, vibration):
        self.temprature = temprature
        self.humidity = humidity
        self.pressure = pressure
        self.position = position
        self.flow = flow
        self.vibration = vibration

    # when sending data from iot to kafka I have to have in the form of
    # json. So first converting into dic
    def to_dict(self):
        return self.__dict__
ac_sensor_reading = ACSensor(temprature=3, humidity=3, pressure=8, position=7, flow= 4, vibration=7)
# serelizing into the format of dictionary
print(ac_sensor_reading.to_dict())

