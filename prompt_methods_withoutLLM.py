class SimulatedLLM:
    def __init__(self, context):
        self.context = context

    def standard_prompting(self, question):
        if "Eiffel Tower" in question:
            return "The Eiffel Tower is located in Paris, France."
        elif "Great Pyramid of Giza" in question:
            return "The Great Pyramid of Giza is located in Egypt."
        else:
            return "I don't know the answer."

    def chain_of_thought_prompting(self, question):
        thoughts = []
        if "Eiffel Tower" in question:
            thoughts.append("The question is about the location of the Eiffel Tower.")
            thoughts.append("The context mentions that the Eiffel Tower is in Paris, France.")
            return "Step-by-step reasoning: " + "; ".join(thoughts) + "\nAnswer: The Eiffel Tower is located in Paris, France."
        elif "Great Pyramid of Giza" in question:
            thoughts.append("The question is about the location of the Great Pyramid of Giza.")
            thoughts.append("The context mentions that the Great Pyramid of Giza is in Egypt.")
            return "Step-by-step reasoning: " + "; ".join(thoughts) + "\nAnswer: The Great Pyramid of Giza is located in Egypt."
        else:
            return "I don't know the answer."

    def act_only_prompting(self, question):
        if "Eiffel Tower" in question:
            return "Action: Look up 'Eiffel Tower' in the context. Answer: The Eiffel Tower is located in Paris, France."
        elif "Great Pyramid of Giza" in question:
            return "Action: Look up 'Great Pyramid of Giza' in the context. Answer: The Great Pyramid of Giza is located in Egypt."
        else:
            return "I don't know the answer."

    def react_prompting(self, question):
        thoughts_and_actions = []
        if "Eiffel Tower" in question:
            thoughts_and_actions.append("Thought: I need to find information about the Eiffel Tower.")
            thoughts_and_actions.append("Action: Search the context for 'Eiffel Tower'.")
            thoughts_and_actions.append("Observation: The Eiffel Tower is located in Paris, France.")
            thoughts_and_actions.append("Thought: The location of the Eiffel Tower is Paris, France.")
            return "Interleaved reasoning and acting: " + "; ".join(thoughts_and_actions) + "\nAnswer: The Eiffel Tower is located in Paris, France."
        elif "Great Pyramid of Giza" in question:
            thoughts_and_actions.append("Thought: I need to find information about the Great Pyramid of Giza.")
            thoughts_and_actions.append("Action: Search the context for 'Great Pyramid of Giza'.")
            thoughts_and_actions.append("Observation: The Great Pyramid of Giza is located in Egypt.")
            thoughts_and_actions.append("Thought: The location of the Great Pyramid of Giza is Egypt.")
            return "Interleaved reasoning and acting: " + "; ".join(thoughts_and_actions) + "\nAnswer: The Great Pyramid of Giza is located in Egypt."
        else:
            return "I don't know the answer."

context = """
The Eiffel Tower is located in Paris, France. It was built for the 1889 Exposition Universelle.
The Great Pyramid of Giza is located in Egypt. It was built as a tomb for Pharaoh Khufu.
"""

question = "Where is the Eiffel Tower located?"

llm = SimulatedLLM(context)

print("Standard Prompting:")
print(llm.standard_prompting(question))

print("\nChain-of-Thought Prompting:")
print(llm.chain_of_thought_prompting(question))

print("\nAct-Only Prompting:")
print(llm.act_only_prompting(question))

print("\nReAct Prompting:")
print(llm.react_prompting(question))
