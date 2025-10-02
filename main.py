import smbus
import time
from datetime import datetime

# Config to LUX CAPTION
BH1750_ADDR = 0x23
I2C_LUX_BUS = 3

#Config to HUM and TEMP CAPTION
AHT10_ADDR = 0x38
I2C_HUM_TEMP_BUS = 2

CONT_H_RES_MODE = 0x10

# Path file for save the data
PATH_FILE = "/home/caninos/Documents/Daniels/project_final/data"

bus_lux = smbus.SMBus(I2C_LUX_BUS)
bus_hum_tem = smbus.SMBus(I2C_HUM_TEMP_BUS)

def read_lux():
    try:
        bus_lux.write_byte(BH1750_ADDR, CONT_H_RES_MODE)
        time.sleep(0.2)
        data = bus_lux.read_i2c_block_data(BH1750_ADDR, 0x00, 2)
        raw = (data[0] << 8) | data[1]
        lux = raw / 1.2
        return lux
        
    except Exception as e:
        print("Erro: ", e)

def read_hum_temp():
    try:
        # Envia comando de medição
        bus_hum_tem.write_i2c_block_data(AHT10_ADDR, 0xAC, [0x33, 0x00])
        
        # Aguarda até que o sensor esteja pronto, com timeout
        for _ in range(10):  # Tenta até 10 vezes (total ~1s)
            time.sleep(0.1)
            status = bus_hum_tem.read_byte(AHT10_ADDR)
            if not (status & 0x80):  # Bit 7 == 0 → pronto
                break
        else:
            print("Timeout: sensor não ficou pronto para leitura.")
            return None, None

        # Sensor pronto, ler 6 bytes
        data = bus_hum_tem.read_i2c_block_data(AHT10_ADDR, 0x00, 6)

        raw_hum = ((data[1] << 12) | (data[2] << 4) | (data[3] >> 4))
        raw_temp = (((data[3] & 0x0F) << 16) | (data[4] << 8) | data[5])

        hum = (raw_hum * 100.0) / 1048576
        temp = (raw_temp * 200.0) / 1048576 - 50

        return hum, temp

    except Exception as e:
        print("Erro ao ler AHT10:", e)
        return None, None

    
def get_file_name():
    today = datetime.now().strftime("%d-%m-%Y")
    return f"{PATH_FILE}/data_{today}.txt"
        
if __name__ == "__main__":
    print("iniciando coleta de leituras")
    
    try:
        while True:
            lux = read_lux()
            hum, temp = read_hum_temp()
            if lux is not None and hum is not None and temp is not None:
                timestamp = datetime.now().strftime("%Y-%D-%M : %H:%M:%S")
                linha = f"[{timestamp}] Luminosidade: {lux:.2f} lux || Umidade: {hum:.2f} || Temperatura: {temp:.2f} C°\n"
                print(linha.strip())
                
                file = get_file_name()
                
                with open(file, "a") as f:
                    f.write(linha)
                    
            time.sleep(2)
    except KeyboardInterrupt:
        print("\nFechando programa...")