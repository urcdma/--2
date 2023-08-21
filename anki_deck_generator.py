import genanki

class AnkiDeckGenerator:
    def __init__(self, deck_name: str):
        self.deck_name = deck_name
        self.deck = genanki.Deck(2059400110, self.deck_name)
        self.model = genanki.Model(
            1607392319,
            'Simple Model',
            fields=[
                {'name': 'Question'},
                {'name': 'Answer'},
            ],
            templates=[
                {
                    'name': 'Card 1',
                    'qfmt': '{{Question}}',
                    'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
                },
            ])

    def add_card(self, front: str, back: str):
        """
        Add a card to the Anki deck with the given front and back.
        """
        note = genanki.Note(
            model=self.model,
            fields=[front, back])
        self.deck.add_note(note)

    def generate_deck(self) -> str:
        """
        Generate the Anki deck and return the file name.
        """
        genanki.Package(self.deck).write_to_file(f'{self.deck_name}.apkg')
        return f'{self.deck_name}.apkg'
