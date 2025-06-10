import requests
import openpyxl

# 📄 Caminho da planilha Excel
EXCEL_PATH = "contatos.xlsx"

# 🔐 Credenciais da API BRASIL (substitua pelos seus dados reais)
API_URL = "https://gateway.apibrasil.io/api/v2/whatsapp/sendText"
HEADERS = {
    "Content-Type": "application/json",
    "DeviceToken": "seu devicetoken",
    "Authorization": "Bearer seu token"
}

# 📤 Função para enviar mensagem via API BRASIL
def enviar_mensagem(telefone, mensagem):
    data = {
        "number": telefone,
        "text": mensagem
    }

    response = requests.post(API_URL, headers=HEADERS, json=data)

    if response.status_code == 200:
        print(f"✅ Mensagem enviada para {telefone}")
        print(response.text)
    else:
        print(f"❌ Erro ao enviar para {telefone}. Código: {response.status_code}")
        print(response.text)

# 📚 Abrir a planilha de contatos
wb = openpyxl.load_workbook(EXCEL_PATH)
sheet = wb.active

# 🔁 Enviar mensagens para cada contato
for row in sheet.iter_rows(min_row=2, values_only=True):
    nome, telefone, mensagem_base = row
    if nome and telefone and mensagem_base:
        mensagem_final = f"{nome}, {mensagem_base}"
        enviar_mensagem(str(telefone), mensagem_final)
