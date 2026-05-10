# chatbot.py - Modelo que responde preguntas usando prompt engineering + conocimiento recopilado

import requests
import json
import random
from conocimiento import (
    alimentos, recomendaciones, comparativas, consejos,
    buscar_alimento, comparar_alimentos, recomendar_por_tipo,
    buscar_por_beneficio, get_top_alimentos_por_nutriente
)

class ChatbotNutricion:
    """
    Modelo de chatbot especializado en nutrición.
    Usa prompt engineering para inyectar conocimiento recopilado.
    """
    
    def __init__(self):
        self.url = "http://localhost:11434/api/generate"
        self.modelo = "deepseek-r1:7b"
        self.historial = []
    
    def detectar_intencion(self, pregunta):
        """
        Detecta qué tipo de pregunta es y recupera conocimiento relevante.
        Esto es KEY para el prompt engineering.
        """
        pregunta_lower = pregunta.lower()
        contexto = ""
        
        # === 1. PREGUNTAS DE COMPARv-ACIÓN ===
        if "compar" in pregunta_lower or "vs" in pregunta_lower or "mejor" in pregunta_lower or "diferencia" in pregunta_lower:
            for key, info in comparativas.items():
                if any(p in pregunta_lower for p in key.split(" vs ")):
                    contexto = f"""
📚 CONOCIMIENTO RECOPILADO - COMPARATIVA:
{key}
Ganador: {info['ganador']}
Razón: {info['razon']}
Datos: {info.get('detalle_calorias', '')}
"""
                    break
            if not contexto:
                contexto = "📚 Puedo comparar alimentos como pollo frito vs ensalada rusa, arroz blanco vs integral, etc."
        
        # === 2. PREGUNTAS DE CALORÍAS ===
        elif "calor" in pregunta_lower or "energía" in pregunta_lower:
            # Buscar el alimento mencionado
            for alimento, info in alimentos.items():
                if alimento in pregunta_lower:
                    contexto = f"""
📚 CONOCIMIENTO RECOPILADO - {alimento}:
- Calorías: {info['calorias']} kcal por 100g
- Proteínas: {info['proteinas']}g
- Grasas: {info['grasas']}g
- Carbohidratos: {info['carbohidratos']}g
- Fibra: {info.get('fibra', 'N/D')}g
- Beneficios: {', '.join(info.get('beneficios', ['No especificados']))}
"""
                    break
        
        # === 3. PREGUNTAS DE RECOMENDACIONES ===
        elif "desayuno" in pregunta_lower:
            contexto = f"📚 RECOMENDACIONES RECOPILADAS PARA DESAYUNO: {', '.join(recomendaciones['desayuno'])}"
        elif "almuerzo" in pregunta_lower or "comida" in pregunta_lower:
            contexto = f"📚 RECOMENDACIONES RECOPILADAS PARA ALMUERZO: {', '.join(recomendaciones['almuerzo'])}"
        elif "cena" in pregunta_lower:
            contexto = f"📚 RECOMENDACIONES RECOPILADAS PARA CENA: {', '.join(recomendaciones['cena'])}"
        elif "snack" in pregunta_lower or "colación" in pregunta_lower or "entre comida" in pregunta_lower:
            contexto = f"📚 RECOMENDACIONES RECOPILADAS PARA SNACKS: {', '.join(recomendaciones['snacks'])}"
        
        # === 4. PREGUNTAS DE BENEFICIOS ===
        elif "beneficio" in pregunta_lower or "para qué sirve" in pregunta_lower or "propiedades" in pregunta_lower:
            for alimento, info in alimentos.items():
                if alimento in pregunta_lower:
                    contexto = f"""
📚 CONOCIMIENTO RECOPILADO - BENEFICIOS DE {alimento}:
{', '.join(info.get('beneficios', ['No hay beneficios registrados']))}
"""
                    break
        
        # === 5. PREGUNTAS DE CONSEJOS GENERALES ===
        elif "consejo" in pregunta_lower or "recomendación" in pregunta_lower:
            consejo_aleatorio = random.choice(consejos)
            contexto = f"📚 CONSEJO RECOPILADO: {consejo_aleatorio}"
        
        # === 6. PREGUNTAS SOBRE ALIMENTOS ESPECÍFICOS ===
        else:
            for alimento in alimentos.keys():
                if alimento in pregunta_lower:
                    info = alimentos[alimento]
                    contexto = f"""
📚 CONOCIMIENTO RECOPILADO - {alimento}:
Calorías: {info['calorias']} kcal/100g
Beneficios: {', '.join(info.get('beneficios', ['Ninguno registrado']))}
Nota: {info.get('nota', 'Alimento saludable con moderación')}
"""
                    break
        
        return contexto
    
    def generar_prompt(self, pregunta):
        """
        Construye el prompt con prompt engineering avanzado.
        Esta es la parte clave del requisito.
        """
        
        # Detectar intención y obtener conocimiento
        conocimiento_contexto = self.detectar_intencion(pregunta)
        
        # Construir el prompt completo con estructura de ingeniería
        prompt = f"""【INSTRUCCIÓN DEL SISTEMA】
Eres NutriBot, un nutricionista experto certificado. Tu misión es educar sobre alimentación saludable.

【CONOCIMIENTO RECOPILADO (USAR ESTOS DATOS)】
{conocimiento_contexto if conocimiento_contexto else "Usa tu conocimiento general sobre nutrición."}

【REGLAS DE RESPUESTA】
1. SIEMPRE basa tu respuesta en los datos proporcionados arriba
2. Si el conocimiento recopilado no cubre la pregunta, usa tu entrenamiento general
3. Sé breve: máximo 4 líneas para preguntas simples
4. Usa emojis para hacerla amigable (🥗 🍎 🥑)
5. Advierte si algo no es saludable sin alarmar

【PREGUNTA DEL USUARIO】
{pregunta}

【RESPUESTA DE NUTRIBOT】
"""
        return prompt
    
    def preguntar(self, pregunta):
        """
        Método principal: responde preguntas usando el LLM + conocimiento recopilado.
        Este es el corazón del modelo.
        """
        
        # Paso 1: Generar prompt con engineering y conocimiento
        prompt = self.generar_prompt(pregunta)
        
        # Paso 2: Enviar al LLM local (DeepSeek)
        data = {
            "model": self.modelo,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": 0.7,
                "num_predict": 400,
                "stop": ["【", "Usuario:"]
            }
        }
        
        try:
            response = requests.post(self.url, json=data, timeout=180)
            respuesta = response.json()["response"]
            
            # Guardar en historial
            self.historial.append({
                "pregunta": pregunta,
                "respuesta": respuesta,
                "conocimiento_usado": self.detectar_intencion(pregunta)[:100]
            })
            
            return respuesta
            
        except Exception as e:
            return f"❌ Error: {str(e)[:100]}\n\n¿Verifica que Ollama está corriendo?"
    
    def mostrar_estadisticas(self):
        """Muestra estadísticas del uso del conocimiento - para verificar el cumplimiento"""
        print("\n📊 ESTADÍSTICAS DEL MODELO:")
        print(f"  - Consultas realizadas: {len(self.historial)}")
        print(f"  - Alimentos en conocimiento: {len(alimentos)}")
        print(f"  - Comparativas disponibles: {len(comparativas)}")
        print(f"  - Recomendaciones: {sum(len(v) for v in recomendaciones.values())}")


# ============================================
# PRUEBA DEL MODELO (ejecutar directamente)
# ============================================

if __name__ == "__main__":
    print("="*60)
    print("🍏 NUTRIBOT - Chatbot Nutricional")
    print("="*60)
    print("✅ Modelo cargado con conocimiento recopilado")
    print(f"   - {len(alimentos)} alimentos en base de datos")
    print(f"   - {len(comparativas)} comparativas disponibles")
    print("="*60)
    
    bot = ChatbotNutricion()
    
    preguntas_prueba = [
        "Compara pollo frito vs ensalada rusa",
        "¿Cuántas calorías tiene una manzana?",
        "Dame consejos para comer saludable",
        "¿Qué desayuno me recomiendas?"
    ]
    
    for p in preguntas_prueba:
        print(f"\n🧑 Pregunta: {p}")
        print(f"🥗 Respuesta: {bot.preguntar(p)}")
        print("-"*40)
    
    bot.mostrar_estadisticas()