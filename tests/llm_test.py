from llm.huggingface import HuggingFaceLLM

llm = HuggingFaceLLM("mistralai/Mistral-7B-Instruct-v0.2")

print(llm.generate("What is a secure login system?"))