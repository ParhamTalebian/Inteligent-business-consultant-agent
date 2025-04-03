from together import Together
import os
from retrieval_engine import RetrievalEngine
# from memory_manager import MemoryManager  

class LLMInterface:
    def __init__(self, api_key=None, model_name="meta-llama/Llama-3.3-70B-Instruct-Turbo"):
        self.api_key = api_key or os.getenv("cf695d0e05061568bad485126184ca88a09340cd8540ec31deee936b83914c1a")
        if not self.api_key:
            raise ValueError("API Key برای Together تنظیم نشده است.")
        
        self.model = model_name
        self.client = Together(api_key=self.api_key)
        self.retrieval_engine = RetrievalEngine()
        # self.memory = MemoryManager()  

    def ask(self, prompt, user_id="default"):
        # history = self.memory.get_context(user_id)  
        relevant_data = self.retrieval_engine.search(prompt)

        combined_prompt = f""" 
        اطلاعات مرتبط: {relevant_data}  
        پرسش جدید: {prompt}  
        """

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": combined_prompt}],
        ).choices[0].message.content.strip()

        # self.memory.add_memory(user_id, f"User: {prompt}\nAI: {response}")  
        return response
