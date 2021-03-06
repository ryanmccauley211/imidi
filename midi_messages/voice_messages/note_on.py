import midi_constants
from midi_messages.midi_message import MidiMessage
from midi_common import MessageType
from utils_common import get_note_name


class NoteOn(MidiMessage):

    message_type = MessageType.NOTE_ON

    def __init__(self, bdelta, blength, bstatus, bdata):
        super().__init__(bdelta, bstatus, blength, bdata)
        self.note_val = self.bdata[0]
        self.velocity = self.bdata[1]

        self.note = get_note_name(self.note_val)

    def parse(self):
        pass

    def __str__(self):
        if self.velocity > 0:
            return "|| Note On        || {padding:10} note - {0} {padding:4} velocity - {1}".format(self.note, self.velocity, padding="")
        else:
            return "|| Note Off       || {padding:10} note - {0} {padding:4} velocity - {1}".format(self.note, self.velocity, padding="")
