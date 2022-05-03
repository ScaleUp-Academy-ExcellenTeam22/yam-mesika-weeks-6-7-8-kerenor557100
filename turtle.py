#submitted by Keren Or Hadad 208025205

import string


class PostOffice:

    def __init__(self, usernames):
        self.message_id = 0
        self.read = False
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient, message_body, urgent=False):
        """
        Send a message to a recipient.

        sender : str :The message sender's username.
        recipient : str: The message recipient's username.
        message_body : str: The body of the message.
        urgent : bool, optional:The urgency of the message. Urgent messages appear first.
        Returns: int: The message ID, auto incremented number.
        KeyError: If the recipient does not exist.

        """
        user_box = self.boxes[recipient]
        self.message_id = self.message_id + 1
        message_details = {
            'id': self.message_id,
            'body': message_body,
            'sender': sender,
            'read': self.read
        }
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
        return self.message_id

    def read_inbox(self, user, number_of_message=0):
        """
        The function return the messages of a user.

        user : str: The user's name.
        number_of_message : str: How mach message to return. If the user don't move any number, return all the message.
        Returns: list: The message in g-mail of user.
        KeyError: If the user does not exist.
        """

        len_message = len(self.boxes[user])
        # Take only message that not read.
        message_read = [message for message in self.boxes[user] if message['read'] is False]
        # Take only message the user ask.
        message_read = message_read[0:number_of_message] if number_of_message > 0 else message_read

        for message in message_read:
            for i in range(len_message):
                if self.boxes[user][i]['id'] == message['id']:
                    self.boxes[user][i]['read'] = True

        return message_read

    def search_inbox(self, user, part_message):
        """
        The function find messages (of the user) that containing the part message.

        user : str: The user's name.
        part_message : str: Sub message.
        Returns: list: The messages that containing the part message.
        KeyError: If the user does not exist.
        """
        return [message for message in self.boxes[user] if str(message['body']).__contains__(part_message)]


def the_example():
    users = ('keren', 'omer')
    post_office = PostOffice(users)

    # function send_message():
    message_id = post_office.send_message(
        sender='omer',
        recipient='keren',
        message_body='Hi keren,here is your husbend. how are you?.',
    )
    print(f"message sent Successfuly. number of message: {message_id}.")

    message_id = post_office.send_message(
        sender='omer',
        recipient='keren',
        message_body='i want to eat with you pizza.',
    )
    print(f"message sent Successfuly. number of message: {message_id}.")

    message_id = post_office.send_message(
        sender='omer',
        recipient='keren',
        message_body='C U, keren.',
    )
    print(f"Smessage sent Successfuly. number of message: {message_id}.")

    # function read_inbox():
    print(f'\nread_inbox with number 1: {post_office.read_inbox("keren", 1)}')
    print(f'read_inbox with number 1: {post_office.read_inbox("keren", 1)}')

    # function search_inbox():
    print(f'\nsearch_inbox - "pizza": {post_office.search_inbox("keren", "pizza")}')
    print(f'search_inbox - "bend": {post_office.search_inbox("keren", "bend")}')
    print(f'search_inbox - "keren": {post_office.search_inbox("keren", "keren")}')


the_example()
"""
output:
message sent Successfuly. number of message: 1.
message sent Successfuly. number of message: 2.
Smessage sent Successfuly. number of message: 3.

read_inbox with number 1: [{'id': 1, 'body': 'Hi keren,here is your husbend. how are you?.', 'sender': 'omer', 'read': True}]
read_inbox with number 1: [{'id': 2, 'body': 'i want to eat with you pizza.', 'sender': 'omer', 'read': True}]

search_inbox - "pizza": [{'id': 2, 'body': 'i want to eat with you pizza.', 'sender': 'omer', 'read': True}]
search_inbox - "bend": [{'id': 1, 'body': 'Hi keren,here is your husbend. how are you?.', 'sender': 'omer', 'read': True}]
search_inbox - "keren": [{'id': 1, 'body': 'Hi keren,here is your husbend. how are you?.', 'sender': 'omer', 'read': True}, {'id': 3, 'body': 'C U, keren.', 'sender': 'omer', 'read': False}]
"""
nums = [1,1,1]
for i in nums:
    nums[i] = 2

print(nums)