# uhm-counter
A small REST API exercise: uhm-counter to count the uhms in your presentation 

Install uhm counter
```bash
git clone https://github.com/Spansky/uhm-counter.git
cd uhm-counter
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Run uhm-counter
```
uvicorn main:app --reload
```

Test uhm-counter
```
pytest
```

Open the uhm-counter in your browser:
http://localhost:8000/docs