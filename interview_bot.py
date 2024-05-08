import re
import spacy


class InterviewBot:
    def __init__(self):
        self.user_data = {}

    def ask_name(self):
        name = input("What is your full name? ")
        # Use machine learning to extract only the name
        extract_name = self.extract_name(name)
        # Validate name (e.g., check for alphabetic characters)
        if not re.match("^[a-zA-Z ]+$", name):
            print("Invalid name. Please enter alphabetic characters only.")
            return self.ask_name()
        else:

            self.user_data['name'] = extract_name

    def ask_age(self):
        age = input("What is your age? ")
        extract_age = self.extract_age(age)
        # Validate age (e.g., check for numeric characters)
        if not extract_age.isdigit():
            print("Invalid age. Please enter numeric characters only.")
            return self.ask_age()
        else:
            self.user_data['age'] = int(extract_age)

    def ask_gender(self):
        gender = input("What is your gender? ")
        # Validate gender (e.g., check for predefined options)
        if gender.lower() not in ['male', 'female', 'other']:
            print("Invalid gender. Please enter 'male', 'female', or 'other'.")
            return self.ask_gender()
        else:
            self.user_data['gender'] = gender

    def conduct_interview(self):
        print("Welcome to the interview!")
        self.ask_name()
        self.ask_age()
        # self.ask_gender()
        print("Thank you for completing the interview. Here is your information:")
        print(self.user_data)

    def extract_name(self, text):
        # Use spaCy for named entity recognition (NER) to extract names
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(text)
        for entity in doc.ents:
            if entity.label_ == "PERSON":
                return entity.text
        # If no name is detected, return the original text
        return text

    def extract_age(self, text):
        # Use spaCy for named entity recognition (NER) to extract names
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(text)
        for entity in doc.ents:
            if entity.label_ == "AGE":
                return entity.text
        # If no name is detected, return the original text
        return text


if __name__ == "__main__":
    bot = InterviewBot()
    bot.conduct_interview()
