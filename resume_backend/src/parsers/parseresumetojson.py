import json
import os
import os.path
import pathlib

from ..utils.extractor import DataExtractor
from ..utils.keyterms_extractor import KeytermExtractor
from ..utils.text_cleaner import CountFrequency, TextCleaner, generate_unique_id

# need to check the directory
SAVE_DIRECTORY = "../../Data/Processed/Resumes"


class ParseResume:

    def __init__(self, resume: str):
        self.resume_data = resume
        self.clean_data = TextCleaner.clean_text(self.resume_data)
        # here we are passing cleaned data as input and passing to extract entities -- location and organisation
        self.entities = DataExtractor(self.clean_data).extract_entities() 
        # here we are getting  the names of the resume
        self.name = DataExtractor(self.clean_data[:30]).extract_names()
        # here we are providing some experience sections to check the text and getting experience
        self.experience = DataExtractor(self.clean_data).extract_experience()
        # here we are not passing cleaned data , we are passing resume data and getting emails --regex
        self.emails = DataExtractor(self.resume_data).extract_emails()
        # same as emails and getting phone numbers using regex pattern
        self.phones = DataExtractor(self.resume_data).extract_phone_numbers()
        # by using regex from cleaned data we are getting position and year
        self.years = DataExtractor(self.clean_data).extract_position_year()
        # getting nouns and pronouns
        self.key_words = DataExtractor(self.clean_data).extract_particular_words()
        # how much each noun and pronoun frequency-- pos
        self.pos_frequencies = CountFrequency(self.clean_data).count_frequency()
        self.keyterms = KeytermExtractor(self.clean_data).get_keyterms_based_on_sgrank()
        self.bi_grams = KeytermExtractor(self.clean_data).bi_gramchunker()
        self.tri_grams = KeytermExtractor(self.clean_data).tri_gramchunker()

    def get_JSON(self) -> dict:
        """
        Returns a dictionary of resume data.
        """
        resume_dictionary = {
            "unique_id": generate_unique_id(),
            "resume_data": self.resume_data,
            "clean_data": self.clean_data,
            "entities": self.entities,
            "extracted_keywords": self.key_words,
            "keyterms": self.keyterms,
            "name": self.name,
            "experience": self.experience,
            "emails": self.emails,
            "phones": self.phones,
            "years": self.years,
            "bi_grams": str(self.bi_grams),
            "tri_grams": str(self.tri_grams),
            "pos_frequencies": self.pos_frequencies,
        }

        return resume_dictionary
