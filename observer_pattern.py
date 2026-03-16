#!/usr/bin/env python3
"""Observer pattern — pub/sub with topic-based filtering."""
from collections import defaultdict
class EventBus:
    def __init__(self):self.subscribers=defaultdict(list)
    def subscribe(self,topic,callback):self.subscribers[topic].append(callback)
    def unsubscribe(self,topic,callback):
        if topic in self.subscribers: self.subscribers[topic].remove(callback)
    def publish(self,topic,*args,**kwargs):
        for cb in self.subscribers.get(topic,[]):cb(*args,**kwargs)
        for cb in self.subscribers.get("*",[]):cb(topic,*args,**kwargs)
def main():
    bus=EventBus();log=[]
    bus.subscribe("user.login",lambda u:log.append(f"login:{u}"))
    bus.subscribe("user.logout",lambda u:log.append(f"logout:{u}"))
    bus.publish("user.login","alice");bus.publish("user.logout","bob")
    print(f"Log: {log}")
if __name__=="__main__":main()
