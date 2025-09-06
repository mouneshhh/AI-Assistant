import pandas as pd
import os, glob
from utils import simple_sentiment, detect_priority, extract_contact

def load_emails(path: str):
    return pd.read_csv(path, parse_dates=["sent_date"])

def enrich_emails(df: pd.DataFrame):
    df["sentiment"] = df["body"].apply(simple_sentiment)
    df["priority"] = df["body"].apply(detect_priority)
    df["contacts"] = df["body"].apply(extract_contact)
    return df

def draft_reply(row, kb_dir="kb"):
    base = "Hello,\n\nThank you for reaching out. "
    if row["sentiment"] == "Negative":
        base += "We understand your concern and apologize for the inconvenience. "
    kb_text = ""
    for file in glob.glob(os.path.join(kb_dir, "*.md")):
        name = os.path.basename(file).replace(".md", "")
        if name.split("_")[0] in row["subject"].lower() or name.split("_")[0] in row["body"].lower():
            kb_text = open(file).read().strip()
            break
    if kb_text:
        base += f"Here is some information that may help: {kb_text}\n\n"
    base += "Our support team will follow up with more details if needed.\n\nBest regards,\nSupport Team"
    return base
