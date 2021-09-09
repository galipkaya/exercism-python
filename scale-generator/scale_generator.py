class Note:
    def __init__(self, note, next_whole=None, next_sharp=None, next_flat=None):
        self.note = note
        self.next_whole = next_whole
        self.next_sharp = next_sharp
        self.next_flat = next_flat

    def __str__(self):
        return self.note


FLATS = ["Bb", "Db", "Eb", "Gb", "Ab", "F", "g"]

note_A = Note("A")
note_A_sharp = Note("A#")
note_B = Note("B")
note_B_flat = Note("Bb")
note_C = Note("C")
note_C_sharp = Note("C#")
note_D_flat = Note("Db")
note_D = Note("D")
note_D_sharp = Note("D#")
note_E_flat = Note("Eb")
note_E = Note("E")
note_F = Note("F")
note_F_sharp = Note("F#")
note_G_flat = Note("Gb")
note_G = Note("G")
note_G_sharp = Note("G#")
note_A_flat = Note("Ab")

note_A.next_whole = note_B
note_A.next_sharp = note_A_sharp
note_A.next_flat = note_B_flat
note_A_sharp.next_whole = note_B
note_B_flat.next_whole = note_B
note_B.next_whole = note_C
note_C.next_whole = note_D
note_C.next_sharp = note_C_sharp
note_C.next_flat = note_D_flat
note_C_sharp.next_whole = note_D
note_D_flat.next_whole = note_D
note_D.next_whole = note_E
note_D.next_sharp = note_D_sharp
note_D.next_flat = note_E_flat
note_D_sharp.next_whole = note_E
note_E_flat.next_whole = note_E
note_E.next_whole = note_F
note_F.next_whole = note_G
note_F.next_sharp = note_F_sharp
note_F.next_flat = note_G_flat
note_F_sharp.next_whole = note_G
note_G.next_whole = note_A
note_G.next_sharp = note_G_sharp
note_G.next_flat = note_A_flat
note_G_flat.next_whole = note_G
note_G_sharp.next_whole = note_A
note_A_flat.next_whole = note_A

NOTE_DICT = {
    "A": note_A,
    "A#": note_A_sharp,
    "B": note_B,
    "C": note_C,
    "C#": note_C_sharp,
    "D": note_D,
    "D#": note_D_sharp,
    "E": note_E,
    "F": note_F,
    "F#": note_F_sharp,
    "G": note_G,
    "G#": note_G_sharp,
    "Bb": note_B_flat,
    "Db": note_D_flat,
    "Eb": note_E_flat,
    "Gb": note_G_flat,
    "Ab": note_A_flat
}


class Scale:
    def __init__(self, tonic):
        self.chromatic_array = []
        orig_tonic = tonic
        ch = tonic[0].upper()
        if len(tonic) == 2:
            tonic = ch + tonic[1]
        else:
            tonic = ch
        self.start = NOTE_DICT[tonic]
        self.use_flat = self.start.note in FLATS or orig_tonic == "g" or orig_tonic == "d"
        tmp = self.start
        while True:
            self.chromatic_array.append(tmp.note)
            if tonic == "C":
                if tmp.next_sharp is not None:
                    tmp = tmp.next_sharp
                else:
                    tmp = tmp.next_whole
            elif tonic == "F":
                if tmp.next_flat is not None:
                    tmp = tmp.next_flat
                else:
                    tmp = tmp.next_whole
            if tmp == self.start:
                break

    def chromatic(self):
        return self.chromatic_array

    # A, A#, B, C, C#, D, D#, E, F, F#, G, G#
    # A, Bb, B, C, Db, D, Eb, E, F, Gb, G, Ab
    # MmMMmAm - "D", "E", "F", "G", "A", "Bb", "Db"
    def interval(self, intervals):
        result = []
        tmp = self.start
        for ch in intervals:
            result.append(tmp.note)

            if ch == "A":
                if tmp.next_whole.next_sharp is not None:
                    tmp = tmp.next_whole.next_sharp.next_whole
                else:
                    if self.use_flat:
                        tmp = tmp.next_whole.next_whole.next_flat
                    else:
                        tmp = tmp.next_whole.next_whole.next_sharp
            elif ch == "M":
                if tmp.next_sharp is None:
                    if tmp.next_whole.next_sharp is not None:
                        if self.use_flat:
                            tmp = tmp.next_whole.next_flat
                        else:
                            tmp = tmp.next_whole.next_sharp
                    else:
                        tmp = tmp.next_whole.next_whole
                else:
                    tmp = tmp.next_whole
            elif tmp.next_sharp is not None:
                if self.use_flat:
                    tmp = tmp.next_flat
                else:
                    tmp = tmp.next_sharp
            else:
                tmp = tmp.next_whole

            if tmp == self.start:
                break

        return result
