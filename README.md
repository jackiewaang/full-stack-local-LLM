# full-stack-local-LLM

### Requirements
- Ollama server
- Python
- GGUF LLM models

After installing Ollama, pull the chosen LLM models. For this project, I would recommend Qwen3-1.7B and Llama3.2-1B in Q4KM GGUF format. These can be pulled from the hugging face website.

To activate the virtual environment:
source .venv/bin/activate
Then install the dependencies:
pip install requirements.txt

To start the fastAPI backend running at http://localhost:8000 :
uvicorn main:app --host 0.0.0.0 --port 8000

To start the streamlit frontend running at http://localhost:8501 :
streamlit run app.py

Make sure Ollama server runs at http://localhost:11434