@echo off
chcp 65001 >nul
cd /d "C:\Users\yujin\OneDrive\Desktop\claude\rename-tax-invoices"

pip show PyMuPDF >nul 2>&1 || pip install PyMuPDF
pip show google-genai >nul 2>&1 || pip install google-genai
pip show watchdog >nul 2>&1 || pip install watchdog

python watcher.py
pause
