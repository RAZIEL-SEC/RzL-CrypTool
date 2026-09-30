# 🔐 Runtime Cryptography & Code Protection

Ferramenta desenvolvida em **Python** para estudos de criptografia, proteção de arquivos, bypass em 90% dos antivirus e ofuscação de código em tempo de execução.

O projeto reúne ferramentas de **Cripter** e **Loader**, permitindo proteger arquivos por meio de criptografia XOR, gerar chaves automaticamente e trabalhar com o conteúdo protegido durante a execução em memória.

## Uso integrado com as seguintes ferramentas:
Stealer: `https://github.com/RAZIEL-SEC/RzL-Stealer.git`

Compilador de código obfuscado: `https://github.com/RAZIEL-SEC/Builder-to-CrypTool.git`

## 🛠️ Instalação e Uso

### 1. Instalar o Python 3.10
```powershell
winget install Python.Python.3.10
```

### 2. Criar uma pasta para o projeto
```bash
mkdir Build_Project
cd Build_Project
```


### 3. Criar o ambiente virtual

```bash
python -m venv venv
```

### 4. Ativar o ambiente virtual

No PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

No CMD:

```cmd
venv\Scripts\activate
```

### 5. Clonar o repositório

```bash
git clone https://github.com/RAZIEL-SEC/RzL-CrypTool.git
cd RzL-CrypTool
```

### 6. Instalar as dependências

```bash
pip install -r requirements.txt
```

```bash
pip install requests psutil browser_cookie3

```
```bash
pip install cryptography pycryptodome

```
```bash
pip install opencv-python pywin32

```
```bash
pip install pyinstaller auto-py-to-exe

```
---

## 🚀 Recursos

- 🔐 **Cripter**
  - Recebe um arquivo como entrada.
  - Gera uma chave de criptografia.
  - Criptografa o conteúdo utilizando **XOR**.
  - Gera um novo arquivo protegido.

- 🧠 **Loader**
  - Carrega o arquivo protegido.
  - Recupera o conteúdo utilizando a chave correspondente.
  - Processa o conteúdo durante a execução em memória.

- 🐍 **Python**
  - Suporte a experimentos envolvendo scripts Python.
  - Proteção e ofuscação de código em runtime.
 
- ⚙️ **C++**
  - Suporte a experimentos envolvendo scripts C++.
  - Proteção e ofuscação de código em runtime.
   
## 🔄 Funcionamento

```text

┌──────────────────┐
│ Arquivo original │
└────────┬─────────┘
         ↓
┌──────────────────┐
│      CRIPTER     │
└────────┬─────────┘
         ↓
┌──────────────────┐
│ Geração da chave │
└────────┬─────────┘
         ↓
┌──────────────────┐
│   Criptografia   │
│       XOR        │
└────────┬─────────┘
         ↓
┌──────────────────┐
│   Conversao em   │
│     Base 64      │
└────────┬─────────┘
         ↓
┌──────────────────┐
│ Arquivo protegido│
└────────┬─────────┘
         ↓
┌──────────────────┐
│      LOADER      │
└────────┬─────────┘
         ↓
┌──────────────────┐
│ Processamento em │
│     memória      │
└──────────────────┘
