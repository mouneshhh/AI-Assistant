import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from email_pipeline import load_emails, enrich_emails, draft_reply

st.set_page_config(page_title="AI Communication Assistant", layout="wide")

st.title("📧 AI-Powered Communication Assistant")

df = load_emails("data/sample_emails.csv")
df = enrich_emails(df)

st.sidebar.header("Dashboard Stats")
st.sidebar.write("Total emails:", len(df))
st.sidebar.write("Urgent:", (df["priority"]=="Urgent").sum())
st.sidebar.write("Negative:", (df["sentiment"]=="Negative").sum())

sent_counts = df["sentiment"].value_counts()
prio_counts = df["priority"].value_counts()

fig1, ax1 = plt.subplots()
sent_counts.plot(kind="bar", ax=ax1, title="Sentiment")
st.sidebar.pyplot(fig1)

fig2, ax2 = plt.subplots()
prio_counts.plot(kind="bar", ax=ax2, title="Priority")
st.sidebar.pyplot(fig2)

df = df.sort_values(by="priority", ascending=False)

st.subheader("Support Emails")
for i, row in df.iterrows():
    with st.expander(f"{row['subject']} ({row['priority']}, {row['sentiment']})"):
        st.write("From:", row["sender"])
        st.write("Date:", row["sent_date"])
        st.write("Body:", row["body"])
        st.write("Contacts:", row["contacts"])
        draft = draft_reply(row)
        new_draft = st.text_area("AI Draft Reply", draft, key=f"draft_{i}")
        if st.button("Save Reply", key=f"save_{i}"):
            with open(f"outbox/reply_{i}.txt", "w") as f:
                f.write(new_draft)
            st.success("Reply saved to outbox/")
