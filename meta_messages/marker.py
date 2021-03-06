from meta_messages.meta_message import MetaMessage
from midi_exceptions import IncorrectStatusException
from midi_common import MessageType


class Marker(MetaMessage):

    btype = b'\x06'
    message_type = MessageType.MARKER
    name  = "marker"

    def __init__(self, bdelta, bstatus, blength, bdata):
        super().__init__(bdelta, bstatus, blength, bdata)
        if bstatus != b'\xFF':
            raise IncorrectStatusException("Invalid status: {:2x} for meta event".format(bstatus))
        self.marker = ""

    def parse(self):
        self.marker = self.bdata.decode("utf-8")
