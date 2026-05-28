# Getting Started — Set Up the Starter App

Open a new PowerShell session and set up the starter app using the following instructions.

## 1. Clone the Lab Repository

Clone the lab repo and navigate into it:

```powershell
git clone https://github.com/microsoft/Build26-LAB501.git
```
```powershell
cd Build26-LAB501
```

## 2. Copy the Starter App

The `src/` directory contains a ready-to-go Python Flask application — a LEGO set browser backed by Azure Cosmos DB. Copy it to a new `lego-app` working directory and initialize it as its own Git repo:

```powershell
Copy-Item -Recurse src lego-set-browser
```
```powershell
cd lego-set-browser
```
```powershell
git config --global user.name "Your Name"
```
```powershell
git config --global user.email "you@example.com"
```
```powershell
git init && git add -A && git commit -m "init"
```

All subsequent commands should be run from the `lego-app` directory.

> 💡 **What's in the starter app?** `app.py` is a Flask web application with routes for browsing, searching, and viewing LEGO sets. It connects to an Azure Cosmos DB to query set data. `requirements.txt` defines the Python dependencies (Flask, azure-cosmos, azure-identity, gunicorn). A `Dockerfile` is included for containerized deployment. The app uses `DefaultAzureCredential` for passwordless authentication to Cosmos DB.

## 3. Checkpoint: Verify Setup

```powershell
git log --oneline
```

You should see the initial commit.

Install dependencies and start the app:

```powershell
pip install -r requirements.txt
```
```powershell
python app.py
```

Open a browser and navigate to `http://localhost:5000` — you should see the LEGO set browser home page with featured sets loaded from Cosmos DB. Press **Ctrl + C** to stop the running server.

> ⚠️ **Cosmos DB connectivity:** The app connects to a pre-provisioned Cosmos DB in your lab subscription. If you see connection errors, verify you are logged in to Azure CLI (`az login`) — the app uses `DefaultAzureCredential` which picks up your CLI credentials locally.

✅ You now have a working starter app ready to be integrated into AZD and Copilot CLI–driven workflows.

---

**Next:** [Scenario 1 — Ship It & Harden It →](04-scenario-1-ship-and-harden.md)
