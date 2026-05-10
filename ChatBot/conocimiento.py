# conocimiento.py - Base de conocimiento completa de nutrición

# ============================================
# 1. ALIMENTOS Y SUS PROPIEDADES NUTRICIONALES
# ============================================

alimentos = {
    # FRUTAS
    "manzana": {"calorias": 52, "proteinas": 0.3, "carbohidratos": 14, "grasas": 0.2, "fibra": 2.4, "beneficios": ["fibra", "vitamina C", "antioxidantes", "saciedad"]},
    "platano": {"calorias": 89, "proteinas": 1.1, "carbohidratos": 23, "grasas": 0.3, "fibra": 2.6, "beneficios": ["potasio", "energía rápida", "vitamina B6"]},
    "naranja": {"calorias": 47, "proteinas": 0.9, "carbohidratos": 12, "grasas": 0.1, "fibra": 2.4, "beneficios": ["vitamina C", "sistema inmune", "colágeno"]},
    "fresa": {"calorias": 32, "proteinas": 0.7, "carbohidratos": 7.7, "grasas": 0.3, "fibra": 2, "beneficios": ["vitamina C", "antioxidantes", "bajas calorías"]},
    "aguacate": {"calorias": 160, "proteinas": 2, "carbohidratos": 9, "grasas": 15, "fibra": 7, "beneficios": ["grasas saludables", "potasio", "vitamina E", "ácido oleico"]},
    
    # VERDURAS
    "brocoli": {"calorias": 34, "proteinas": 2.8, "carbohidratos": 7, "grasas": 0.4, "fibra": 2.6, "beneficios": ["vitamina C", "vitamina K", "fibra", "sulforafano"]},
    "espinaca": {"calorias": 23, "proteinas": 2.9, "carbohidratos": 3.6, "grasas": 0.4, "fibra": 2.2, "beneficios": ["hierro", "vitamina K", "magnesio", "folato"]},
    "zanahoria": {"calorias": 41, "proteinas": 0.9, "carbohidratos": 10, "grasas": 0.2, "fibra": 2.8, "beneficios": ["vitamina A", "betacaroteno", "visión", "piel"]},
    "tomate": {"calorias": 18, "proteinas": 0.9, "carbohidratos": 3.9, "grasas": 0.2, "fibra": 1.2, "beneficios": ["licopeno", "vitamina C", "antioxidantes"]},
    "lechuga": {"calorias": 15, "proteinas": 1.4, "carbohidratos": 2.9, "grasas": 0.2, "fibra": 1.3, "beneficios": ["hidratación", "vitamina K", "bajas calorías"]},
    
    # PROTEÍNAS
    "pollo_pechuga": {"calorias": 165, "proteinas": 31, "carbohidratos": 0, "grasas": 3.6, "fibra": 0, "beneficios": ["proteína magra", "vitamina B6", "fósforo", "bajo en grasas"]},
    "pollo_frito": {"calorias": 300, "proteinas": 25, "carbohidratos": 15, "grasas": 18, "fibra": 1, "beneficios": [], "nota": "Alto en grasas saturadas y calorías"},
    "pescado_blanco": {"calorias": 90, "proteinas": 19, "carbohidratos": 0, "grasas": 1.5, "fibra": 0, "beneficios": ["proteína magra", "fácil digestión"]},
    "salmon": {"calorias": 208, "proteinas": 20, "carbohidratos": 0, "grasas": 13, "fibra": 0, "beneficios": ["omega-3", "vitamina D", "selenio", "salud cerebral"]},
    "huevo": {"calorias": 155, "proteinas": 13, "carbohidratos": 1, "grasas": 11, "fibra": 0, "beneficios": ["proteína completa", "colina", "vitamina B12", "luteína"]},
    "lentejas": {"calorias": 116, "proteinas": 9, "carbohidratos": 20, "grasas": 0.4, "fibra": 8, "beneficios": ["proteína vegetal", "fibra", "hierro", "folato"]},
    "garbanzos": {"calorias": 139, "proteinas": 7.5, "carbohidratos": 23, "grasas": 2.4, "fibra": 7.6, "beneficios": ["proteína vegetal", "fibra", "hierro", "magnesio"]},
    
    # CEREALES Y TUBÉRCULOS
    "quinoa": {"calorias": 120, "proteinas": 4.4, "carbohidratos": 21, "grasas": 1.9, "fibra": 2.8, "beneficios": ["proteína completa", "fibra", "magnesio", "sin gluten"]},
    "arroz_blanco": {"calorias": 130, "proteinas": 2.7, "carbohidratos": 28, "grasas": 0.3, "fibra": 0.4, "beneficios": ["energía rápida", "fácil digestión"]},
    "arroz_integral": {"calorias": 111, "proteinas": 2.6, "carbohidratos": 23, "grasas": 0.9, "fibra": 1.8, "beneficios": ["fibra", "magnesio", "vitaminas B", "más saciedad"]},
    "papa": {"calorias": 77, "proteinas": 2, "carbohidratos": 17, "grasas": 0.1, "fibra": 2.2, "beneficios": ["potasio", "vitamina C", "energía"]},
    "papas_fritas": {"calorias": 312, "proteinas": 3.4, "carbohidratos": 41, "grasas": 15, "fibra": 3.8, "beneficios": [], "nota": "Evitar por exceso de grasas y sal"},
    "avena": {"calorias": 389, "proteinas": 16.9, "carbohidratos": 66, "grasas": 6.9, "fibra": 10.6, "beneficios": ["fibra soluble", "betaglucanos", "colesterol", "saciedad"]},
    
    # LÁCTEOS Y ALTERNATIVAS
    "yogur_griego": {"calorias": 59, "proteinas": 10, "carbohidratos": 3.6, "grasas": 0.4, "fibra": 0, "beneficios": ["proteína", "probióticos", "calcio"]},
    "queso_fresco": {"calorias": 98, "proteinas": 11, "carbohidratos": 3, "grasas": 5, "fibra": 0, "beneficios": ["calcio", "proteína", "versátil"]},
    
    # FRUTOS SECOS
    "nueces": {"calorias": 654, "proteinas": 15, "carbohidratos": 14, "grasas": 65, "fibra": 6.7, "beneficios": ["omega-3", "antioxidantes", "salud cerebral"]},
    "almendras": {"calorias": 579, "proteinas": 21, "carbohidratos": 22, "grasas": 49, "fibra": 12, "beneficios": ["vitamina E", "magnesio", "saciedad"]},
    
    # PLATOS COMPUESTOS
    "ensalada_rusa": {"calorias": 95, "proteinas": 2.5, "carbohidratos": 8, "grasas": 6, "fibra": 2, "beneficios": ["verduras", "fibra", "vitaminas"], "nota": "Moderar mayonesa"},
    "pizza_margarita": {"calorias": 270, "proteinas": 12, "carbohidratos": 33, "grasas": 10, "fibra": 2, "beneficios": [], "nota": "Consumir con moderación"},
    "hamburguesa": {"calorias": 300, "proteinas": 17, "carbohidratos": 30, "grasas": 13, "fibra": 2, "beneficios": [], "nota": "Versión casera más saludable"},
}

# ============================================
# 2. RECOMENDACIONES POR COMIDA
# ============================================

recomendaciones = {
    "desayuno": [
        "Avena con frutas y nueces 🥣",
        "Yogur griego con fresas y granola 🍓",
        "Tostada integral con aguacate y huevo 🥑🍳",
        "Smoothie verde (espinaca, plátano, leche vegetal) 🥤",
        "Pan integral con queso fresco y tomate 🍅"
    ],
    "almuerzo": [
        "Pechuga a la plancha con quinoa y brócoli 🍗",
        "Ensalada de salmón con aguacate y espinacas 🥗",
        "Lentejas guisadas con verduras 🥣",
        "Pescado blanco al horno con papas y verduras 🐟",
        "Wrap de pollo con vegetales y hummus 🌯"
    ],
    "cena": [
        "Crema de calabaza o zanahoria 🥣",
        "Tortilla de claras con espinacas 🍳",
        "Pescado blanco al vapor con brócoli 🐟",
        "Ensalada de tomate y aguacate 🥗",
        "Revuelto de champiñones y huevo 🍄"
    ],
    "snacks": [
        "Manzana con canela 🍎",
        "Puñado de nueces o almendras (30g) 🥜",
        "Palitos de zanahoria y pepino 🥕",
        "Yogur griego natural 🥄",
        "Plátano con mantequilla de maní 🍌",
        "Hummus con vegetales"
    ]
}

# ============================================
# 3. COMPARATIVAS SALUDABLES
# ============================================

comparativas = {
    "pollo frito vs ensalada rusa": {
        "ganador": "ensalada rusa",
        "razon": "La ensalada rusa tiene 3 veces menos calorías (95 vs 300 kcal), menos grasas saturadas y aporta vegetales. El pollo frito tiene grasas trans del empanizado y fritura.",
        "detalle_calorias": "Ensalada rusa: 95 kcal/100g | Pollo frito: 300 kcal/100g"
    },
    "arroz blanco vs arroz integral": {
        "ganador": "arroz integral",
        "razon": "El arroz integral conserva el salvado y germen, aportando 4 veces más fibra (1.8g vs 0.4g), más magnesio y vitaminas del grupo B. Tiene menor índice glucémico.",
        "detalle_calorias": "Arroz integral: 111 kcal/100g | Arroz blanco: 130 kcal/100g"
    },
    "pollo a la plancha vs pollo frito": {
        "ganador": "pollo a la plancha",
        "razon": "El pollo a la plancha tiene 165 kcal vs 300 kcal del frito. Además evita las grasas trans del empanizado y aceite de fritura. Usar especias para dar sabor.",
        "detalle_calorias": "A la plancha: 165 kcal | Frito: 300 kcal"
    },
    "salmon vs pescado blanco": {
        "ganador": "depende del objetivo",
        "razon": "Para omega-3 y salud cardiovascular el salmón es superior. Para dieta hipocalórica el pescado blanco tiene menos calorías (90 vs 208 kcal). Ambos son excelentes.",
        "detalle_calorias": "Salmón: 208 kcal | Pescado blanco: 90 kcal"
    },
    "azucar vs miel": {
        "ganador": "miel (con moderación)",
        "razon": "La miel tiene antioxidantes y propiedades antibacterianas, pero ambas son azúcares. La miel es ligeramente mejor pero igual hay que limitar su consumo.",
        "detalle_calorias": "Azúcar: 387 kcal/100g | Miel: 304 kcal/100g"
    },
    "coca cola vs agua": {
        "ganador": "agua",
        "razon": "El agua tiene 0 calorías y es esencial. La Coca-Cola tiene 42 kcal/100ml (una lata 330ml = 139 kcal) y azúcares añadidos sin valor nutricional.",
        "detalle_calorias": "Agua: 0 kcal | Coca-Cola: 139 kcal/lata"
    }
}

# ============================================
# 4. CONSEJOS GENERALES DE NUTRICIÓN
# ============================================

consejos = [
    "💧 Bebe 2-3 litros de agua al día. Mantenerse hidratado ayuda al metabolismo.",
    "🥬 Incluye vegetales en todas las comidas. Al menos 5 porciones al día.",
    "🍳 Prefiere cocciones saludables: horno, plancha, vapor o hervido sobre frituras.",
    "🚫 Reduce el azúcar añadido. La OMS recomienda máximo 25g (6 cucharaditas) al día.",
    "🍎 Come frutas enteras, no jugos. Conservas la fibra y reduces el azúcar libre.",
    "📅 Planifica tus comidas semanalmente. Evita decisiones impulsivas poco saludables.",
    "🥑 Incluye grasas saludables (aguacate, frutos secos, aceite de oliva).",
    "🍽️ Controla las porciones. Usa platos más pequeños si quieres reducir cantidad.",
    "🌙 No cenes tarde. Deja al menos 2 horas entre la cena y acostarte.",
    "🏃‍♂️ Combina buena alimentación con ejercicio físico regular (150 min/semana)."
]

# ============================================
# 5. FUNCIONES DE BÚSQUEDA
# ============================================

def buscar_alimento(nombre):
    """Busca un alimento por nombre (coincidencia parcial)"""
    nombre = nombre.lower().strip()
    for clave, info in alimentos.items():
        if clave in nombre or nombre in clave:
            return {clave: info}
    return None

def comparar_alimentos(alimento1, alimento2):
    """Compara dos alimentos y devuelve un texto formateado"""
    a1 = buscar_alimento(alimento1)
    a2 = buscar_alimento(alimento2)
    
    if not a1 or not a2:
        return None
    
    nombre1 = list(a1.keys())[0]
    nombre2 = list(a2.keys())[0]
    datos1 = a1[nombre1]
    datos2 = a2[nombre2]
    
    comparacion = f"""
📊 **Comparación nutricional**

| Nutriente | {nombre1} | {nombre2} |
|-----------|----------|----------|
| 🔥 Calorías | {datos1['calorias']} kcal | {datos2['calorias']} kcal |
| 🥩 Proteínas | {datos1['proteinas']} g | {datos2['proteinas']} g |
| 🍚 Carbohidratos | {datos1['carbohidratos']} g | {datos2['carbohidratos']} g |
| 🧈 Grasas | {datos1['grasas']} g | {datos2['grasas']} g |
| 🌾 Fibra | {datos1.get('fibra', 'N/D')} g | {datos2.get('fibra', 'N/D')} g |

✅ **Recomendación**: 
El {'primer' if datos1['calorias'] < datos2['calorias'] else 'segundo'} alimento es mejor en calorías.
"""
    return comparacion

def recomendar_por_tipo(tipo):
    """Devuelve recomendaciones según tipo (desayuno/almuerzo/cena/snacks)"""
    if tipo in recomendaciones:
        return recomendaciones[tipo]
    return None

def obtener_consejo_aleatorio():
    """Devuelve un consejo aleatorio"""
    import random
    return random.choice(consejos)

def buscar_por_beneficio(beneficio):
    """Busca alimentos que tengan un beneficio específico"""
    beneficio = beneficio.lower()
    resultados = []
    for nombre, info in alimentos.items():
        if beneficio in [b.lower() for b in info.get('beneficios', [])]:
            resultados.append(nombre)
    return resultados

def get_top_alimentos_por_nutriente(nutriente, top=5):
    """Devuelve los alimentos con más de un nutriente específico"""
    nutriente = nutriente.lower()
    if nutriente not in ['proteinas', 'fibra', 'calorias', 'grasas']:
        return []
    
    validos = [(nombre, info[nutriente]) for nombre, info in alimentos.items() 
               if nutriente in info and info[nutriente] > 0]
    validos.sort(key=lambda x: x[1], reverse=True)
    return validos[:top]

# ============================================
# 6. DATOS DE EJEMPLO PARA DEMOSTRACIÓN
# ============================================

print("📚 Módulo de conocimiento cargado:")
print(f"   - {len(alimentos)} alimentos registrados")
print(f"   - {len(comparativas)} comparativas disponibles")
print(f"   - {len(consejos)} consejos nutricionales")