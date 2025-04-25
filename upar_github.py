import os

# Diretório onde os arquivos serão salvos
output_dir = ".\\botoes\\moldes"

# Garante que o diretório existe
os.makedirs(output_dir, exist_ok=True)

# Número de produtos (botões) a serem gerados
num_produtos = 9

# Loop para criar os arquivos
for i in range(1, num_produtos + 1):
    # Nome do arquivo
    file_name = f"molde{i}.html"
    file_path = os.path.join(output_dir, file_name)
    
    # Código do arquivo HTML
    html_code = f"""
<!-- {file_name} -->
<!-- Este arquivo contém o código do botão de pagamento para o produto {i}. -->
<!-- Altere o 'data-preference-id' abaixo para o ID único do seu produto no Mercado Pago. -->

<script src="https://www.mercadopago.com.br/integrations/v1/web-payment-checkout.js"
  data-preference-id="ID_UNICO_PRODUTO_{i}" data-source="button">
</script>
"""

    # Salva o arquivo
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(html_code)

print(f"{num_produtos} arquivos HTML foram criados com sucesso no diretório '{output_dir}'.")