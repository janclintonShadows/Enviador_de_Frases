@echo off

call conda activate automacao

streamlit.exe run "%~pd0\main.py"
