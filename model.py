from transformers import pipeline
MODEL = "jy46604790/Fake-News-Bert-Detect"
clf = pipeline("text-classification", model=MODEL, tokenizer=MODEL)

#LABEL_0: Fake news

#LABEL_1: Real news

def news_classifier(text):
    result = clf(text)
    return result
