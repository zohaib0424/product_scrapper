from deep_translator import GoogleTranslator


def translate(input: str) -> str:
    """
    Translate the input text to English.
    """
    try:
        translator = GoogleTranslator(source='auto', target='en')
        chunks = [input[i:i+100] for i in range(0, len(input), 100)]
        translated_chunks = [translator.translate(chunk) for chunk in chunks]
        return ' '.join(translated_chunks)
    except Exception as e:
        print(f"Translation error: {e}")
        return input
