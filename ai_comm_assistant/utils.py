import re

def simple_sentiment(text: str) -> str:
    text = text.lower()
    if any(w in text for w in ["urgent", "immediately", "critical", "blocked", "down"]):
        return "Negative"
    if any(w in text for w in ["thank", "great", "appreciate"]):
        return "Positive"
    return "Neutral"

def detect_priority(text: str) -> str:
    text = text.lower()
    if any(w in text for w in ["urgent", "immediately", "critical", "blocked", "down", "cannot access"]):
        return "Urgent"
    return "Not urgent"

def extract_contact(text: str):
    phones = re.findall(r"\+?\d[\d\- ]{7,}\d", text)
    emails = re.findall(r"[\w._%+-]+@[\w.-]+", text)
    return {"phones": phones, "emails": emails}
