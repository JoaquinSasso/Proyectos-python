def transform_text(text):
    # Convertir todo el texto a minúsculas
    text = text.lower()
    
    # Dividir el texto en párrafos
    paragraphs = text.split('\n')
    
    # Capitalizar la primera letra de cada párrafo
    for i in range(len(paragraphs)):
        if paragraphs[i]:  # Verificar si el párrafo no está vacío
            paragraphs[i] = paragraphs[i][0].upper() + paragraphs[i][1:]
    
    # Unir los párrafos nuevamente en un solo texto
    transformed_text = '\n'.join(paragraphs)
    
    return transformed_text

# Texto de ejemplo en mayúsculas
texto_mayusculas = """
Modelo BQ-CC51AR
PUEDE CARGAR HASTA 4 PILAS AA O 4 PILAS AAA NI-MH.
CONTROL AUTOMATICO DE SEGURIDAD PARA CORTAR LA CARGA.
VOLTAJE MUNDIAL (CA110V/240V).
TIEMPO DE CARGA (10HS)
"""

# Transformar el texto
texto_transformado = transform_text(texto_mayusculas)

print(texto_transformado)
