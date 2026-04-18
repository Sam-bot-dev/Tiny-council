from llm.huggingface import HuggingFaceLLM

if __name__ == "__main__":
    llm = HuggingFaceLLM()
    response = llm.generate("Explain secure login system")
    print("\nFINAL OUTPUT:\n", response)