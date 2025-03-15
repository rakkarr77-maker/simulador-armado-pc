"""
SIMULADOR DE ARMADO DE PC - VISTA FIJA CON LISTA COMPLETA
"""
import tkinter as tk

PROCESADORES = {
    "Intel Core i7-12700K": {"socket": "LGA1700", "consumo": 125},
    "Intel Core i5-6500 (Socket: LGA1151)": {"socket": "LGA1151", "consumo": 65},
    "Intel Core i3-10100F (Socket: LGA1200)": {"socket": "LGA1200", "consumo": 65},
    "AMD Ryzen 5 5600X (Socket: AM4)": {"socket": "AM4", "consumo": 65},
    "AMD Ryzen 7 5800X3D (Socket: AM4)": {"socket": "AM4", "consumo": 105},
    "Intel Core i9-13900K (Socket: LGA1700)": {"socket": "LGA1700", "consumo": 253},
    "Intel Core i5-12400F (Socket: LGA1700)": {"socket": "LGA1700", "consumo": 65},
    "Intel Core i7-10700K (Socket: LGA1200)": {"socket": "LGA1200", "consumo": 125},
    "AMD Ryzen 9 7950X (Socket: AM5)": {"socket": "AM5", "consumo": 170},
    "AMD Ryzen 5 7600X (Socket: AM5)": {"socket": "AM5", "consumo": 105},
    "Intel Celeron G5905 (Socket: LGA1200)": {"socket": "LGA1200", "consumo": 58},
    "AMD Ryzen 3 4100 (Socket: AM4)": {"socket": "AM4", "consumo": 65},
    "Intel Core i9-14900K (Socket: LGA1700)": {"socket": "LGA1700", "consumo": 253},
    "AMD Ryzen 5 5500 (Socket: AM4)": {"socket": "AM4", "consumo": 65},
    "Intel Core i5-13600K (Socket: LGA1700)": {"socket": "LGA1700", "consumo": 125}
}

TARJETAS_MADRES = {
    "ASUS Prime Z690-P": {"socket": "LGA1700", "ram": "DDR4", "forma": "ATX", "puertos_m2": 3, "consumo": 70},
    "ASUS Prime B250M-PLUS (Socket: LGA1151)": {"socket": "LGA1151", "ram": "DDR4", "forma": "Micro-ATX", "puertos_m2": 1, "consumo": 50},
    "MSI B550 TOMAHAWK (Socket: AM4)": {"socket": "AM4", "ram": "DDR4", "forma": "ATX", "puertos_m2": 2, "consumo": 60},
    "Gigabyte H410M S2H (Socket: LGA1200)": {"socket": "LGA1200", "ram": "DDR4", "forma": "Micro-ATX", "puertos_m2": 1, "consumo": 45},
    "ASRock X670E Taichi (Socket: AM5)": {"socket": "AM5", "ram": "DDR5", "forma": "ATX", "puertos_m2": 4, "consumo": 90},
    "MSI PRO B650M-A WIFI (Socket: AM5)": {"socket": "AM5", "ram": "DDR5", "forma": "Micro-ATX", "puertos_m2": 2, "consumo": 60},
    "ASUS Prime H510M-E (Socket: LGA1200)": {"socket": "LGA1200", "ram": "DDR4", "forma": "Micro-ATX", "puertos_m2": 1, "consumo": 40},
    "Gigabyte Z790 AORUS ELITE (Socket: LGA1700)": {"socket": "LGA1700", "ram": "DDR5", "forma": "ATX", "puertos_m2": 4, "consumo": 80},
    "MSI B450 TOMAHAWK MAX II (Socket: AM4)": {"socket": "AM4", "ram": "DDR4", "forma": "ATX", "puertos_m2": 1, "consumo": 55},
    "ASUS TUF GAMING B760M-PLUS (Socket: LGA1700)": {"socket": "LGA1700", "ram": "DDR5", "forma": "Micro-ATX", "puertos_m2": 2, "consumo": 65},
    "Gigabyte B550M DS3H (Socket: AM4)": {"socket": "AM4", "ram": "DDR4", "forma": "Micro-ATX", "puertos_m2": 1, "consumo": 50},
    "ASRock B660M-ITX (Socket: LGA1700)": {"socket": "LGA1700", "ram": "DDR4", "forma": "Mini-ITX", "puertos_m2": 1, "consumo": 50},
    "MSI MEG X670E ACE (Socket: AM5)": {"socket": "AM5", "ram": "DDR5", "forma": "ATX", "puertos_m2": 4, "consumo": 100},
    "ASUS Prime A320M-K (Socket: AM4)": {"socket": "AM4", "ram": "DDR4", "forma": "Micro-ATX", "puertos_m2": 0, "consumo": 35},
    "Intel D945GCLF2 (Socket: LGA775)": {"socket": "LGA775", "ram": "DDR2", "forma": "Mini-ITX", "puertos_m2": 0, "consumo": 30}
}

MEMORIAS_RAM = {
    "Corsair Vengeance 32GB (2x16GB) DDR4": {"ram": "DDR4", "consumo": 10},
    "Kingston Fury 16GB (2x8GB) DDR4": {"ram": "DDR4", "consumo": 6},
    "AORUS 32GB (2x16GB) DDR5": {"ram": "DDR5", "consumo": 12},
    "Crucial Basics 8GB (1x8GB) DDR4": {"ram": "DDR4", "consumo": 3},
    "G.Skill Trident Z RGB 16GB (2x8GB) DDR4": {"ram": "DDR4", "consumo": 7},
    "Corsair Dominator Platinum 64GB (2x32GB) DDR5": {"ram": "DDR5", "consumo": 15},
    "Kingston ValueRAM 4GB (1x4GB) DDR4": {"ram": "DDR4", "consumo": 2},
    "Patriot Viper Steel 16GB (2x8GB) DDR4": {"ram": "DDR4", "consumo": 6},
    "XPG Spectrix D41 32GB (2x16GB) DDR4": {"ram": "DDR4", "consumo": 10},
    "TeamGroup T-Force Delta 32GB (2x16GB) DDR5": {"ram": "DDR5", "consumo": 11},
    "G.Skill Flare X5 64GB (2x32GB) DDR5": {"ram": "DDR5", "consumo": 14},
    "Corsair Vengeance LPX 16GB (1x16GB) DDR4": {"ram": "DDR4", "consumo": 5},
    "Kingston Fury Beast 8GB (1x8GB) DDR5": {"ram": "DDR5", "consumo": 4},
    "ADATA XPG Lancer 16GB (1x16GB) DDR5": {"ram": "DDR5", "consumo": 6},
    "Crucial 8GB (1x8GB) DDR4": {"ram": "DDR4", "consumo": 3}
}

TARJETAS_GRAFICAS = {
    "Sin Gráfica Dedicada (Usar integrados)": {"consumo": 0},
    "NVIDIA GTX 1660 Super": {"consumo": 125},
    "NVIDIA RTX 3060 12GB": {"consumo": 170},
    "AMD RX 6700 XT 12GB": {"consumo": 230},
    "NVIDIA RTX 4070 12GB": {"consumo": 200},
    "NVIDIA RTX 4090 24GB": {"consumo": 450},
    "NVIDIA RTX 3080 10GB": {"consumo": 320},
    "NVIDIA RTX 4060 Ti 8GB": {"consumo": 160},
    "NVIDIA GTX 1050 Ti 4GB": {"consumo": 75},
    "AMD RX 7900 XTX 24GB": {"consumo": 355},
    "AMD RX 7600 8GB": {"consumo": 165},
    "AMD RX 580 8GB": {"consumo": 185},
    "AMD RX 6500 XT 4GB": {"consumo": 107},
    "Intel Arc A770 16GB": {"consumo": 225},
    "NVIDIA GT 1030 2GB": {"consumo": 30}
}

ALMACENAMIENTO = {
    "WD Blue SA510 500GB (SSD SATA)": {"tipo": "SATA", "consumo": 2},
    "Kingston A400 1TB (SSD SATA)": {"tipo": "SATA", "consumo": 3},
    "Samsung 980 PRO 1TB (M.2 NVMe)": {"tipo": "M.2", "consumo": 6},
    "Crucial P3 500GB (M.2 NVMe)": {"tipo": "M.2", "consumo": 4},
    "Seagate Barracuda 2TB (HDD SATA)": {"tipo": "SATA", "consumo": 8},
    "WD Black SN850X 2TB (M.2 NVMe)": {"tipo": "M.2", "consumo": 7},
    "Kingston NV2 1TB (M.2 NVMe)": {"tipo": "M.2", "consumo": 4},
    "Corsair MP600 PRO 2TB (M.2 NVMe)": {"tipo": "M.2", "consumo": 8},
    "Samsung 870 EVO 1TB (SSD SATA)": {"tipo": "SATA", "consumo": 3},
    "Crucial MX500 2TB (SSD SATA)": {"tipo": "SATA", "consumo": 4},
    "Adata SU650 240GB (SSD SATA)": {"tipo": "SATA", "consumo": 2},
    "Toshiba X300 4TB (HDD SATA)": {"tipo": "SATA", "consumo": 10},
    "WD Purple 8TB (HDD SATA)": {"tipo": "SATA", "consumo": 12},
    "Seagate IronWolf 4TB (HDD SATA)": {"tipo": "SATA", "consumo": 9},
    "Sabrent Rocket 4 Plus 1TB (M.2 NVMe)": {"tipo": "M.2", "consumo": 7}
}

GABINETES = {
    "NZXT H510 (ATX)": "ATX",
    "Corsair Carbide 275R (ATX)": "ATX",
    "Cooler Master Q300L (Micro-ATX)": "Micro-ATX",
    "Thermaltake Versa H15 (Micro-ATX)": "Micro-ATX",
    "Lian Li PC-O11 Dynamic (ATX)": "ATX",
    "Fractal Design Meshify C (ATX)": "ATX",
    "Phanteks Eclipse P400A (ATX)": "ATX",
    "NZXT H7 Flow (ATX)": "ATX",
    "Corsair 4000D Airflow (ATX)": "ATX",
    "DeepCool MATREXX 55 (ATX)": "ATX",
    "Asus Prime AP201 (Micro-ATX)": "Micro-ATX",
    "Fractal Design Pop Mini Air (Micro-ATX)": "Micro-ATX",
    "SilverStone FARA H1M (Micro-ATX)": "Micro-ATX",
    "Aerocool Trinity Mini (Micro-ATX)": "Micro-ATX",
    "Cooler Master NR200P (Mini-ITX)": "Mini-ITX"
}

FUENTES_PODER = {
    "Corsair CX650M 650W 80 Plus Bronze": 650,
    "Generica 400W": 400, "EVGA 500W 80+": 500, "Seasonic Focus 750W": 750, 
    "Corsair RM850x": 850, "Corsair HX1200": 1200, "EVGA SuperNOVA 1000W": 1000, 
    "Thermaltake 850W": 850, "CM MWE 750W": 750, "XPG Core Reactor 650W": 650, 
    "Gigabyte 550W": 550, "Aerocool 500W": 500, "Acteck 500W": 500, 
    "Be Quiet! 1000W": 1000, "ASUS ROG 1200W": 1200
}

def procesar_diagnostico():
    cpu_sel = combo_cpu.get(); mobo_sel = combo_mobo.get(); ram_sel = combo_ram.get()
    gpu_sel = combo_gpu.get(); alma_sel = combo_alma.get(); gabi_sel = combo_gabi.get()
    fuente_sel = combo_fuente.get()
    
    socket_cpu = PROCESADORES[cpu_sel]["socket"]
    socket_mobo = TARJETAS_MADRES[mobo_sel]["socket"]
    ram_mobo = TARJETAS_MADRES[mobo_sel]["ram"]
    forma_mobo = TARJETAS_MADRES[mobo_sel]["forma"]
    puertos_m2_mobo = TARJETAS_MADRES[mobo_sel]["puertos_m2"]
    tipo_ram = MEMORIAS_RAM[ram_sel]["ram"]
    tipo_alma = ALMACENAMIENTO[alma_sel]["tipo"]
    soporte_gabi = GABINETES[gabi_sel]
    capacidad_fuente = FUENTES_PODER[fuente_sel]
    
    consumo_total = (PROCESADORES[cpu_sel]["consumo"] + TARJETAS_MADRES[mobo_sel]["consumo"] + 
                     MEMORIAS_RAM[ram_sel]["consumo"] + TARJETAS_GRAFICAS[gpu_sel]["consumo"] + 
                     ALMACENAMIENTO[alma_sel]["consumo"] + 50)
                     
    detalles = []
    compatible = True
    if socket_cpu == socket_mobo: detalles.append(f"✓ Socket Compatible ({socket_cpu})")
    else: detalles.append(f"✗ Socket Incompatible: CPU usa {socket_cpu}, Placa usa {socket_mobo}"); compatible = False
        
    if ram_mobo == tipo_ram: detalles.append(f"✓ Memoria RAM Compatible ({tipo_ram})")
    else: detalles.append(f"✗ Memoria Incompatible: Placa soporta {ram_mobo}, elegiste {tipo_ram}"); compatible = False
        
    if forma_mobo == "ATX" and soporte_gabi == "Micro-ATX": detalles.append(f"✗ Espacio Insuficiente: Placa {forma_mobo} no entra en gabinete {soporte_gabi}"); compatible = False
    else: detalles.append(f"✓ Formato de Gabinete Correcto ({forma_mobo} en {soporte_gabi})")
        
    if tipo_alma == "M.2" and puertos_m2_mobo == 0: detalles.append(f"✗ Almacenamiento Incompatible: La placa no tiene puertos M.2 NVMe"); compatible = False
    else: detalles.append(f"✓ Almacenamiento Compatible ({tipo_alma})")

    if capacidad_fuente >= consumo_total: detalles.append(f"✓ Potencia Suficiente (Demanda: {consumo_total}W | Fuente: {capacidad_fuente}W)")
    else: detalles.append(f"✗ Potencia Insuficiente: El sistema requiere {consumo_total}W, tu fuente da {capacidad_fuente}W"); compatible = False
        
    lbl_detalles.config(text="\n".join(detalles), fg="green" if compatible else "red")
    lbl_status.config(text="RESULTADO: ¡ARMADO VIABLE!" if compatible else "RESULTADO: COMPONENTES INCOMPATIBLES", fg="green" if compatible else "red")

ventana = tk.Tk()
ventana.title("Simulador Completo de Hardware")
ventana.geometry("700x850"); ventana.resizable(False, False)
tk.Label(ventana, text="Validador Completo de PC", font=("Arial", 14, "bold")).pack(pady=10)

def crear_menu(texto, variable, diccionario):
    tk.Label(ventana, text=texto, font=("Arial", 10, "bold")).pack()
    variable.set(list(diccionario.keys())[0]); menu = tk.OptionMenu(ventana, variable, *diccionario.keys()); menu.config(width=70); menu.pack(pady=4)

combo_cpu = tk.StringVar(ventana); crear_menu("1. Procesador (CPU):", combo_cpu, PROCESADORES)
combo_mobo = tk.StringVar(ventana); crear_menu("2. Tarjeta Madre:", combo_mobo, TARJETAS_MADRES)
combo_ram = tk.StringVar(ventana); crear_menu("3. Memoria RAM:", combo_ram, MEMORIAS_RAM)
combo_gpu = tk.StringVar(ventana); crear_menu("4. Tarjeta Gráfica (GPU):", combo_gpu, TARJETAS_GRAFICAS)
combo_alma = tk.StringVar(ventana); crear_menu("5. Almacenamiento Principal:", combo_alma, ALMACENAMIENTO)
combo_gabi = tk.StringVar(ventana); crear_menu("6. Gabinete:", combo_gabi, GABINETES)
combo_fuente = tk.StringVar(ventana); crear_menu("7. Fuente de Poder:", combo_fuente, FUENTES_PODER)

btn_validar = tk.Button(ventana, text="Verificar Compatibilidad Total", command=procesar_diagnostico, font=("Arial", 11, "bold"))
btn_validar.pack(pady=15)
lbl_status = tk.Label(ventana, text="RESULTADO: Esperando componentes...", font=("Arial", 12, "bold")); lbl_status.pack()
lbl_detalles = tk.Label(ventana, text="", font=("Arial", 10), justify="left"); lbl_detalles.pack(pady=10)
ventana.mainloop()