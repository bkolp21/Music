from music21 import stream, note, chord, environment, lyrics

# Create a music21 environment to configure settings
environment.set('musicxmlPath', '/usr/bin/musescore')  # Change the path to your MuseScore executable
environment.set('midiPath', '/usr/bin/timidity')  # Change the path to your Timidity executable

# Define the 12-bar blues chords and lyrics
blues_data = [
    ("E7", "I", ""),
    ("A7", "IV", ""),
    ("E7", "I", ""),
    ("E7", "I", ""),
    ("A7", "IV", ""),
    ("A7", "IV", ""),
    ("E7", "I", ""),
    ("E7", "I", ""),
    ("B7", "V", ""),
    ("A7", "IV", ""),
    ("E7", "I", ""),
    ("B7", "V", "")
]

# Create a music21 stream for the blues
blues_stream = stream.Stream()
lyric_stream = lyrics.Lyric()

for chord_symbol, lyric1, lyric2 in blues_data:
    if chord_symbol and lyric1:
        blues_stream.append(chord.Chord(chord_symbol.split()))
        lyric_stream.addLyric(lyric1)
    if lyric2:
        lyric_stream.addLyric(lyric2)

# Define the melody for the blues
melody_data = [
    ("E5", 4),
    ("G5", 4),
    ("A5", 4),
    ("G5", 4),
    ("B5", 4),
    ("G5", 4),
    ("E5", 4),
    ("G5", 4),
    ("A5", 4),
    ("G5", 4),
    ("A5", 2),
    ("G5", 2),
]

for note_symbol, duration in melody_data:
    note_obj = note.Note(note_symbol)
    note_obj.duration.quarterLength = duration
    blues_stream.append(note_obj)

blues_stream.insert(0, lyric_stream)

# Show the musical score with chords, lyrics, and melody
blues_stream.show()

# Convert and save as MusicXML
blues_stream.write('musicxml', 'best_dog_blues.xml')

# Convert and save as MIDI
blues_stream.write('midi', 'best_dog_blues.mid')
