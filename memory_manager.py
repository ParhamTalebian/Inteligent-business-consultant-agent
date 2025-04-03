import json
import os

class MemoryManager:
    def __init__(self, memory_file="chat_memory.json", max_history=5):
        self.memory_file = memory_file
        self.max_history = max_history
        self.history = self.load_memory()
        self.memory = {} 
    def load_memory(self):
        if os.path.exists(self.memory_file):
            with open(self.memory_file, "r", encoding="utf-8") as file:
                return json.load(file)
        return []
    
    def save_memory(self):
        with open(self.memory_file, "w", encoding="utf-8") as file:
            json.dump(self.history, file, ensure_ascii=False, indent=4)
    
    def add_message(self, role, message):
        self.history.append({"role": role, "message": message})
        if len(self.history) > self.max_history:
            self.history.pop(0)  
        self.save_memory()
    
    def get_context(self):
        return self.history[-self.max_history:]
    
    def clear_memory(self):
        self.history = []
        self.save_memory()


