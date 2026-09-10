import pytest 
from survey import AnonymousSurvey

# A survey function that will be available to all functions 
@pytest.fixture
def language_survey():
    question = "What is your first language?"
    language_survey = AnonymousSurvey(question)
    return language_survey

def test_store_response(language_survey):
    language_survey.store_response('English')
    assert 'English' in language_survey.responses


def test_store_three_response(language_survey):
    responses = ["English", "Bangladeshi", "Italian"]
    
    for r in responses: 
        language_survey.store_response(r)
    
    for r in responses: 
        assert r in language_survey.responses

def test_store_response_can_handle_large_number_of_response(language_survey):
    responses = []
    i = 0
    while(i <= 1000):
        responses.append("English")
        i += 1

    for r in responses: 
        language_survey.store_response(r)
    
    for r in responses: 
        assert r in language_survey.responses
