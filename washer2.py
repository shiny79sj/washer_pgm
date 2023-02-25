class Washer:
    def __init__(self,brand,origin,model,load_capacity,normal_cycle_duration):
        self.brand=brand
        self.origin=origin
        self.model=model
        self.load_capacity=load_capacity
        self.normal_cycle_duration=normal_cycle_duration
    def washer_data(self):
        data=f"Brand : {self.brand}\nOrigin : { self.origin}\nModel : {self.model}\nLoad_capacity : {self.load_capacity}\nNormal_cycle_duration : {self.normal_cycle_duration}" 
        return data
washer1=Washer("Siemens","Germany","iq800","10kg","1hour")
washer2=Washer("LG","South korea","LG3768IREG","7.5kg","58minutes")
washer3=Washer("Samsung","Korea","WQ875TDE","7kg","50minutes")
print("_______________________________________")
print(washer1.washer_data())
print("_______________________________________")
print(washer2.washer_data())
print("_______________________________________")
print(washer3.washer_data())
print("_______________________________________")
    
    