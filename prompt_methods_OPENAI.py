import openai

openai.api_key = 'your_openai_api_key'

context = """
The Eiffel Tower is located in Paris, France. It was built for the 1889 Exposition Universelle.
The Great Pyramid of Giza is located in Egypt. It was built as a tomb for Pharaoh Khufu.
"""

question = "Where is the Eiffel Tower located?"

def standard_prompting(context, question):
    prompt = f"Context: {context}\nQuestion: {question}\nAnswer:"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=60,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].text.strip()

def chain_of_thought_prompting(context, question):
    prompt = f"Context: {context}\nQuestion: {question}\nLet's think step by step."
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].text.strip()

def act_only_prompting(context, question):
    prompt = f"Context: {context}\nQuestion: {question}\nAction:"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=60,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].text.strip()

def react_prompting(context, question):
    prompt = f"Context: {context}\nQuestion: {question}\nThought 1: I need to identify the relevant information from the context."
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=200,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].text.strip()

print("Standard Prompting:")
print(standard_prompting(context, question))

print("\nChain-of-Thought Prompting:")
print(chain_of_thought_prompting(context, question))

print("\nAct-Only Prompting:")
print(act_only_prompting(context, question))

print("\nReAct Prompting:")
print(react_prompting(context, question))
