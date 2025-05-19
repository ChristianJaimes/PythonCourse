#faq_bot.py
def responder_pregunta(pregunta):
    pregunta = pregunta.lower()
    respuestas = {
        "envío": "El envío tarda entre 3 y 5 días hábiles.",
        "devolución": "Puedes devolver productos en un plazo de 30 días.",
        "pago": "Aceptamos tarjetas de crédito, débito y PayPal.",
        "precio": "Los precios están sujetos a cambios según promociones.",
        "stock": "Si el producto aparece en la lista, está disponible.",
    }
    for clave in respuestas:
        if clave in pregunta:
            return respuestas[clave]
    return "Lo siento, no tengo una respuesta para esa pregunta. Por favor contáctanos directamente."