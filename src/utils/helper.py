import os
import streamlit as st
import pandas as pd
from src.generator.question_generator import QuestionGenerator


def rerun():
    st.session_state['rerun_trigger'] = not st.session_state.get('rerun_trigger',False)

class QuizManager:
    def __init__(self):
        self.questions = []
        self.user_answers = []
        self.results = []

    def generate_questions(self,
                          generator: QuestionGenerator,
                          topic: str,
                          question_type: str,
                          difficulty: str,
                          num_questions: int):
        self.questions = []
        self.user_answers = []
        self.results = []

        try:
            for _ in range(num_questions):
                if question_type == 'Multiple Choice':
                    question = generator.generate_mcq(topic, difficulty.lower())
                    
                    self.questions.append({
                        'type' : 'MCQ',
                        'question' : question.question,
                        'options' : question.options,
                        'correct_answer': question.correct_answer
                    })
        except Exception as e:
            st.error(f"Error generating question {e}")
            return False
        return True