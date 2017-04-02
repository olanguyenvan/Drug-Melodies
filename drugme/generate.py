import random
from midiutil.MidiFile3 import MIDIFile


class GenerateMelody(object):
    def __init__(self, file, pitch, length, beat_duration):
        self.pitch = pitch
        self.length = length
        self.file = file
        self.midi_melody = MIDIFile(1)
        self.beat_duration = beat_duration

    def get_filename(self):
        if not self.file.endswith(".mid"):
            return self.file + ".mid"
        return self.file

    def get_random_pitch(self):
        step = random.randint(-5, 5)
        return abs(self.pitch + step)

    @staticmethod
    def get_random_volume():
        return random.randint(70, 200)

    def generate(self):
        time = 0
        i = 0

        self.midi_melody.addTempo(0, time, 60)
        while time < self.length:
            self.midi_melody.addNote(0, 0, self.get_random_pitch(), time,
                                     self.beat_duration, self.get_random_volume())
            time += self.beat_duration
            i += 1

        binfile = open(self.get_filename(), 'wb')
        self.midi_melody.writeFile(binfile)
        binfile.close()
