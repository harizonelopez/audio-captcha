import random
from captcha.audio import AudioCaptcha

def generate_random_captcha(length=6):
    characters = '1234567890'
    captcha_text = ''.join(random.choice(characters, k=length))
    
    return captcha_text

audio = AudioCaptcha()
captcha_text = generate_random_captcha()

print(f"Generated CAPTCHA text:", captcha_text)
audio_captcha = audio.generate(captcha_text)
audio.write(captcha_text, 'Audio_Captcha.wav')

print(f"Audio CAPTCHA generated: Audio_Captcha.wav")


