import tkinter as tk
from tkinter import scrolledtext, messagebox
from llm_interface import LLMInterface
from retrieval_engine import RetrievalEngine
from business_plan_generator import BusinessPlanGenerator
from document_reader import DocumentReader
# from memory_manager import MemoryManager  # حذف مدیریت حافظه
import os 
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


class BusinessAdvisorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("مشاور هوشمند کسب‌وکار")
        self.root.geometry("1000x1000")

        self.api_key = "cf695d0e05061568bad485126184ca88a09340cd8540ec31deee936b83914c1a"
        self.llm = LLMInterface(api_key=self.api_key)
        self.retrieval_engine = RetrievalEngine()
        self.business_plan_generator = BusinessPlanGenerator()
        self.doc_reader = DocumentReader()
        # self.memory_manager = MemoryManager()  # حذف مدیریت حافظه

        tk.Label(root, text="تنظیمات:", font=("Arial", 12)).pack(pady=5)

        self.api_key_entry = tk.Entry(root, width=60)
        self.api_key_entry.insert(0, self.api_key)
        self.api_key_entry.pack(pady=5)

        self.save_settings_button = tk.Button(root, text="ذخیره تنظیمات", command=self.save_settings, font=("Arial", 12))
        self.save_settings_button.pack(pady=5)

        tk.Label(root, text="سوال خود را وارد کنید:", font=("Arial", 12)).pack(pady=5)
        self.question_entry = tk.Entry(root, width=60)
        self.question_entry.pack(pady=5)

        self.ask_button = tk.Button(root, text="📩 دریافت پاسخ", command=self.ask_llm, font=("Arial", 12))
        self.ask_button.pack(pady=10)

        tk.Label(root, text="📌 پاسخ:", font=("Arial", 12)).pack(pady=5)
        self.response_text = scrolledtext.ScrolledText(root, width=70, height=6, wrap=tk.WORD)
        self.response_text.pack(pady=5)

        tk.Label(root, text="📂 اطلاعات مرتبط:", font=("Arial", 12)).pack(pady=5)
        self.retrieval_text = scrolledtext.ScrolledText(root, width=70, height=4, wrap=tk.WORD)
        self.retrieval_text.pack(pady=5)

        tk.Label(root, text="📋 طرح کسب‌وکار:", font=("Arial", 12)).pack(pady=5)
        self.business_plan_text = scrolledtext.ScrolledText(root, width=70, height=6, wrap=tk.WORD)
        self.business_plan_text.pack(pady=5)

        tk.Label(root, text="بارگذاری فایل (PDF/Word):", font=("Arial", 12)).pack(pady=5)
        self.file_entry = tk.Entry(root, width=60)
        self.file_entry.pack(pady=5)
        self.load_file_button = tk.Button(root, text="بارگذاری فایل", command=self.load_file, font=("Arial", 12))
        self.load_file_button.pack(pady=5)

        self.download_button = tk.Button(root, text="💾 دانلود خروجی", command=self.download_output, font=("Arial", 12))
        self.download_button.pack(pady=5)

    def save_settings(self):
        new_api_key = self.api_key_entry.get()
        if new_api_key:
            self.api_key = new_api_key
            messagebox.showinfo("تنظیمات", "تنظیمات با موفقیت ذخیره شدند.")
        else:
            messagebox.showwarning("⚠️ هشدار", "لطفاً یک API Key وارد کنید.")

    def ask_llm(self):
        question = self.question_entry.get()
        if not question:
            messagebox.showwarning("⚠️ هشدار", "لطفاً یک سوال وارد کنید.")
            return

        response = self.llm.ask(question)
        self.response_text.delete("1.0", tk.END)
        self.response_text.insert(tk.END, response)

        relevant_data = self.retrieval_engine.search(question)
        self.retrieval_text.delete("1.0", tk.END)
        self.retrieval_text.insert(tk.END, relevant_data)

        # self.memory_manager.save_conversation(question, response)

        business_plan = self.business_plan_generator.generate_business_plan(response)
        self.business_plan_text.delete("1.0", tk.END)
        self.business_plan_text.insert(tk.END, business_plan)

    def load_file(self):
        file_path = self.file_entry.get()
        if not file_path:
            messagebox.showwarning("⚠️ هشدار", "لطفاً آدرس فایل را وارد کنید.")
            return

        if file_path.endswith(".pdf"):
            content = self.doc_reader.read_pdf(file_path)
        elif file_path.endswith(".docx"):
            content = self.doc_reader.read_docx(file_path)
        else:
            content = self.doc_reader.read_text_file(file_path)

        self.response_text.delete("1.0", tk.END)
        self.response_text.insert(tk.END, content)

    def download_output(self):
        response = self.response_text.get("1.0", tk.END)
        business_plan = self.business_plan_text.get("1.0", tk.END)

        output_content = f"💬 پاسخ:\n{response}\n\n📋 طرح کسب‌وکار:\n{business_plan}"

        with open("business_output.txt", "w", encoding="utf-8") as f:
            f.write(output_content)

        messagebox.showinfo("دانلود", "خروجی‌ها با موفقیت ذخیره شدند. می‌توانید آن را دانلود کنید.")

    def download_pdf(self):
        response = self.response_text.get("1.0", tk.END)
        business_plan = self.business_plan_text.get("1.0", tk.END)

        filename = "business_output.pdf"
        c = canvas.Canvas(filename, pagesize=letter)
        c.drawString(100, 750, f"💬 پاسخ:\n{response}")
        c.drawString(100, 700, f"📋 طرح کسب‌وکار:\n{business_plan}")
        c.save()

        messagebox.showinfo("دانلود PDF", "خروجی‌ها با موفقیت ذخیره شدند. می‌توانید PDF را دانلود کنید.")

def run_tkinter():
    root = tk.Tk()
    app = BusinessAdvisorApp(root)
    root.mainloop()
