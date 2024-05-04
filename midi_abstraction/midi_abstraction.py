#!/usr/bin/env python3
from dataclasses import dataclass
from enum import Enum

VELOCITY_MIN = 0
VELOCITY_MAX = 127


class Note(str, Enum):
    C = "c"
    CS = "cs"
    DB = "db"
    D = "d"
    DS = "ds"
    EB = "eb"
    E = "e"
    ES = "es"
    F = "f"
    FS = "fs"
    GB = "gb"
    G = "g"
    GS = "gs"
    AB = "ab"
    A = "a"
    AS = "as"
    BB = "bb"
    B = "b"


NOTES = {
    Note.C: [i * 12 for i in range(0, 11)],
    Note.CS: [i * 12 + 1 for i in range(0, 11)],
    Note.DB: [i * 12 + 1 for i in range(0, 11)],
    Note.D: [i * 12 + 2 for i in range(0, 11)],
    Note.DS: [i * 12 + 3 for i in range(0, 11)],
    Note.EB: [i * 12 + 3 for i in range(0, 11)],
    Note.E: [i * 12 + 4 for i in range(0, 11)],
    Note.F: [i * 12 + 5 for i in range(0, 11)],
    Note.FS: [i * 12 + 6 for i in range(0, 11)],
    Note.GB: [i * 12 + 6 for i in range(0, 11)],
    Note.G: [i * 12 + 7 for i in range(0, 11)],
    Note.GS: [i * 12 + 8 for i in range(0, 9)],
    Note.AB: [i * 12 + 8 for i in range(0, 9)],
    Note.A: [i * 12 + 9 for i in range(0, 9)],
    Note.AS: [i * 12 + 10 for i in range(0, 9)],
    Note.BB: [i * 12 + 10 for i in range(0, 9)],
    Note.B: [i * 12 + 11 for i in range(0, 9)],
}


class Chord(str, Enum):
    AB_MINOR = "ab_minor"
    AB_DIM = "ab_dim"
    A_MINOR = "a_minor"
    A_MINOR_SEVENTH = "a_minor_seventh"
    AS_DIM = "as_dim"
    AS_MINOR_SEVENTH_FLAT_FIVE = "as_minor_seventh_flat_five"
    AS_MAJOR = "as_major"
    AS_MINOR = "as_minor"
    A_MAJOR = "a_major"
    A_DIM = "a_dim"
    A_MAJOR_SEVENTH = "a_major_seventh"
    A_DOM_SEVENTH = "a_dom_seventh"
    AB_MAJOR = "ab_major"
    AB_MAJOR_SEVENTH = "ab_major_seventh"
    BB_MINOR = "bb_minor"
    BB_DIM = "bb_dim"
    BB_MAJOR_SEVENTH = "bb_major_seventh"
    BB_MAJOR = "bb_major"
    BB_DOM_SEVENTH = "bb_dom_seventh"
    B_DIM = "b_dim"
    B_MINOR_SEVENTH_FLAT_FIVE = "b_minor_seventh_flat_five"
    B_MAJOR = "b_major"
    B_MAJOR_SEVENTH = "b_major_seventh"
    B_MINOR = "b_minor"
    B_MINOR_SEVENTH = "b_minor_seventh"
    CS_DIM = "cs_dim"
    CS_MAJOR = "cs_major"
    CS_MINOR_SEVENTH_FLAT_FIVE = "cs_minor_seventh_flat_five"
    CS_MINOR = "cs_minor"
    CS_MINOR_SEVENTH = "cs_minor_seventh"
    C_MAJOR = "c_major"
    C_DIM = "c_dim"
    C_MAJOR_SEVENTH = "c_major_seventh"
    C_MINOR = "c_minor"
    C_MINOR_SEVENTH = "c_minor_seventh"
    C_DOM_SEVENTH = "c_dom_seventh"
    DB_DIM = "db_dim"
    DB_MAJOR = "db_major"
    DS_MAJOR = "ds_major"
    DS_DIM = "ds_dim"
    DS_MINOR = "ds_minor"
    DS_MINOR_SEVENTH = "ds_minor_seventh"
    D_MAJOR = "d_major"
    D_MAJOR_SEVENTH = "d_major_seventh"
    D_MINOR = "d_minor"
    D_MINOR_SEVENTH = "d_minor_seventh"
    D_DIM = "d_dim"
    D_MINOR_SEVENTH_FLAT_FIVE = "d_minor_seventh_flat_five"
    DB_MINOR = "db_minor"
    E_MAJOR = "e_major"
    E_MAJOR_SEVENTH = "e_major_seventh"
    E_DOM_SEVENTH = "e_dom_seventh"
    E_MINOR = "e_minor"
    E_MINOR_SEVENTH = "e_minor_seventh"
    EB_MAJOR = "eb_major"
    EB_MAJOR_SEVENTH = "eb_major_seventh"
    EB_MINOR = "eb_minor"
    EB_DIM = "eb_dim"
    E_DIM = "e_dim"
    E_MINOR_SEVENTH_FLAT_FIVE = "e_minor_seventh_flat_five"
    FS_MINOR = "fs_minor"
    FS_MINOR_SEVENTH = "fs_minor_seventh"
    F_MAJOR = "f_major"
    F_DIM = "f_dim"
    F_MAJOR_SEVENTH = "f_major_seventh"
    FS_MAJOR = "fs_major"
    FS_DIM = "fs_dim"
    FS_DOM_SEVENTH = "fs_dom_seventh"
    F_MINOR = "f_minor"
    GB_MAJOR = "gb_major"
    GB_DIM = "gb_dim"
    GB_MINOR = "gb_minor"
    GS_MAJOR = "gs_major"
    GS_MINOR = "gs_minor"
    GS_MINOR_SEVENTH = "gs_minor_seventh"
    GS_DIM = "gs_dim"
    GS_MINOR_SEVENTH_FLAT_FIVE = "gs_minor_seventh_flat_five"
    G_MAJOR = "g_major"
    G_DIM = "g_dim"
    G_DOM_SEVENTH = "g_dom_seventh"
    G_MAJOR_SEVENTH = "g_major_seventh"
    G_MINOR = "g_minor"
    G_MINOR_SEVENTH = "g_minor_seventh"


CHORDS = {
    Chord.AB_MINOR: [Note.AB, Note.B, Note.EB],
    Chord.AB_DIM: [Note.AB, Note.B, Note.D],
    Chord.A_MINOR: [Note.A, Note.C, Note.E],
    Chord.A_MINOR_SEVENTH: [Note.A, Note.C, Note.E, Note.G],
    Chord.AS_DIM: [Note.AS, Note.CS, Note.E],
    Chord.AS_MINOR_SEVENTH_FLAT_FIVE: [Note.AS, Note.CS, Note.E, Note.GS],
    Chord.AS_MAJOR: [Note.AS, Note.D, Note.F],
    Chord.AS_MINOR: [Note.AS, Note.CS, Note.F],
    Chord.A_MAJOR: [Note.A, Note.CS, Note.E],
    Chord.A_DIM: [Note.A, Note.C, Note.EB],
    Chord.A_MAJOR_SEVENTH: [Note.A, Note.CS, Note.E, Note.GS],
    Chord.A_DOM_SEVENTH: [Note.A, Note.CS, Note.E, Note.G],
    Chord.AB_MAJOR: [Note.AB, Note.C, Note.EB],
    Chord.AB_MAJOR_SEVENTH: [Note.AB, Note.C, Note.EB, Note.G],
    Chord.BB_MINOR: [Note.BB, Note.DB, Note.F],
    Chord.BB_DIM: [Note.BB, Note.DB, Note.G],
    Chord.BB_MAJOR_SEVENTH: [Note.BB, Note.D, Note.F, Note.A],
    Chord.BB_MAJOR: [Note.BB, Note.D, Note.F],
    Chord.BB_DOM_SEVENTH: [Note.BB, Note.D, Note.F, Note.AB],
    Chord.B_DIM: [Note.B, Note.D, Note.F],
    Chord.B_MINOR_SEVENTH_FLAT_FIVE: [Note.B, Note.D, Note.F, Note.A],
    Chord.B_MAJOR: [Note.B, Note.DS, Note.FS],
    Chord.B_MAJOR_SEVENTH: [Note.B, Note.DS, Note.FS, Note.AS],
    Chord.B_MINOR: [Note.B, Note.D, Note.FS],
    Chord.B_MINOR_SEVENTH: [Note.B, Note.D, Note.FS, Note.A],
    Chord.CS_DIM: [Note.CS, Note.E, Note.G],
    Chord.CS_MAJOR: [Note.CS, Note.F, Note.G],
    Chord.CS_MINOR_SEVENTH_FLAT_FIVE: [Note.CS, Note.E, Note.G, Note.B],
    Chord.CS_MINOR: [Note.CS, Note.E, Note.GS],
    Chord.CS_MINOR_SEVENTH: [Note.CS, Note.E, Note.GS, Note.B],
    Chord.C_MAJOR: [Note.C, Note.E, Note.G],
    Chord.C_DIM: [Note.C, Note.EB, Note.GB],
    Chord.C_MAJOR_SEVENTH: [Note.C, Note.E, Note.G, Note.B],
    Chord.C_MINOR: [Note.C, Note.EB, Note.G],
    Chord.C_MINOR_SEVENTH: [Note.C, Note.EB, Note.G, Note.BB],
    Chord.C_DOM_SEVENTH: [Note.C, Note.E, Note.G, Note.BB],
    Chord.DB_DIM: [Note.DB, Note.E, Note.GS],
    Chord.DB_MINOR: [Note.DB, Note.E, Note.AB],
    Chord.DB_MAJOR: [Note.DB, Note.F, Note.AB],
    Chord.DS_MAJOR: [Note.DS, Note.G, Note.AS],
    Chord.DS_DIM: [Note.DS, Note.FS, Note.A],
    Chord.DS_MINOR: [Note.DS, Note.FS, Note.AS],
    Chord.DS_MINOR_SEVENTH: [Note.DS, Note.FS, Note.AS, Note.CS],
    Chord.D_MAJOR: [Note.D, Note.FS, Note.A],
    Chord.D_MAJOR_SEVENTH: [Note.D, Note.FS, Note.A, Note.CS],
    Chord.D_MINOR: [Note.D, Note.F, Note.A],
    Chord.D_MINOR_SEVENTH: [Note.D, Note.F, Note.A, Note.C],
    Chord.D_DIM: [Note.D, Note.F, Note.AB],
    Chord.D_MINOR_SEVENTH_FLAT_FIVE: [Note.D, Note.F, Note.AB, Note.C],
    Chord.E_MAJOR: [Note.E, Note.GS, Note.B],
    Chord.E_MAJOR_SEVENTH: [Note.E, Note.GS, Note.B, Note.DS],
    Chord.E_DOM_SEVENTH: [Note.E, Note.GS, Note.B, Note.D],
    Chord.E_MINOR: [Note.E, Note.G, Note.B],
    Chord.E_MINOR_SEVENTH: [Note.E, Note.G, Note.B, Note.D],
    Chord.EB_MAJOR: [Note.EB, Note.G, Note.BB],
    Chord.EB_MAJOR_SEVENTH: [Note.EB, Note.G, Note.BB, Note.D],
    Chord.EB_MINOR: [Note.EB, Note.GB, Note.BB],
    Chord.EB_DIM: [Note.EB, Note.GB, Note.A],
    Chord.E_DIM: [Note.E, Note.G, Note.BB],
    Chord.E_MINOR_SEVENTH_FLAT_FIVE: [Note.E, Note.G, Note.BB, Note.D],
    Chord.FS_MINOR: [Note.FS, Note.A, Note.CS],
    Chord.FS_MINOR_SEVENTH: [Note.FS, Note.A, Note.CS, Note.E],
    Chord.F_MAJOR: [Note.F, Note.A, Note.C],
    Chord.F_DIM: [Note.F, Note.AB, Note.B],
    Chord.F_MAJOR_SEVENTH: [Note.F, Note.A, Note.C, Note.E],
    Chord.FS_MAJOR: [Note.FS, Note.AS, Note.CS],
    Chord.FS_DIM: [Note.FS, Note.A, Note.C],
    Chord.FS_DOM_SEVENTH: [Note.FS, Note.AS, Note.CS, Note.E],
    Chord.F_MINOR: [Note.F, Note.AB, Note.C],
    Chord.GB_MAJOR: [Note.GB, Note.BB, Note.DB],
    Chord.GB_MINOR: [Note.GB, Note.A, Note.DB],
    Chord.GB_DIM: [Note.GB, Note.BB, Note.DB],
    Chord.GS_MAJOR: [Note.GS, Note.C, Note.DS],
    Chord.GS_MINOR: [Note.GS, Note.B, Note.DS],
    Chord.GS_MINOR_SEVENTH: [Note.GS, Note.B, Note.DS, Note.FS],
    Chord.GS_DIM: [Note.GS, Note.B, Note.D],
    Chord.GS_MINOR_SEVENTH_FLAT_FIVE: [Note.GS, Note.B, Note.D, Note.FS],
    Chord.G_MAJOR: [Note.G, Note.B, Note.D],
    Chord.G_DIM: [Note.G, Note.BB, Note.DB],
    Chord.G_DOM_SEVENTH: [Note.G, Note.B, Note.D, Note.F],
    Chord.G_MAJOR_SEVENTH: [Note.G, Note.B, Note.D, Note.FS],
    Chord.G_MINOR: [Note.G, Note.BB, Note.D],
    Chord.G_MINOR_SEVENTH: [Note.G, Note.BB, Note.D, Note.F],
}


RELATIVE_CHORD = {
    Chord.C_MAJOR: Chord.A_MINOR,
    Chord.G_MAJOR: Chord.E_MINOR,
    Chord.D_MAJOR: Chord.B_MINOR,
    Chord.A_MAJOR: Chord.FS_MINOR,
    Chord.E_MAJOR: Chord.CS_MINOR,
    Chord.B_MAJOR: Chord.GS_MINOR,
    Chord.FS_MAJOR: Chord.DS_MINOR,
    Chord.CS_MAJOR: Chord.AS_MINOR,
    Chord.F_MAJOR: Chord.D_MINOR,
    Chord.BB_MAJOR: Chord.G_MINOR,
    Chord.EB_MAJOR: Chord.C_MINOR,
    Chord.AB_MAJOR: Chord.F_MINOR,
    Chord.DB_MAJOR: Chord.BB_MINOR,
    Chord.GB_MAJOR: Chord.EB_MINOR,
    Chord.B_MAJOR: Chord.AB_MINOR,
    Chord.A_MINOR: Chord.C_MAJOR,
    Chord.E_MINOR: Chord.G_MAJOR,
    Chord.B_MINOR: Chord.D_MAJOR,
    Chord.FS_MINOR: Chord.A_MAJOR,
    Chord.CS_MINOR: Chord.E_MAJOR,
    Chord.GS_MINOR: Chord.B_MAJOR,
    Chord.DS_MINOR: Chord.FS_MAJOR,
    Chord.AS_MINOR: Chord.CS_MAJOR,
    Chord.D_MINOR: Chord.F_MAJOR,
    Chord.G_MINOR: Chord.BB_MAJOR,
    Chord.C_MINOR: Chord.EB_MAJOR,
    Chord.F_MINOR: Chord.AB_MAJOR,
    Chord.BB_MINOR: Chord.DB_MAJOR,
    Chord.EB_MINOR: Chord.GB_MAJOR,
    Chord.AB_MINOR: Chord.B_MAJOR,
}


class Drum(int, Enum):
    ACOUSTIC_BASE_DRUM = 35
    BASS_DRUM_1 = 36
    SIDE_STICK = 37
    ACOUSTIC_SNARE = 38
    HAND_CLAP = 39
    ELECTRIC_SNARE = 40
    LOW_FLOOR_TOM = 41
    CLOSED_HI_HAT = 42
    HIGH_FLOOR_TOM = 43
    PEDAL_HI_HAT = 44
    LOW_TOM = 45
    OPEN_HI_HAT = 46
    LOW_MID_TOM = 47
    HI_MID_TOM = 48
    CRASH_CYMBAL_1 = 49
    HIGH_TOM = 50
    RIDE_CYMBAL_1 = 51
    CHINESE_CYMBAL = 52
    RIDE_BELL = 53
    TAMBOURINE = 54
    SPLASH_CYMBAL = 55
    COWBELL = 56
    CRASH_CYMBAL_2 = 57
    VIBRASLAP = 58
    RIDE_CYMBAL_2 = 59
    HI_BONGO = 60
    LOW_BONGO = 61
    MUTE_HI_CONGA = 62
    OPEN_HI_CONGA = 63
    LOW_CONGA = 64
    HIGH_TIMBALE = 65
    LOW_TIMBALE = 66
    HIGH_AGOGO = 67
    LOW_AGOGO = 68
    CABASA = 69
    MARACAS = 70
    SHORT_WHISTLE = 71
    LONG_WHISTLE = 72
    SHORT_GUIRO = 73
    LONG_GUIRO = 74
    CLAVES = 75
    HI_WOOD_BLOCK = 76
    LOW_WOOD_BLOCK = 77
    MUTE_CUICA = 78
    OPEN_CUICA = 79
    MUTE_TRIANGLE = 80
    OPEN_TRIANGLE = 81


ENHARMONIC = {
    Note.CS: Note.DB,
    Note.DS: Note.EB,
    Note.FS: Note.GB,
    Note.GS: Note.AB,
    Note.AS: Note.BB,
    Note.DB: Note.CS,
    Note.EB: Note.DS,
    Note.GB: Note.FS,
    Note.AB: Note.GS,
    Note.BB: Note.AS,
}


SCALE = [
    {Note.C},
    {Note.CS, Note.DB},
    {Note.D},
    {Note.DS, Note.EB},
    {Note.E},
    {Note.F},
    {Note.FS, Note.GB},
    {Note.G},
    {Note.GS, Note.AB},
    {Note.A},
    {Note.AS, Note.BB},
    {Note.B},
]


class Step(int, Enum):
    H = 1
    W = 2


class Seniority(str, Enum):
    MAJOR = "major"
    MINOR = "minor"
    DIMINISHED = "diminished"


class Mode(str, Enum):
    IONIAN = "ionian"
    DORIAN = "dorian"
    PHRYGIAN = "phrygian"
    LYDIAN = "lydian"
    MIXOLYDIAN = "mixolydian"
    AEOLIAN = "aeolian"
    LOCRIAN = "locrian"
    MAJOR = "major"
    MINOR = "minor"


class Note(str, Enum):
    C = "c"
    CS = "cs"
    DB = "db"
    D = "d"
    DS = "ds"
    EB = "eb"
    E = "e"
    F = "f"
    FS = "fs"
    GB = "gb"
    G = "g"
    GS = "gs"
    AB = "ab"
    A = "a"
    AS = "as"
    BB = "bb"
    B = "b"


@dataclass(frozen=True, kw_only=True)
class Key:
    mode: Mode
    steps: list[Step]
    numerals: list[str]
    seniority: Seniority

    def chords(self, note: Note) -> list[set[Chord]]:
        """
        Return a list of sets, where each set holds enharmonic equivalent names of
        chords appropriate for the mode of the given note. These are sorted by
        scale degrees, so the result can be indexed with 0-6 to get degrees 1-7.
        """
        # Translate bogus notes into real ones.
        note = {
            "es": Note.F,
            "fb": Note.E,
            "cb": Note.B,
            "bs": Note.C,
        }.get(note, note)

        for degree in range(len(SCALE)):
            if note in SCALE[degree]:
                break

        results = []
        for i, step in enumerate(self.steps):
            if degree >= len(SCALE):
                degree -= 12

            numeral = self.numerals[i]

            if numeral.isupper():
                if "d" in numeral:
                    result = {Chord(f"{n.value}_major_dim") for n in SCALE[degree]}
                else:
                    result = {Chord(f"{n.value}_major") for n in SCALE[degree]}
            else:
                if "d" in numeral:
                    result = {Chord(f"{n.value}_dim") for n in SCALE[degree]}
                else:
                    result = {Chord(f"{n.value}_minor") for n in SCALE[degree]}

            results.append(result)
            degree += step

        return results

    def notes(self, note: Note) -> list[set[Note]]:
        # Translate bogus notes into real ones.
        note = {
            "es": Note.F,
            "fb": Note.E,
            "cb": Note.B,
            "bs": Note.C,
        }.get(note, note)

        for degree in range(len(SCALE)):
            if note in SCALE[degree]:
                break

        results = []
        for i, step in enumerate(self.steps):
            if degree >= len(SCALE):
                degree -= 12

            results.append(SCALE[degree])

            degree += step

        return results


IONIAN = Key(
    mode=Mode.IONIAN,
    steps=[Step.W, Step.W, Step.H, Step.W, Step.W, Step.W, Step.H],
    numerals=["I", "ii", "iii", "IV", "V", "vi", "viid"],
    seniority=Seniority.MAJOR,
)

MAJOR = Key(
    mode=Mode.MAJOR,
    steps=[Step.W, Step.W, Step.H, Step.W, Step.W, Step.W, Step.H],
    numerals=["I", "ii", "iii", "IV", "V", "vi", "viid"],
    seniority=Seniority.MAJOR,
)

DORIAN = Key(
    mode=Mode.DORIAN,
    steps=[Step.W, Step.H, Step.W, Step.W, Step.W, Step.H, Step.W],
    numerals=["i", "ii", "III", "IV", "v", "vid", "VII"],
    seniority=Seniority.MINOR,
)

PHRYGIAN = Key(
    mode=Mode.PHRYGIAN,
    steps=[Step.H, Step.W, Step.W, Step.W, Step.H, Step.W, Step.W],
    numerals=["i", "II", "III", "iv", "vd", "VI", "vii"],
    seniority=Seniority.MINOR,
)

LYDIAN = Key(
    mode=Mode.LYDIAN,
    steps=[Step.W, Step.W, Step.W, Step.H, Step.W, Step.W, Step.H],
    numerals=["I", "II", "iii", "ivd", "V", "vi", "vii"],
    seniority=Seniority.MAJOR,
)

MIXOLYDIAN = Key(
    mode=Mode.MIXOLYDIAN,
    steps=[Step.W, Step.W, Step.H, Step.W, Step.W, Step.H, Step.W],
    numerals=["I", "ii", "iiid", "IV", "v", "vi", "VII"],
    seniority=Seniority.MAJOR,
)

AEOLIAN = Key(
    mode=Mode.AEOLIAN,
    steps=[Step.W, Step.H, Step.W, Step.W, Step.H, Step.W, Step.W],
    numerals=["i", "iid", "III", "iv", "v", "VI", "VII"],
    seniority=Seniority.MINOR,
)

MINOR = Key(
    mode=Mode.MINOR,
    steps=[Step.W, Step.H, Step.W, Step.W, Step.H, Step.W, Step.W],
    numerals=["i", "iid", "III", "iv", "v", "VI", "VII"],
    seniority=Seniority.MINOR,
)

LOCRIAN = Key(
    mode=Mode.LOCRIAN,
    steps=[Step.H, Step.W, Step.W, Step.H, Step.W, Step.W, Step.W],
    numerals=["id", "II", "iii", "iv", "V", "VI", "vii"],
    seniority=Seniority.DIMINISHED,
)
