"""
359. Logger Rate Limiter
Design a logger system that receive stream of messages along with its timestamps, each message should be printed if and only if it is not printed in the last 10 seconds.

Given a message and a timestamp (in seconds granularity), return true if the message should be printed in the given timestamp, otherwise returns false.

It is possible that several messages arrive roughly at the same time.

Example:
Logger logger = new Logger();
// logging string "foo" at timestamp 1
logger.shouldPrintMessage(1, "foo"); returns true; 
// logging string "bar" at timestamp 2
logger.shouldPrintMessage(2,"bar"); returns true;
// logging string "foo" at timestamp 3
logger.shouldPrintMessage(3,"foo"); returns false;
// logging string "bar" at timestamp 8
logger.shouldPrintMessage(8,"bar"); returns false;
// logging string "foo" at timestamp 10
logger.shouldPrintMessage(10,"foo"); returns false;
// logging string "foo" at timestamp 11
logger.shouldPrintMessage(11,"foo"); returns true;
"""
from collections import defaultdict
class Logger(object):
    timeStoreLen = 10

    def __init__(self):
        self.timeToMessages = defaultdict(set) 
    
    def shouldPrintMessage(self, timestamp, message):
        oldTimes = list( self.timeToMessages.keys() )
        # remove timestamps whare are too old
        for oldTime in oldTimes:
            if timestamp - oldTime >= self.timeStoreLen:
                del self.timeToMessages[ oldTime ]

        # printed same message recently?
        for oldTime in self.timeToMessages:
            if message in self.timeToMessages[oldTime]:
                return False

        self.timeToMessages[ timestamp ].add( message )
        return True

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)