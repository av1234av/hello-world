from datetime import datetime, timedelta
import operator
'''
Find Room To Clean - A simple data analysis problem
Description:
A janitorial staff would like to clean rooms that are the most dirty. We define 'dirty' as 'having the most foot traffic'.
Rooms in the business all have badge readers which are swiped to either get in or out of a room. We'd like to create a
system which tracks each badge swipe and can tell us which room has had the most foot traffic at the current time.

Tech Setup
----------
Each badge sends the info about the person and the door on each swipe:
|person|door
------------
| p1   | d1

Each swipe is at the current time. Here's an example of several swipes happening over time:
| person | door | time
----------------------
| p1     | d1   | 0
| p2     | d2   | 10
| p1     | d1   | 10
| p1     | d2   | 15

Person 1 entered door 1 at time 0, left at time 10, and entered door 2 at time 15.
Person 2 entered door 2 at 1ime 10.

if we had asked to find a room to clean at time 10, Person 1 had been in door 1 for 10 units, Person 2 had been in
door 2 for 0 units. Door 1 has a total of 10 units of foot traffic compared to door 2 with 0 units, so we clean door 1.

If we had asked to find a room to clean at 20: Person 1 was in door 1 for 10 units and had been in door 2 for 5 units,
Person 2 had been in door 2 for 10 units. Door 2 has a total of 15 units of foot traffic compared to door 1 with 10
units, so we clean door 2.

Note that we can clean rooms that still have people in them. Also we're only interested in finding a room to clean at the
current time, and don't need to worry about historical data.

Hint:
Two functions...
swipe(door, time)
room_to_clean()
'''

class DoorSwipe(object):
    def __init__(self, person, ttime):
        '''
        DoorSwipe class to record entry/exit of a person and keeps a running count of traffic (time spent in the room)
        :param person: person name
        :param ttime: entry time
        '''
        self.person_map=dict()
        self.currentTraffic = timedelta(0)
        self.new_swipe(person, ttime)

    def new_swipe(self, person, ttime):
        '''
        Add a new swipe. If the person is already in the room then it is an exit.
        So add to the currentTraffic for the room by subtracting the entry time from person's
        exit time. The person entry is removed from person_map as he/she is no longer occupying the room.
        :param person: person name, it is the key for person map
        :param ttime: entry/exit time
        :return: None
        '''
        _time = self.person_map.get(person)
        if _time:
            self.currentTraffic += ttime - _time
            del self.person_map[person]
        else:
            self.person_map[person] = ttime

    def get_foot_traffic(self, ttime=datetime.now()):
        '''
        Get Foot traffic based on current Traffic already recorded
        plus the time all people who are still in the room.

        :param ttime:
        :return: total foot traffic for the room
        '''

        foot_traffic = self.currentTraffic
        for person, _time in self.person_map.items():
            foot_traffic +=  ttime - _time
        return foot_traffic

    def room_cleaned(self, ttime=datetime.now()):
        '''
        Clean room means time should be reset
        :param ttime: time the room is cleaned
        :return: None
        '''
        self.currentTraffic = timedelta(0)
        for person in self.person_map.items():
            self.person_map[person]=ttime

door_map = {}


def swipe(person, door, ttime=datetime.now()):
    '''
    Swipe the entry/exit to the room. It save the entry in the 'door_map' hashmap
    :param person: person name
    :param door: door id
    :param ttime: time of swipe
    :return: None
    '''
    doorObj = door_map.get(door,None)
    if not doorObj:
        door_map[door] = DoorSwipe(person, ttime)
    else:
        door_map[door].new_swipe(person, ttime)


def get_room_to_clean(ttime=datetime.now()):
    '''
    Get the foot traffic of all the rooms and returns the 'dirtiest' room based on the largest foot traffic
    :param ttime:
    :return: max_val
    '''
    ll=[]
    for door, obj in door_map.items():
        traffic = obj.get_foot_traffic(ttime)
        print(door, traffic)
        ll.append((door, traffic))

    room_to_clean = max(ll, key=operator.itemgetter(1))[0]
    return room_to_clean

if __name__ == '__main__':
    t = datetime.now()
    swipe('p1', 'd1', t)
    t1 = t+timedelta(seconds=10)
    swipe('p2', 'd2', t1)
    swipe('p1', 'd1', t1)
    t2 = t1+timedelta(seconds=5)
    swipe('p1', 'd2', t2)
    # swipe('p1','d1',t2)
    print('Room to Clean: {}'.format(get_room_to_clean(t2+timedelta(seconds=5))))