import speech_recognition as sr  # Importa la librería para reconocimiento de voz
import webbrowser  # Importa la librería para abrir URLs en el navegador
import pyttsx3  # Importa la librería para síntesis de voz


recognizer = sr.Recognizer()  # Crea un objeto Recognizer para el reconocimiento de voz
engine = pyttsx3.init()  # Inicializa el motor de síntesis de voz

def hablar():
    microfono = sr.Microphone()  # Crea un objeto Microphone
    with microfono as fuente:  # Usa el micrófono como fuente de audio
        print("Por favor, habla algo...")
        audio = recognizer.listen(fuente)  # Escucha el audio

    try:
        text = recognizer.recognize_google(audio, language='es-ES')  # Reconocer el audio usando Google Web Speech API
        print(f'Haz dicho: {text}')  # Imprime el texto reconocido
        return text.lower()  # Devuelve el texto en minúsculas
    
    except sr.UnknownValueError:
        print("No se pudo entender el audio")
        return ""  # Devuelve una cadena vacía si no se puede entender
    except sr.RequestError as e:
        print(f"No se pudo conectar al servicio de reconocimiento de voz; {e}")
        return ""  # Devuelve una cadena vacía en caso de error de conexión

# Llama a la función hablar() y verifica si la palabra "google" está en el texto
if 'google' in hablar():
    engine.say('¿Claro, Qué quieres buscar en Google?')  # Pregunta al usuario
    engine.runAndWait()  # Espera a que se complete la síntesis de voz
    search_text = hablar()  # Llama a hablar() nuevamente para obtener el texto de búsqueda
    if search_text:  # Asegúrate de que no sea una cadena vacía
        webbrowser.open(f'https://www.google.com/search?q={search_text}')  # Abre la búsqueda de Google con el texto
