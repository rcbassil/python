"""
Given a real-time source of data, uniquify all duplicates which were received within 10 seconds. 
The messages should be printed in the order they were received in.

Input:
foo @ 0 print foo, store foo@0
mee @ 1 print mee, store mee@1
bar @ 2 print bar, store bar@2
baz @ 5 
foo @ 8 skip foo@8; do not store
bar @ 13 print bar; store bar@13 - override previous entry
baz @ 15

Output: "foo mee bar baz bar".

"""

class Record:
  seconds # integer
  message # string

class RecordStream:
  def next():
      return
       # returns Record if any
  def has_next():
      return
     # returns boolean


def uniquify(record_stream):
   # Implement code here
    
    my_dict = {}
    
    while record_stream.has_next():

      r = record_stream.next()
      my_message = r.message
      my_time = r.seconds
      
      if my_time > my_dict[my_message] and (my_time - my_dict[my_message]) <= 10 and my_dict[my_message]:
        print(my_message)
        my_dict[my_message] = my_time 
      
      
     
      
    
      
