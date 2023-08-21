## main.py
import os
from gpt3_analysis import GPT3Analysis
from anki_deck_generator import AnkiDeckGenerator
from gui import GUI

class Main:
    def __init__(self, file_path: str = "", output_path: str = ""):
        self.file_path = file_path
        self.output_path = output_path
        self.gpt3_analysis = GPT3Analysis(api_key="your_openai_api_key")
        self.anki_deck_generator = AnkiDeckGenerator(deck_name="Code Analysis")
        self.gui = GUI(title="Code Analysis Tool", main=self)

    def run(self):
        try:
            with open(self.file_path, 'r') as file:
                code = file.read()

            analysis = self.gpt3_analysis.analyze_code(code)
            organization = self.gpt3_analysis.organize_code(code)

            self.anki_deck_generator.add_card(front=code, back=f"Analysis: {analysis}\nOrganization: {organization}")
            deck_file = self.anki_deck_generator.generate_deck()

            os.rename(deck_file, self.output_path)
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    Main().gui.run()
