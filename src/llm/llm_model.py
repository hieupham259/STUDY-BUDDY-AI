from langchain_google_genai import ChatGoogleGenerativeAI
from src.config.settings import settings


def get_gemini_llm():
    return ChatGoogleGenerativeAI(
        api_key=settings.GEMINI_API_KEY,
        model="gemini-2.5-flash",
        temperature=settings.TEMPERATURE
    )

def generate_mcq(topic:str , difficulty:str) -> str:

    from langchain.prompts import PromptTemplate

    mcq_prompt_template = PromptTemplate(
        template=(
            "Generate a {difficulty} multiple-choice question about {topic}.\n\n"
            "Return ONLY a JSON object with these exact fields:\n"
            "- 'question': A clear, specific question\n"
            "- 'options': An array of exactly 4 possible answers\n"
            "- 'correct_answer': One of the options that is the correct answer\n\n"
            "Example format:\n"
            '{{\n'
            '    "question": "What is the capital of France?",\n'
            '    "options": ["London", "Berlin", "Paris", "Madrid"],\n'
            '    "correct_answer": "Paris"\n'
            '}}\n\n'
            "Your response:"
        ),
        input_variables=["topic", "difficulty"]
    )

    chain = mcq_prompt_template | get_gemini_llm()
    response = chain.invoke({
        "topic": topic,
        "difficulty": difficulty
    })
    return response.content


if __name__ == "__main__":
    topic = "Paris"
    difficulty = "easy"
    itinerary = generate_mcq(topic, difficulty)
    print(itinerary)