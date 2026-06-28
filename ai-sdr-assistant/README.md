# AI SDR Assistant

AI SDR Assistant is a personal project that demonstrates how AI can support Sales Development Representative workflows.

The app helps generate prospect research, personalized cold emails, LinkedIn messages, cold call openers, follow-up sequences, and CRM notes.

## Why I built it

I built this project to better understand how AI can improve sales productivity. SDRs spend a lot of time researching prospects and preparing outreach. This assistant helps speed up that process while keeping the human SDR in control.

## Features

- Company and prospect input form
- AI-generated business challenges
- Personalized cold email
- LinkedIn connection message
- Cold call opener
- Follow-up email sequence
- CRM-ready prospect note
- Simple Streamlit interface

## Tech Stack

- Python
- Streamlit
- OpenAI API
- Prompt engineering

## How to run

1. Clone the repository.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Add your OpenAI API key:

```bash
export OPENAI_API_KEY="your_api_key_here"
```

On Windows PowerShell:

```powershell
$env:OPENAI_API_KEY="your_api_key_here"
```

4. Run the app:

```bash
streamlit run app.py
```

## Example use case

A sales development representative enters a company name, website, contact name, job title, and product context. The AI assistant generates a first draft of outreach materials that the SDR can review, edit, and personalize before sending.

## Ethical note

The tool is designed to assist with drafting, not to replace human judgment. Users should verify all company information and avoid making claims that are not supported by real research.
