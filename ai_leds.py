import google.generativeai as genai
import board
import neopixel
import time

# Initialize NeoPixel Jewel (7 LEDs, RGBW) on GPIO 18
led = neopixel.NeoPixel(board.D18, 7, pixel_order=neopixel.RGBW, auto_write=False)

# Configure Gemini API
# ⚠️ REPLACE THIS WITH YOUR NEW KEY FROM AISTUDIO.GOOGLE.COM
GENI_API_KEY = "AIzaSyAxlqIcpLf68Sw19HFG1h3noliJr0KTs-4" 
genai.configure(api_key=GENI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

def ask_ai(symptom):
    try:
        response = model.generate_content(
            f"""A postpartum mother reports: '{symptom}'
            Reply with ONE word only: CRITICAL, WARNING, or NORMAL"""
        )
        # Clean up any accidental markdown, spaces, or punctuation from the model
        return response.text.strip().upper().replace("*", "")
    except Exception as e:
        print(f"API Error: {e}")
        return "NORMAL" # Safe fallback if API fails or times out

def flash_red():
    print("🚨 Triggering Critical Flash!")
    for _ in range(5):
        led.fill((255, 0, 0, 0)) # Red
        led.show()
        time.sleep(0.3)
        led.fill((0, 0, 0, 0))   # Off
        led.show()
        time.sleep(0.3)

def light_up(severity):
    # Using 'in' handles cases where the model accidentally returns punctuation or short phrases
    if "CRITICAL" in severity:
        flash_red()
    elif "WARNING" in severity:
        print("🟠 Triggering Warning Light (Orange)")
        led.fill((255, 165, 0, 0)) # Orange
        led.show()
    else:
        print("... Triggering Normal Light (Green)")
        led.fill((0, 255, 0, 0))   # Green
        led.show()
        time.sleep(3)
        led.fill((0, 0, 0, 0))     # Turn off after 3 seconds
        led.show()

# Main Loop
while True:
    symptom = input("\nDescribe symptom: ")
    if not symptom.strip():
        continue
        
    print("Asking Gemini...")
    severity = ask_ai(symptom)
    print(f"Gemini raw evaluation: {severity}")
    
    light_up(severity)