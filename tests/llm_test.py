from llm.huggingface import HuggingFaceLLM

llm = HuggingFaceLLM("google/flan-t5-base")

print(llm.generate("What is a secure login system?"))