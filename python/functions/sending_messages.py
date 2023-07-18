def make_messages(msg):
  for messages in msg:
    letter = f" {messages}: "
    print(letter)
    
message_in_a_bottle = ['long message 1', 'really long message 2','really really long message 3']
make_messages(message_in_a_bottle)