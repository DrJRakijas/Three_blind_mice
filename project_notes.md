3 things:

1) Define structure of music files
2) Define music objects
3) Define the player

1) The music files
set[Measure]
- letter that note corresponds to
- notes in order that they should be
- more complicated stuff??
    - notes objects
    - duration of note


2) Music objects
    - Note (contained by Measure, units of Measure)
        -attributes:
            - tone
            - duration/length
            - type? quarter, dotted half, sixteenth etc
        - subclass : Rest
            - tone attribute is silence but others are the same
    - Measure (contains Notes, defined by TimeSignature)
        - attributes
            - nbeats (determined by time signature)
            - notes : set[Notes] 
    - TimeSignature/Meter? (master regulator)
        - attributes
            - base_note
            - bpmeasure
            - speed