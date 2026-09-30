import base64
import sys

# --- TEMPLATE DO BUILDER BASICO (Execução Direta) ---
PAYLOAD_TEMPLATE_PY = """
import base64 as _b64
import sys

def run_payload():
    # =========== CONFIGS ===========
    secret_data = "{secret_data}" 
    secret_key = {secret_key} 
    # ===============================

    decode_func = _b64.b64decode
    execute_func = exec
    
    try:
        # Processo DECRYPT
        raw_bytes = decode_func(secret_data)
        
        # XOR Manual
        decrypted_bytes = bytes([b ^ secret_key for b in raw_bytes])
        
        # Conversao para string
        final_code = decrypted_bytes.decode('utf-8')

        # Execucao
        execute_func(final_code, globals())
        
    except Exception as e:
        pass
    
if __name__ == "__main__":
    run_payload()
"""

# --- FUNÇÕES ---

def xor_cipher(data, key):
    """Realiza a operação XOR entre os bytes e a chave."""
    return bytes([b ^ key for b in data])

def encrypt_file(file_path, key):
    """Lê o arquivo, aplica a ofuscação e retorna a string Base64."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        data = content.encode('utf-8')
        encrypted = xor_cipher(data, key)
        return base64.b64encode(encrypted).decode('utf-8')
    except FileNotFoundError:
        return "FILE_NOT_FOUND"
    except Exception as e:
        return str(e)

def generate_py_payload(obfuscated_code, key, output_file):
    """Injeta o código ofuscado no template Python e salva o arquivo."""
    try:
        payload_content = PAYLOAD_TEMPLATE_PY.format(
            secret_data=obfuscated_code,
            secret_key=key
        )
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(payload_content)
        return True
    except Exception as e:
        print(f"[-] Erro ao gerar payload Python: {e}")
        return False

def main():
    while True:
        print("\n" + "="*35)
        print("   SISTEMA DE OFUSCAÇÃO")
        print("="*35)
        print("[1] Modo Python (Gerar Payload Executável)")
        print("[2] Modo C++ (Gerar Dados para Loader)")
        print("[3] Sair")
        print("-" * 35)
        
        opcao = input("[?] Selecione uma opção: ").strip()

        if opcao == '3':
            break
        
        elif opcao == '1':
            # --- FLUXO PYTHON ---
            arquivo_alvo = input("[>] Arquivo para ofuscar (.py): ").strip()
            try:
                chave_input = input("[>] Chave numérica: ").strip()
                chave = int(chave_input)
            except ValueError:
                print("\n[!] Erro: A chave deve ser um número inteiro.")
                continue

            print("\n[*] Ofuscando e gerando payload Python...")
            resultado_ofuscado = encrypt_file(arquivo_alvo, chave)

            if resultado_ofuscado == "FILE_NOT_FOUND":
                print(f"\n[!] Erro: Arquivo '{arquivo_alvo}' não encontrado.")
                continue

            nome_saida = input("[>] Nome do arquivo de saída (ex: payload.py): ").strip()
            if not nome_saida.endswith(".py"):
                nome_saida += ".py"

            if generate_py_payload(resultado_ofuscado, chave, nome_saida):
                print("\n" + "-"*50)
                print(f"[+] SUCESSO!")
                print(f"[+] Arquivo gerado: {nome_saida}")
                print(f"[+] Chave: {chave}")
                print("-" * 50)
            else:
                print("\n[!] Falha na geração.")

            feedback = input("\n[?] Outra operação? (s/n): ").strip().lower()
            if feedback != 's': break

        elif opcao == '2':
            # --- FLUXO C++ (APENAS DADOS) ---
            arquivo_alvo = input("[>] Arquivo para ofuscar: ").strip()
            try:
                chave_input = input("[>] Chave numérica: ").strip()
                chave = int(chave_input)
            except ValueError:
                print("\n[!] Erro: A chave deve ser um número inteiro.")
                continue

            print("\n[*] Processando dados para C++...")
            resultado_ofuscado = encrypt_file(arquivo_alvo, chave)

            if resultado_ofuscado == "FILE_NOT_FOUND":
                print(f"\n[!] Erro: Arquivo '{arquivo_alvo}' não encontrado.")
                continue

            # Exibicao limpa para o usuario copiar e colar no loader C++
            
            print("\n" + "="*50)
            print("   DADOS PARA LOADER C++")
            print("="*50)
            print(f"\n[!] CHAVE (Key): {chave}")
            print(f"\n[!] STRING (Base64):")
            print("-" * 50)
            print(resultado_ofuscado)
            print("-" * 50)
            print("\n[!] Copie a string e a chave acima para o seu código C++.")
            print("="*50)

            salvar = input("\n[?] Salvar dados em .txt para facilitar? (s/n): ").strip().lower()
            if salvar == 's':
                nome_txt = input("[>] Nome do arquivo de saída: ").strip()
                if not nome_txt.endswith(".txt"):
                    nome_txt += ".txt"
                try:
                    with open(nome_txt, "w", encoding="utf-8") as f:
                        f.write(f"KEY: {chave}\n")
                        f.write(f"DATA: {resultado_ofuscado}\n")
                    print(f"[+] Salvo com sucesso em: {nome_txt}")
                except Exception as e:
                    print(f"[!] Erro ao salvar: {e}")

            feedback = input("\n[?] Outra operação? (s/n): ").strip().lower()
            if feedback != 's': break
        else:
            print("[!] Opção inválida.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[-] Saindo...")
        sys.exit(0)
