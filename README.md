# 🔁 Sistema Intelligente Gestione Resi - Fashion Sector

Questa è una demo basata su Streamlit che mostra un'applicazione reale della **comunicazione Agent-to-Agent (A2A)** con orchestrazione interna tramite **Model Context Protocol (MCP)**. 
L'applicazione è progettata per automatizzare e ottimizzare il processo di **gestione dei resi** nel settore fashion.

---

## 📦 Flusso degli Agenti

### 👤 1. Customer Agent
- Riceve la richiesta di reso da parte del cliente.
- Classifica automaticamente il motivo del reso.

### 🔍 2. Product Agent
- Valuta lo stato del prodotto a partire da una descrizione (può essere esteso con immagini).

### 🚚 3. Logistics Agent
- Simula l'organizzazione del ritiro del prodotto.

### ⚖️ 4. Decision Agent
- Decide in autonomia se approvare o meno il reso, combinando il motivo e lo stato del prodotto.

---

## 🧪 Come usare il progetto localmente

### 1. Clona il repository
```bash
git clone https://github.com/tuo-username/fashion-returns-streamlit-demo.git
cd fashion-returns-streamlit-demo
```

### 2. Crea un ambiente virtuale (opzionale)
```bash
python -m venv venv
source venv/bin/activate  # Su Windows: venv\Scripts\activate
```

### 3. Installa le dipendenze
```bash
pip install -r requirements.txt
```

### 4. Crea un file `.env` con la tua chiave OpenAI
```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxx
```

### 5. Avvia l'applicazione
```bash
streamlit run app.py
```

---

## ☁️ Deploy su Streamlit Cloud

1. Crea un repo su GitHub e carica i file (`app.py`, `requirements.txt`, `.env.example`, `README.md`)
2. Vai su [streamlit.io/cloud](https://streamlit.io/cloud) e collega il repo
3. Imposta la variabile `OPENAI_API_KEY` nei Secrets
4. Clicca **Deploy** 🚀

---

## 📍 Esempi di input

- **Richiesta Cliente:** "Vorrei restituire il vestito, la taglia è troppo piccola"
- **Descrizione Prodotto:** "Il prodotto è stato provato, ma non presenta danni."

---

## 📈 Estensioni possibili

- Integrazione con immagini e visione artificiale per valutare il prodotto
- Integrazione con ERP/logistica reale
- Dashboard amministrativa

---

## 🤖 Tecnologie usate

- Python 3.10+
- [Streamlit](https://streamlit.io)
- [OpenAI GPT-4](https://openai.com/gpt-4)
- python-dotenv

---

## 📬 Contatti
