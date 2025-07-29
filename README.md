# 💰 Finance Project Setup

Questo progetto utilizza Python e un ambiente virtuale per gestire le dipendenze in modo ordinato.

## 🛠 Requisiti

- Python 3.8 o superiore
- pip installato

## ⚙️ Setup ambiente virtuale

1. Clona il repository (se applicabile):
    ```bash
    git clone https://github.com/TUO_REPO/finance-project.git
    cd finance-project
    ```

2. Crea e attiva l'ambiente virtuale:
    ```bash
    python -m venv finance
    source finance/bin/activate  # Su macOS/Linux
    finance\Scripts\activate     # Su Windows
    ```

3. Installa i pacchetti necessari:
    ```bash
    pip install -r requirements.txt
    ```

4. Avvia il tuo script:
    ```bash
    python main.py
    ```

## Builda
    ```bash
    pyinstaller --onefile --console --name "Delfi" --icon=favicon.ico lib/main.py
    ```


## ✅ Disattiva l'ambiente virtuale

Quando hai finito:
```bash
deactivate
