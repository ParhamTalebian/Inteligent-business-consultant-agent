# app/test_llm_interface.py

from llm_interface import LLMInterface


def test_llm_interface():
    api_key = "cf695d0e05061568bad485126184ca88a09340cd8540ec31deee936b83914c1a"
    llm = LLMInterface(api_key=api_key)
    
    question = "What are some innovative business ideas?"
    response = llm.ask(question)
    
    print(f"Response: {response}")

if __name__ == "__main__":
    test_llm_interface()
