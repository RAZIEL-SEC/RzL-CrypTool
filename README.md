# 🔐 Runtime Cryptography & Code Protection

Ferramenta desenvolvida em **Python** para estudos de criptografia, proteção de arquivos, bypass em 90% dos antivirus e ofuscação de código em tempo de execução.

O projeto reúne ferramentas de **Cripter** e **Loader**, permitindo proteger arquivos por meio de criptografia XOR, gerar chaves automaticamente e trabalhar com o conteúdo protegido durante a execução em memória.

## Uso integrado com as seguintes ferramentas:
`https://github.com/RAZIEL-SEC/RzL-Stealer.git` e `https://github.com/RAZIEL-SEC/Builder-to-CrypTool.git`

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
