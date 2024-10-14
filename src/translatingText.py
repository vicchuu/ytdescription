# src/translate.py
from transformers import MarianMTModel, MarianTokenizer


def load_translation_model(src_lang='en', tgt_lang='fr'):
    model_name = f'Helsinki-NLP/opus-mt-{src_lang}-{tgt_lang}'
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)
    return tokenizer, model


def translate_text(text, tokenizer, model):
    batch = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    generated_ids = model.generate(**batch)
    translated_text = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
    return translated_text
