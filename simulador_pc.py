"""
SIMULADOR DE ARMADO DE PC - VERSIÓN COMPLETA (GUI)
===================================================
Nuevas integraciones:
    - Tarjetas Gráficas (GPUs) con cálculo de consumo.
    - Almacenamiento (SATA vs M.2 NVMe) con validación de puertos.
    - Opciones expandidas de hardware.
"""
import tkinter as tk

# --- DATOS ESTÁTICOS DE HARDWARE ---

PROCESADORES = {
    "Intel Core i5-6500": {"socket": "LGA1151", "consumo": 65},
    "Intel Core i7-12700K": {"socket": "LGA1700", "consumo": 125},
    "Intel Core i3-10100F": {"socket": "LGA1200", "consumo": 65},
    "AMD Ryzen 5 5600X": {"socket": "AM4", "consumo": 65},
    "AMD Ryzen 7 5800X3D": {"socket": "AM4", "consumo": 105}
}

TARJETAS_MADRES = {
    "ASUS Prime B250M-PLUS": {"socket": "LGA1151", "ram": "DDR4", "forma": "Micro-ATX", "puertos_m2": 1, "consumo": 50},
    "ASUS Prime Z690-P": {"socket": "LGA1700", "ram": "DDR4", "forma": "ATX", "puertos_m2": 3, "consumo": 70},
    "MSI B550 TOMAHAWK": {"socket": "AM4", "ram": "DDR4", "forma": "ATX", "puertos_m2": 2, "consumo": 60},
    "Gigabyte H410M S2H": {"socket": "LGA1200", "ram": "DDR4", "forma": "Micro-ATX", "puertos_m2": 1, "consumo": 45},
    "Placa Generica H110": {"socket": "LGA1151", "ram": "DDR4", "forma": "Micro-ATX", "puertos_m2": 0, "consumo": 40}
}

MEMORIAS_RAM = {
    "Kingston Fury 16GB (2x8GB) DDR4": {"ram": "DDR4", "consumo": 6},
    "Corsair Vengeance 32GB (2x16GB) DDR4": {"ram": "DDR4", "consumo": 10},
    "AORUS 32GB (2x16GB) DDR5": {"ram": "DDR5", "consumo": 12}
}

TARJETAS_GRAFICAS = {
    "Sin Gráfica Dedicada (Usar Integrados)": {"consumo": 0},
    "NVIDIA GeForce GTX 1660 Super": {"consumo": 125},
    "NVIDIA GeForce RTX 3060 12GB": {"consumo": 170},
    "AMD Radeon RX 6700 XT 12GB": {"consumo": 230},
    "NVIDIA GeForce RTX 4070 12GB": {"consumo": 200}
}

ALMACENAMIENTO = {
    "Kingston A400 1TB (SSD SATA)": {"tipo": "SATA", "consumo": 3},
    "WD Blue SA510 500GB (SSD SATA)": {"tipo": "SATA", "consumo": 2},
    "Samsung 980 PRO 1TB (M.2 NVMe)": {"tipo": "M.2", "consumo": 6},
    "Crucial P3 500GB (M.2 NVMe)": {"tipo": "M.2", "consumo": 4},
    "Seagate Barracuda 2TB (HDD SATA)": {"tipo": "SATA", "consumo": 8}
}

GABINETES = {
    "Corsair Carbide 275R (ATX)": "ATX",
    "NZXT H510 (ATX)": "ATX",
    "Cooler Master Q300L (Micro-ATX)": "Micro-ATX",
    "Thermaltake Versa H15 (Micro-ATX)": "Micro-ATX"
}

FUENTES_PODER = {
    "Generica 400W (Sin Certificación)": 400,
    "EVGA 500W 80 Plus White": 500,
    "Corsair CX650M 650W 80 Plus Bronze": 650,
    "Seasonic Focus 750W 80 Plus Gold": 750,
    "Corsair RM850x 850W 80 Plus Gold": 850
}

def procesar_diagnostico():
    """ Lógica matemática determinista para evaluar compatibilidad """
    # Obtener valores de la interfaz
    cpu_sel = combo_cpu.get()
    mobo_sel = combo_mobo.get()
    ram_sel = combo_ram.get()
    gpu_sel = combo_gpu.get()
    alma_sel = combo_alma.get()
    gabi_sel = combo_gabi.get()
    fuente_sel = combo_fuente.get()
    
    # Extraer atributos
    socket_cpu = PROCESADORES[cpu_sel]["socket"]
    socket_mobo = TARJETAS_MADRES[mobo_sel]["socket"]
    ram_mobo = TARJETAS_MADRES[mobo_sel]["ram"]
    forma_mobo = TARJETAS_MADRES[mobo_sel]["forma"]
    puertos_m2_mobo = TARJETAS_MADRES[mobo_sel]["puertos_m2"]
    
    tipo_ram = MEMORIAS_RAM[ram_sel]["ram"]
    tipo_alma = ALMACENAMIENTO[alma_sel]["tipo"]
    soporte_gabi = GABINETES[gabi_sel]
    capacidad_fuente = FUENTES_PODER[fuente_sel]
    
    # Cálculo de consumos
    consumo_total = (PROCESADORES[cpu_sel]["consumo"] + 
                     TARJETAS_MADRES[mobo_sel]["consumo"] + 
                     MEMORIAS_RAM[ram_sel]["consumo"] + 
                     TARJETAS_GRAFICAS[gpu_sel]["consumo"] + 
                     ALMACENAMIENTO[alma_sel]["consumo"] + 50) # +50W de margen (ventiladores, USBs)
                     
    detalles = []
    compatible = True
    
    # 1. Validación de Socket
    if socket_cpu == socket_mobo:
        detalles.append(f"✓ Socket Compatible ({socket_cpu})")
    else:
        detalles.append(f"✗ Socket Incompatible: CPU usa {socket_cpu}, Placa usa {socket_mobo}")
        compatible = False
        
    # 2. Validación de RAM
    if ram_mobo == tipo_ram:
        detalles.append(f"✓ Memoria RAM Compatible ({tipo_ram})")
    else:
        detalles.append(f"✗ Memoria Incompatible: Placa soporta {ram_mobo}, elegiste {tipo_ram}")
        compatible = False
        
    # 3. Validación de Factor de Forma
    if forma_mobo == "ATX" and soporte_gabi == "Micro-ATX":
        detalles.append(f"✗ Espacio Insuficiente: Placa {forma_mobo} no entra en gabinete {soporte_gabi}")
        compatible = False
    else:
        detalles.append(f"✓ Formato de Gabinete Correcto ({forma_mobo} en {soporte_gabi})")
        
    # 4. Validación de Almacenamiento (M.2)
    if tipo_alma == "M.2" and puertos_m2_mobo == 0:
        detalles.append(f"✗ Almacenamiento Incompatible: La placa no tiene puertos para discos M.2 NVMe")
        compatible = False
    else:
        detalles.append(f"✓ Almacenamiento Compatible ({tipo_alma})")

    # 5. Validación de Potencia Eléctrica
    if capacidad_fuente >= consumo_total:
        detalles.append(f"✓ Potencia Suficiente (Demanda: {consumo_total}W | Fuente: {capacidad_fuente}W)")
    else:
        detalles.append(f"✗ Potencia Insuficiente: El sistema requiere {consumo_total}W, tu fuente da {capacidad_fuente}W")
        compatible = False
        
    # Despliegue de resultados
    texto_resultado = "\n".join(detalles)
    lbl_detalles.config(text=texto_resultado, fg="green" if compatible else "red")
    
    if compatible:
        lbl_status.config(text="RESULTADO: ¡ARMADO VIABLE!", fg="green")
    else:
        lbl_status.config(text="RESULTADO: COMPONENTES INCOMPATIBLES", fg="red")

# --- CONSTRUCCIÓN DE LA INTERFAZ ---
ventana = tk.Tk()
ventana.title("Simulador Completo de Hardware")
ventana.geometry("550x780")
ventana.resizable(False, False)

tk.Label(ventana, text="Validador Completo de PC", font=("Arial", 14, "bold")).pack(pady=10)

def crear_menu(texto, variable, diccionario):
    tk.Label(ventana, text=texto, font=("Arial", 10, "bold")).pack()
    variable.set(list(diccionario.keys())[0])
    menu = tk.OptionMenu(ventana, variable, *diccionario.keys())
    menu.config(width=45)
    menu.pack(pady=4)

combo_cpu = tk.StringVar(ventana)
crear_menu("1. Procesador (CPU):", combo_cpu, PROCESADORES)

combo_mobo = tk.StringVar(ventana)
crear_menu("2. Tarjeta Madre:", combo_mobo, TARJETAS_MADRES)

combo_ram = tk.StringVar(ventana)
crear_menu("3. Memoria RAM:", combo_ram, MEMORIAS_RAM)

combo_gpu = tk.StringVar(ventana)
crear_menu("4. Tarjeta Gráfica (GPU):", combo_gpu, TARJETAS_GRAFICAS)

combo_alma = tk.StringVar(ventana)
crear_menu("5. Almacenamiento Principal:", combo_alma, ALMACENAMIENTO)

combo_gabi = tk.StringVar(ventana)
crear_menu("6. Gabinete:", combo_gabi, GABINETES)

combo_fuente = tk.StringVar(ventana)
crear_menu("7. Fuente de Poder:", combo_fuente, FUENTES_PODER)

btn_validar = tk.Button(ventana, text="Verificar Compatibilidad Total", command=procesar_diagnostico, bg="#10b981", fg="white", font=("Arial", 11, "bold"))
btn_validar.pack(pady=15)

lbl_status = tk.Label(ventana, text="RESULTADO: Esperando componentes...", font=("Arial", 12, "bold"))
lbl_status.pack()

lbl_detalles = tk.Label(ventana, text="", font=("Arial", 10), justify="left")
lbl_detalles.pack(pady=10)

ventana.mainloop()