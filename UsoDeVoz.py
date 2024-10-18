import speech_recognition as sr  # Importa la librería SpeechRecognition con el alias 'sr'

# Crear un objeto de reconocimiento
recognizer = sr.Recognizer()  # Crea una instancia del objeto Recognizer


# Usar el micrófono como fuente de audio
with sr.Microphone() as source:  # Abre el micrófono como fuente de audio
    print("Por favor, dime algo para escribir a texto:")  # Informa al usuario que hable
    
    # Ajustar el ruido de fondo
    recognizer.adjust_for_ambient_noise(source, duration=1)  # Ajusta el ruido ambiental durante 1 segundo
    
    # Escuchar el audio
    audio = recognizer.listen(source)  # Captura el audio del micrófono y lo almacena en 'audio'

    try:
        # Usar Google Web Speech API para reconocer el audio
        text = recognizer.recognize_google(audio, language='es-ES')  # Convierte el audio en texto en español
        print("Usted dijo: " + text)  # Muestra en pantalla el texto reconocido
    
    except sr.UnknownValueError:
        print("No se pudo entender el audio")  # Manejo de error si no se entiende el audio
    
    except sr.RequestError as e:
        print(f"No se pudo conectar al servicio de reconocimiento de voz; {e}")  # Manejo de error si hay problemas de conexión
    
    except Exception as e:
        print(f"Ocurrió un error: {e}")  # Manejo de otros errores no previstos
