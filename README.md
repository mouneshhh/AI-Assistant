**AI Communication Assistant**

The AI Communication Assistant is a simple but powerful tool that helps automate communication workflows, such as parsing and managing emails. It’s designed to be lightweight, easy to set up, and flexible enough to adapt to your needs.

## 🚀 Features
- Automatically parse and process emails  
- Easy configuration with a `config.yaml` file  
- Clean, modular codebase that’s easy to extend  
- Runs with just a few commands  

## 📂 Project Structure
ai_comm_assistant/app.py ---> Main application entry point
<br>
 email_pipeline.py ----> Email processing pipeline
<br>
 utils.py ---> Helper functions
<br>
 config.example.yaml  ---> Example configuration file
<br>
 requirements.txt  ---> Python dependencies


## ⚙️ Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/mouneshhh/AI-Assistant.git
   cd AI-Assistant/ai_comm_assistant

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # macOS/Linux
   venv\Scripts\activate      # Windows
3. Install dependencies:
   ```bash
   pip install -r requirements.txt

4. Edit config.yaml with your settings (API keys, email server details, etc.).
5.Run the assistant:
   ```bash
   streamlit run app.py
