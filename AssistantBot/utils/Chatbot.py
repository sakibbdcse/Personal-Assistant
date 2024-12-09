from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
class Chatbot:
    def __init__(self, model_name="microsoft/DialoGPT-small"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)
        self.chat_history_ids = None
        self.training_data = []

    def generate_response(self, user_input):
        new_user_input_ids = self.tokenizer.encode(user_input + self.tokenizer.eos_token, return_tensors="pt")
        bot_input_ids = torch.cat([self.chat_history_ids, new_user_input_ids], dim=-1) if self.chat_history_ids is not None else new_user_input_ids
        self.chat_history_ids = self.model.generate(bot_input_ids, max_length=1000, pad_token_id=self.tokenizer.eos_token_id, temperature=0.7, top_k=50, top_p=0.9)
        response = self.tokenizer.decode(self.chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
        self.training_data.append({"input": user_input, "response": response})
        self.auto_train()
        return response

    def auto_train(self):
        if len(self.training_data) > 10:
            print("Training model with new data...")
            inputs = self.tokenizer([data["input"] for data in self.training_data], return_tensors="pt", padding=True, truncation=True)
            labels = self.tokenizer([data["response"] for data in self.training_data], return_tensors="pt", padding=True, truncation=True)["input_ids"]
            self.model.train()
            with torch.no_grad():
                self.model(**inputs, labels=labels)
            self.training_data = []
            print("Model fine-tuned with new conversations.")