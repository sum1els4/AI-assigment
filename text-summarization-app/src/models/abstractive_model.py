from transformers import T5ForConditionalGeneration, T5Tokenizer

class AbstractiveSummarizer:
    def __init__(self, model_name='t5-small'):
        self.tokenizer = T5Tokenizer.from_pretrained(model_name)
        self.model = T5ForConditionalGeneration.from_pretrained(model_name)

    def summarize(self, text, max_length=150, min_length=40, do_sample=False):
        inputs = self.tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=512, truncation=True)
        summary_ids = self.model.generate(inputs, max_length=max_length, min_length=min_length, do_sample=do_sample)
        summary = self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        return summary

    def summarize_file(self, file_path):
        with open(file_path, 'r') as file:
            text = file.read()
        return self.summarize(text)