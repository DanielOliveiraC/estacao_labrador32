# 🌱 Estação Labrador 32 – Datalogger

[![GitHub](https://img.shields.io/badge/github-repo-blue?logo=github)](https://github.com/DanielOliveiraC/estacao_labrador32)

## 📌 Sobre o Projeto
Este projeto demonstra como utilizar a placa **Labrador 32**, desenvolvida pelo [Caninos Loucos](https://caninosloucos.org/), para criar um **datalogger ambiental** capaz de coletar e registrar em tempo real os dados de **luminosidade, umidade e temperatura**.  
Os valores são gravados em um arquivo `.txt` no microSD, juntamente com um **timestamp**, criando um histórico contínuo de medições.  

O projeto foi pensado para simular o controle de variáveis ambientais em **aviários e granjas**, mas pode ser facilmente adaptado para outros contextos como **automação agrícola, monitoramento de estufas e aplicações IoT**.

---

## 🔧 Tecnologias Utilizadas
- **Placa Labrador 32**  
- **Python 3**  
- **Biblioteca SMBus (I2C)**  
- Sensores:
  - **AHT10** (Temperatura e Umidade)  
  - **BH1750** (Luminosidade)  

---

## 🚀 Como Executar
1. Clone o repositório:  
   ```bash
   git clone https://github.com/DanielOliveiraC/estacao_labrador32.git
   cd estacao_labrador32
   ```

2. Instale as dependências:  
   ```bash
   sudo apt-get install python3-smbus
   ```

3. Execute o script principal:  
   ```bash
   python3 main.py
   ```

4. Os dados coletados serão exibidos no terminal e salvos em `data.txt` no cartão **microSD**.  

---

## 📊 Lógica de Registro
Os dados **só são gravados** se todos os sensores responderem corretamente.  
Isto pode ser representado pela lógica de uma **porta AND**:

| Lux válido | Umidade válida | Temperatura válida | Registrar linha |
|------------|----------------|---------------------|-----------------|
| 0          | 0              | 0                   | 0               |
| 0          | 1              | 1                   | 0               |
| 1          | 1              | 1                   | 1               |

---

## 📈 Melhorias Futuras
- Organização automática dos arquivos por dia/mês.  
- Integração com **banco de dados em nuvem**.  
- Visualização em **dashboard (Power BI / Grafana)**.  
- Inclusão de novos sensores (ex.: amônia, CO₂).  

---

## 🎥 Demonstração
Será disponibilizado em breve um vídeo no YouTube mostrando o funcionamento do projeto. O link será incluído aqui.  

---

## 📄 Licença
Este projeto está sob a licença MIT. Sinta-se à vontade para usar e contribuir.  
