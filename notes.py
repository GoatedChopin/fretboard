import random as r


NOTES = [
    ('A',), 
    ('A#', 'Bb'),
    ('B',),
    ('C',),
    ('C#', 'Db'),
    ('D',),
    ('D#', 'Eb'),
    ('E',),
    ('F'),
    ('F#', 'Gb'),
    ('G',),
    ('G#', 'Ab')
]

STANDARD_TUNING = [
    7, 2, 10, 5, 0, 7
]

DROP_D = [
    7, 2, 10, 5, 0, 5
]


def note_at_fret(string_number, fret_number, tuning=STANDARD_TUNING):
    global NOTES
    note = tuning[string_number-1]
    for _ in range(fret_number):
        note += 1
        if note == len(NOTES):
            note = 0
    return NOTES[note]


def random_note(lowest_fret=0, highest_fret=22, tuning=STANDARD_TUNING):
    string = r.randint(1,6)
    fret = r.randint(lowest_fret, highest_fret)
    return string, fret, note_at_fret(string, fret, tuning)


def all_places(note, lowest_fret=0, highest_fret=22, named=False, finds = [[], [], [], [], [], []], tuning=STANDARD_TUNING):
    fret = lowest_fret
    while fret <= highest_fret:
        for string in range(1, 7):
            if note_at_fret(string, fret, tuning) == note:
                if named:
                    finds[string-1].append((fret, note[0]))
                else:
                    finds[string-1].append(fret)
        fret += 1
    return finds


def quiz(lowest_fret=0, highest_fret=22, tuning=STANDARD_TUNING):
    while True:
        string, fret, note = random_note(lowest_fret, highest_fret, tuning)
        guess = input(f"The note on string {string} at fret {fret} is: ")
        if guess.strip().lower() in (n.lower() for n in note):
            print("Correct!")
        elif guess.lower() in ("quit", "exit", "stop"):
            print("Stopping...")
            break
        else:
            print(f"No, the note is {note}")


def print_fretboard(notes_to_highlight=[[]]*6, 
                    chars_per_fret=3, 
                    fret_char='|', 
                    string_char='-', 
                    match_char='X', 
                    lowest_fret=0, 
                    highest_fret=22,
                    named=False,
                    print_numbers=True):

    match_part = string_char*(chars_per_fret//2)
    if print_numbers:
        blank_part = " "*(chars_per_fret//2)
        for i in range(lowest_fret, highest_fret+1):
            num = str(i)
            right_part = blank_part[:-1] if len(num)>1 else blank_part
            print(blank_part + num + right_part, end='|')
        print()
    for string in range(6):
        for i in range(lowest_fret, highest_fret+1):
            if named:
                if i in {entry[0] for entry in notes_to_highlight[string]}:
                    for fret, note in notes_to_highlight[string]:
                        if i == fret:
                            right_part = match_part
                            if len(note) > 1:
                                right_part = match_part[:-1]
                            print((match_part + note + right_part), sep='', end=fret_char)
                            break
                else:
                    print((chars_per_fret*string_char), sep='', end=fret_char)
                
            else:
                if i in notes_to_highlight[string]:
                    print((match_part + match_char + match_part), sep='', end=fret_char)
                else:
                    print((chars_per_fret*string_char), sep='', end=fret_char)
        print()





if __name__ == "__main__":
    from sys import argv

    print(argv)
    if not argv[1:]:
        quiz()
    elif argv[1].lower().strip() in ('test', 'quiz'):
        quiz()
    else:
        try:
            tones = eval(argv[1])
            highlights = [[], [], [], [], [], []]
            for tone in tones:
                highlights = all_places(NOTES[tone], finds=highlights, named=True)
            print_fretboard(notes_to_highlight=highlights, named=True)
        except:
            from pprint import pprint
            print("Try passing in 'quiz' or a tuple of the following for fretboard diagrams:")
            pprint({i:NOTES[i] for i in range(len(NOTES))})

    # highlights = [[], [], [], [], [], []]

    # C_MAJOR = (3, 7, 10)
    # C_MAJOR_7 = C_MAJOR + (C_MAJOR[0]-1,)
    # C_MAJOR_6 = C_MAJOR + (C_MAJOR[0]-3,)
    # A_MINOR = (0, 3, 7)
    # A_MINOR_7 = A_MINOR + (A_MINOR[0]-2+len(NOTES),)
    # A_MINOR_6 = A_MINOR + ((A_MINOR[0]-4)+len(NOTES),)


    # for tone in A_MINOR_7:
    #     highlights = all_places(NOTES[tone], finds=highlights, named=True)

    # # all_places(NOTES[0], named=True)

    # print_fretboard(notes_to_highlight=highlights, named=True)
