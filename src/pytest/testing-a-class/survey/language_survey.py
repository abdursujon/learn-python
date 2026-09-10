from survey import AnonymousSurvey

class LanguageSurvey: 
    questions = ["What is your first language?", "Do you speak any other language (Y/N)?", 
    "If you were to learn a new langauge which one would you learn first, and why?"]

    def language_survey(self):
        response_list = []
        print("Type 'q' to quit anytime")

        for q in self.questions:
            print(q)
            while True: 
                response = input("Response: ")
                if response == 'q':
                    return
                else:
                    response_list.append(response)
                    break
        print(response_list)
        survey = AnonymousSurvey()
        survey.responses = response_list
        survey.show_result()

lang_survey = LanguageSurvey()
lang_survey.language_survey()