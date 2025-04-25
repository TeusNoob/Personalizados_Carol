import os
import subprocess

def git_automate(commit_message, branch_name="main"):
    try:
        # 1. Verificar o status do repositório
        print("Verificando o status do repositório...")
        subprocess.run(["git", "status"], check=True)

        # 2. Adicionar todos os arquivos modificados ao índice (staging area)
        print("Adicionando arquivos modificados ao índice...")
        subprocess.run(["git", "add", "."], check=True)

        # 3. Fazer o commit com a mensagem fornecida
        print(f"Realizando commit com a mensagem: '{commit_message}'")
        subprocess.run(["git", "commit", "-m", commit_message], check=True)

        # 4. Enviar as alterações para o repositório remoto
        print(f"Enviando alterações para a branch '{branch_name}' no GitHub...")
        subprocess.run(["git", "push", "origin", branch_name], check=True)

        print("Processo concluído com sucesso!")

    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o comando Git: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    # Solicitar informações ao usuário
    commit_msg = input("Digite a mensagem do commit: ")
    branch = input("Digite o nome da branch (padrão: main): ").strip() or "main"

    # Executar o processo automatizado
    git_automate(commit_msg, branch)