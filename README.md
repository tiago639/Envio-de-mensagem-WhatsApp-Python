
# 📤 Automação de Envio de Mensagens no WhatsApp com API BRASIL e Excel

Este projeto realiza o envio automatizado de mensagens personalizadas via WhatsApp utilizando a **API BRASIL**, com base em uma planilha Excel contendo os contatos e as mensagens.

O script lê os dados de uma planilha `.xlsx`, monta mensagens no formato `"Nome, Mensagem Base"` e envia essas mensagens via requisições HTTP à API BRASIL.

## ✅ Funcionalidades

- 📥 Leitura de contatos e mensagens a partir de um arquivo Excel
- 💬 Geração de mensagens personalizadas por linha
- 🚀 Envio automatizado via API BRASIL
- 📊 Log de envio no terminal (sucesso ou erro)

## 📁 Estrutura do Projeto

📦 whatsapp_sender/  
├── enviar_mensagens.py → Script principal  
├── contatos.xlsx → Planilha de contatos  
└── README.md → Documentação do projeto

## 📝 Formato da Planilha

A planilha `contatos.xlsx` deve conter os seguintes dados a partir da **linha 2**:

| Nome        | Telefone        | Mensagem Base               |
|-------------|-----------------|-----------------------------|
| João Silva  | 5521999999999   | sua encomenda foi enviada. |
| Maria Souza | 5521988888888   | seu pedido foi aprovado.   |

- O número deve estar no formato internacional (ex: `55` para o Brasil, sem símbolos ou espaços).
- A primeira linha (cabeçalho) será ignorada.

## ⚙️ Configuração

No topo do arquivo `enviar_mensagens.py`, edite os dados da API:

```python
EXCEL_PATH = "contatos.xlsx"

HEADERS = {
    "Content-Type": "application/json",
    "DeviceToken": "seu_device_token_aqui",
    "Authorization": "Bearer seu_token_aqui"
}
```

## 📦 Instalação

Clone este repositório:

```bash
git clone https://github.com/seuusuario/whatsapp_sender.git
cd whatsapp_sender
```

Instale as dependências:

```bash
pip install requests openpyxl
```

## ▶️ Execução

Execute o script Python:

```bash
python enviar_mensagens.py
```

---

## 💬 Exemplo de Mensagem Enviada

Para a seguinte linha da planilha:

| Nome        | Telefone        | Mensagem Base               |
|-------------|-----------------|-----------------------------|
| João Silva  | 5521999999999   | sua encomenda foi enviada. |

A mensagem enviada será:

```
João Silva, sua encomenda foi enviada.
```

---

## 🧾 Requisitos

- Python 3.7 ou superior
- Instalar as Dependencias ( pip install requests / pip install openpyxl )
- Conta ativa na [API BRASIL](https://apibrasil.me)
- Token e DeviceToken válidos
- Planilha Excel no formato correto

---

## ⚠️ Observações

- A API BRASIL pode ter limitações de uso no plano gratuito.
- Use a automação de forma ética e legal, evitando spam.
- Ideal para empresas que têm autorização prévia dos destinatários.

---
## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENÇA.txt) para detalhes.

## 👤 Autor

**Tiago Fonseca**
