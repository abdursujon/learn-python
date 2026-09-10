class AnonymousSurvey:

    def __init__(self, question=""):
        self.question = question
        self.responses = []
    
    def show_question(self):
        print(self.question)
    
    def store_response(self, new_response):
        self.responses.append(new_response)
    
    def show_result(self):
        print("Survey result: ")
        labels = ["First language: ", "Speak A Second language?: ", "Language wish to learn: "]
        for i, response in enumerate(self.responses):
            print(f"{labels[i]}{response}")
