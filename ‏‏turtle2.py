#submitted by Keren Or Hadad 208025205
import string


class Message:

    def _init_(self, m_id, body, sender):
        self.message_id = m_id
        self.message_body = body
        self.message_sender = sender
        self.message_read = False

    def get_details(self):
        """
        The function return details of a message.
        Returns: String with message's details.
        """
        return {"Id: " + str(self.message_id) + ", Body: " + self.message_body + ", Sender: " + self.message_sender +\
                 ", Read: " + str(self.message_read)}

    def set_read(self, status_read):
        """
        The function that change status of message. Read or not read.
        Parameters
        -------
        status_read : bool
            New status of read.
        """
        self.message_read = status_read


class PostOffice:


    def _init_(self, usernames):
        self.message_id = 0
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
        message_details = Message(self.message_id, message_body, sender)
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
        return message_details.message_id

    def read_inbox(self, user, number_of_message=0):
        """
              The function return the messages of a user.

              user : str: The user's name.
              number_of_message : str: How mach message to return. If the user don't move any number, return all the message.
              Returns: list: The message in g-mail of user.
              KeyError: If the user does not exist.
        """
        # Take only message that not read.
        message_read = [message for message in self.boxes[user] if message.message_read is False]
        # Take only message the user ask.
        message_read = message_read[0:number_of_message] if number_of_message > 0 else message_read

        for message in message_read:
            message.set_read(True)

        return [message.get_details() for message in message_read]

    def search_inbox(self, user, part_message):
        """
              The function find messages (of the user) that containing the part message.

              user : str: The user's name.
              part_message : str: Sub message.
              Returns: list: The messages that containing the part message.
              KeyError: If the user does not exist.
        """
        return [message.get_details() for message in self.boxes[user]
                if str(message.message_body)._contains_(part_message)]


def the_example():

    users = ('keren', 'omer')
    post_office = PostOffice(users)

    # function send_message():
    message_id = post_office.send_message(
        sender='omer',
        recipient='keren',
        message_body='Hi keren,here is your husbend. how are you?.',
    )
    print(f"message sent Successfuly. number of message:  {message_id}.")

    message_id = post_office.send_message(
        sender='omer',
        recipient='keren',
        message_body='i want to eat with you pizza.',
    )
    print(f"message sent Successfuly. number of message:{message_id}.")

    message_id = post_office.send_message(
        sender='omer',
        recipient='keren',
        message_body='C U, keren.',
    )
    print(f"message sent Successfuly. number of message: {message_id}.")

    # function read_inbox():
    print(f'\nread_inbox with number 1: {post_office.read_inbox("keren", 1)}')
    print(f'read_inbox with number 1: {post_office.read_inbox("keren", 1)}')

    # function search_inbox():
    print(f'\nsearch_inbox - "pizza": {post_office.search_inbox("keren", "pizza")}')
    print(f'search_inbox - "bend": {post_office.search_inbox("keren", "bend")}')
    print(f'search_inbox - "keren": {post_office.search_inbox("keren", "keren")}')


the_example()

