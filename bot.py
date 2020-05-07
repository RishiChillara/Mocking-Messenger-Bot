from fbchat import log, Client
from fbchat.models import *
import credentials


def memeifyString(s):
    result = ""
    i = True
    for char in s:
        if i:
            result = result + char.upper()
        else:
            result = result + char.lower()
        if char != ' ':
            i = not i
    return result


class EchoBot(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(author_id, thread_id)
        self.markAsRead(author_id)


        # don't reply on our own messages
        if author_id != self.uid:
            self.send(Message(text = memeifyString(message_object.text)), thread_id=thread_id, thread_type=thread_type)
            self.sendRemoteFiles("https://i.kym-cdn.com/entries/icons/original/000/022/940/mockingspongebobbb.jpg", message=None, thread_id=thread_id, thread_type=thread_type)

            
client = EchoBot(credentials.email, credentials.password)
client.listen()








