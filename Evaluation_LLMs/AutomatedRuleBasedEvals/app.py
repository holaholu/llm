from langchain_core.prompts           import ChatPromptTemplate
from langchain_openai                 import ChatOpenAI
from langchain_core.output_parsers    import StrOutputParser

delimiter = "####"

quiz_bank = """1. Subject: Leonardo DaVinci
   Categories: Art, Science
   Facts:
    - Painted the Mona Lisa
    - Studied zoology, anatomy, geology, optics
    - Designed a flying machine

2. Subject: Paris
   Categories: Art, Geography
   Facts:
    - Location of the Louvre, the museum where the Mona Lisa is displayed
    - Capital of France
    - Most populous city in France
    - Where Radium and Polonium were discovered by scientists Marie and Pierre Curie

3. Subject: Telescopes
   Category: Science
   Facts:
    - Device to observe different objects
    - The first refracting telescopes were invented in the Netherlands in the 17th Century
    - The James Webb space telescope is the largest telescope in space. It uses a gold-berillyum mirror

4. Subject: Starry Night
   Category: Art
   Facts:
    - Painted by Vincent van Gogh in 1889
    - Captures the east-facing view of van Gogh's room in Saint-Rémy-de-Provence

5. Subject: Physics
   Category: Science
   Facts:
    - The sun doesn't change color during sunset.
    - Water slows the speed of light
    - The Eiffel Tower in Paris is taller in the summer than the winter due to expansion of the metal.
"""

system_message = f"""
Follow these steps to generate a customized quiz for the user.
The question will be delimited with four hashtags i.e {delimiter}

The user will provide a category that they want to create a quiz for. Any questions included in the quiz
should only refer to the category.

Step 1:#### First decide whether the user is asking about a subject that is in the following quiz bank:
- Geography: Paris, Rome (historical), Mediterranean climate
- Science: Photosynthesis, Newton's Laws, Quantum Mechanics  
- Art: Mona Lisa, Starry Night, Impressionism

Here is the quiz bank

{quiz_bank}

Step 2:#### If the subject is NOT explicitly in the quiz bank, respond ONLY with:
"I'm sorry I do not have information about that"
DO NOT generate questions about related topics.

Step 3:#### If the subject IS in the quiz bank, identify the category and generate 3 questions.

Use the following format for the quiz:
Question 1:{delimiter} <question 1>

Question 2:{delimiter} <question 2>

Question 3:{delimiter} <question 3>

Additional rules:

- Only use explicit matches for the category, if the category is not an exact match to categories in the quiz bank, answer that you do not have information.
- If the user asks a question about a subject you do not have information about in the quiz bank, answer "I'm sorry I do not have information about that".
"""

"""
  Helper functions for writing the test cases
"""

def assistant_chain(
    system_message=system_message,
    human_template="{question}",
    llm=ChatOpenAI(model="gpt-3.5-turbo", temperature=0),
    output_parser=StrOutputParser()):

  chat_prompt = ChatPromptTemplate.from_messages([
      ("system", system_message),
      ("human", human_template),
  ])
  return chat_prompt | llm | output_parser
