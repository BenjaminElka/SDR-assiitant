import os
import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="AI SDR Assistant", page_icon="🤖", layout="centered")

st.title("AI SDR Assistant")
st.write("Generate prospect research, cold emails, LinkedIn messages, call openers, and follow-ups for SDR workflows.")

with st.sidebar:
    st.header("Settings")
    model = st.selectbox("Model", ["gpt-4o-mini", "gpt-4.1-mini"], index=0)
    st.caption("Set your OPENAI_API_KEY as an environment variable before running.")

company_name = st.text_input("Company name", placeholder="Example: Example Media Group")
company_website = st.text_input("Company website", placeholder="https://example.com")
contact_name = st.text_input("Contact name", placeholder="Dana Cohen")
job_title = st.text_input("Contact job title", placeholder="Head of Ad Operations")
industry = st.text_input("Industry", placeholder="Digital publishing / AdTech / SaaS")
product_context = st.text_area(
    "What are you selling?",
    value="A cybersecurity and ad quality solution that helps digital publishers and ad platforms detect malicious, deceptive, or low-quality ads before they affect users.",
    height=100,
)

prompt = f"""
You are an SDR assistant helping prepare personalized B2B outreach.

Prospect information:
- Company: {company_name}
- Website: {company_website}
- Contact: {contact_name}
- Job title: {job_title}
- Industry: {industry}

Product context:
{product_context}

Create the following:
1. A short company summary based only on the provided information. Do not invent facts.
2. Three likely business challenges this prospect may care about.
3. A personalized cold email under 120 words.
4. A LinkedIn connection message under 300 characters.
5. A 20-second cold call opener.
6. Three follow-up emails, each under 90 words.
7. A suggested CRM note summarizing why this prospect may be relevant.

Use a professional, natural sales tone. Avoid fake claims, exaggerated promises, and buzzwords.
"""

if st.button("Generate SDR Outreach"):
    if not company_name or not contact_name or not job_title:
        st.error("Please fill in at least company name, contact name, and job title.")
    elif not os.getenv("OPENAI_API_KEY"):
        st.error("OPENAI_API_KEY is not set. Add it as an environment variable first.")
    else:
        try:
            client = OpenAI()
            with st.spinner("Generating outreach..."):
                response = client.chat.completions.create(
                    model=model,
                    messages=[
                        {"role": "system", "content": "You help SDRs write accurate, ethical, personalized B2B outreach."},
                        {"role": "user", "content": prompt},
                    ],
                    temperature=0.7,
                )
            st.subheader("Generated SDR Output")
            st.markdown(response.choices[0].message.content)
        except Exception as e:
            st.error(f"Something went wrong: {e}")

st.divider()
st.caption("Personal project for demonstrating AI-assisted sales prospecting and outreach workflows.")
