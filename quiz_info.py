""" This is where all of our data for the quizzes is, which includes title, description, and questions.
Every item in the questions list has a question, which contain several answers, but only one correct answer.
The correct answer is denoted by the key value pair of True, while the rest are False. """

quiz_info = [
    {
        
        "quiz_title": "NBA Quiz",
        "quiz_description": "Quiz on NBA players and stats",
            "questions": [
            {
                "id" : 100,
                "question": "Who is the All Time leader in assists?",
                "answers": {
                    "John Stockton": True,
                    "Chris Paul": False,
                    "Steve Nash": False
                }
            },
            {
                "id" : 101,
                "question": "Who is the All Time leader in Points?",
                "answers": {
                    "LeBron James": True,
                    "Kobe Bryant": False,
                    "Michael Jordan": False
                }
            }
        ]
    },
    
    {
        
        "quiz_title": "Car Quiz",
        "quiz_description": "Quiz on Popular automobiles and specs",
                "questions": [
            {
                "id" : 200,
                "question": "Which vehicle company originates from Germany?",
                "answers": {
                    "Porsche": True,
                    "Ferrari": False,
                    "Aston Martin": False
                }
            }
        ]
    },
    
    {
        
        "quiz_title": "History Quiz",
        "quiz_description": "Quiz on historical events and notable people",
        "questions": [
            {
                "id" : 300,
                "question": "Who was the first U.S. President?",
                "answers": {
                    "George Washington": True,
                    "Andrew Jackson": False,
                    "Winston Churchill": False
                }
            }, 
            {
                "id" : 301,
                "question" : "When did the United States become a independent country?",
                "answers" : {
                    "2000" : False,
                    "1492" : False,
                    "1609" : False,
                    "1776" : True
                }
            }
        ]
    }
]