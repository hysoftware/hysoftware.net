'''
Noum generator
'''


def generate_first_person(developers):
    '''
    Generates First Person Noum
    '''
    result = {
        "i": "I",
        "I": "I",
        "iam": "I am",
        "Iam": "I am",
        "Ami": "Am I",
        "ami": "am I",
        "my": "my",
        "My": "My",
        "me": "me"
    }
    if len(developers) > 2:
        result = {
            "i": "we",
            "I": "We",
            "iam": "we are",
            "Iam": "We are",
            "Ami": "Are we",
            "ami": "are we",
            "my": "our",
            "My": "Our",
            "me": "us"
        }
    return result
