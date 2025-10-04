import os
import subprocess
import sys

venv_nome = "venv"

subprocess.run([sys.executable, "-m", "venv", venv_nome])


if os.name == "nt":  
    pip_path = os.path.join(venv_nome, "Scripts", "pip.exe")
    python_path = os.path.join(venv_nome, "Scripts", "python.exe")
else:  
    pip_path = os.path.join(venv_nome, "bin", "pip")
    python_path = os.path.join(venv_nome, "bin", "python")

subprocess.run([pip_path, "install", "--upgrade", "pip"])
subprocess.run([pip_path, "install", "-r", "requirements.txt"])


subprocess.run([python_path, "-m", "ipykernel", "install", "--user", "--name", venv_nome, "--display-name", f"Python ({venv_nome})"])

print("\n✅ Setup concluído! Ative o ambiente virtual e abra o notebook.")
if os.name == "nt":
    print(f"Para ativar o venv no Windows: {venv_nome}\\Scripts\\activate")
else:
    print(f"Para ativar o venv no Linux/Mac: source {venv_nome}/bin/activate")