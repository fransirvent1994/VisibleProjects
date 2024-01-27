import datetime
import pyttsx3
import speech_recognition as sr
import pyjokes
import pywhatkit
import webbrowser
import wikipedia
import yfinance as yf
import math

#  Language config
engine = pyttsx3.init()

# Voices database(There´s just two, Spanish, as it is my mother tongue, and English, which is the language we work in this code
# but it´s possible to get more voices databases. These are the ones I have by default.)

# Spanish.
id1 = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0"
# English
id2 = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"


# Micro listening and get audio converted into a text
def audio_into_text():
    # Var to storage the recognizer
    r = sr.Recognizer()

    # Micro configuration
    with sr.Microphone() as origen:

        # Waiting time
        r.pause_threshold = 0.6  # Waiting time value

        # Recording can begin
        print("Say something")

        # Var to storage the audio
        audio = r.listen(origen)

        try:
            # Search in google
            petition = r.recognize_google(audio, language="en-US")

            # The audio was recogniced
            print("Said: " + petition)

            # Go back to petition
            return petition

        # In case of error
        except sr.UnknownValueError:
            # Audio not recogniced
            print("Sorry, an error ocurred, repeat again please")

            # Go back to error
            return "Still waiting"

        # In case petition not resolved
        except sr.RequestError:
            # Audio not recogniced
            print("Server not responding")

            # Go back to error
            return "Still waiting"

        # Error unexpected
        except:
            # Go back to error
            print("Something went wrong")

            # Go back to error
            return "Still waiting"


# Writing into audio transforming

# Speaking assistant function
def speak(message):
    # Turn on Pyttsx3 engine
    engine = pyttsx3.init()
    engine.setProperty("voice", id2)  # Var to choose the voice selected

    # Pronounce message
    engine.say(message)

    engine.runAndWait()

# Initial salute
def initial_salute():
    # Var with the salute depending on which hour it is
    hour = datetime.datetime.now()
    if hour.hour < 6 or hour.hour > 20:  # Before 6 a.m. and after 8 p.m.
        day_moment = "Good night"
    elif 6 <= hour.hour < 13:  # 6 a.m. or after and before than 1 p.m.
        day_moment = "Good morning"
    else:
        day_moment = "Good afternoon"  # For the rest of hours

    # say salute
    speak(f"{day_moment}. I´m your voice assistant")

initial_salute()

# This is a test. I wanted to hear how the voice says the initial salute, dates and hours. Just for fun.
def day_asking():
    # Var for actual day
    day = datetime.date.today()
    print(day)

    # Var for day of the week
    week_day = day.weekday()

    # dict for day names
    calendar = {0: "Monday",
                1: "Tuesday",
                2: "Wednesday",
                3: "Thursday",
                4: "Friday",
                5: "Saturday",
                6: "Sunday"}

    # Say day of the week
    day_name = calendar[week_day] # This line is a var to read the actual day name
    print(f"It's {day_name}") # Prints the name of the actual day
    speak(f"It´s {calendar[week_day]}") #It says the day

day_asking()

# Hour function
def hour_asking():
    hour = datetime.datetime.now()
    hour = f"Right now it´s {hour.hour}:{hour.minute}:{hour.second}"
    print(hour)

    # Say hour
    speak(hour)

hour_asking()

speak("What can I do for you?")

def calculate_math(expression):
    try:
        result = eval(expression, {"__builtins__": None}, {"math": math})
        return f"The result of {expression} is {result}"
    except Exception as e:
        return f"Error to calculate: {str(e)}"

# Petitions

def petitions():
    # Activate initial salute

    # Loop to begin the voice commands without stopping
    begin = True  # It´s on

    while begin:
        # Micro activate and save petition in a string
        petition = audio_into_text().lower()

        if "open youtube" in petition:  # Opens the main page of YouTube
            speak("Opening youtube")
            webbrowser.open("https://www.youtube.com")
            continue

        elif "open browser" in petition:  # Opens the browser. Google Chrome chosen in this case.
            speak("Opening browser")
            webbrowser.open("https://www.google.com")
            continue

        elif "what day is today" in petition:  # Says the actual day
            day_asking()
            continue

        elif "what time is it" in petition:  # Says the actual hour
            hour_asking()
            continue

        elif "calculate" in petition: # Calculates math operationes
            expression = petition.replace("calculate", "") # Say "calculate" and the nums with the operation
            result = calculate_math(expression)
            print(result) # Print the result in screen
            speak(result)
            continue

        elif "need some holidays" in petition:  # Opens a travels web
            speak("Opening vueling")
            webbrowser.open("https://www.vueling.com")
            continue

        elif "i want to change my job" in petition:  # Opens a holiday´s web
            speak("Opening LinkedIn")
            webbrowser.open("https://www.linkedin.com")
            continue

        elif "search in wikipedia" in petition:  # Searches in Wikipedia with the petition aske
            speak("searching in wikipedia")
            petition = petition.replace("Search in wikipedia", "")
            wikipedia.set_lang("en")  # Search in English
            result = wikipedia.summary(petition, sentences=1)  # To obtain just one result
            speak("Wikipedia says: ")
            speak(result)
            continue

        elif "search in the internet" in petition:  # Searches in Internet with the petition asked
            speak("Diving in the Net")
            petition = petition.replace("search in Internet", "")
            pywhatkit.search(petition)  # Search in internet
            print(f"This is what I found: {pywhatkit.search(petition)}")
            speak("This is what I found: ")
            continue

        elif "like to go out" in petition:
            speak("I would invite you to a beer, but I have no money")
            continue

        elif "play" in petition:  # Opens YouTube with the petition asked after "play" said
            speak("Let´s do it!")
            pywhatkit.playonyt(petition)  # playonyt is a library that works with YouTube
            continue

        elif "tell me a joke" in petition:  # Just for jokes
            speak(pyjokes.get_joke("en"))
            continue

        elif "stock market value" in petition:  # To see the stock market value of the enterprises below
            action = petition.split("of")[-1].strip()
            wallet = {"apple": "AAPL",
                      "amazon": "AMZN",
                      "google": "GOOGL"}
            try:
                stock_market_looked_for = wallet.get(action.lower())
                if stock_market_looked_for:
                    stock_market_looked_for = yf.Ticker(stock_market_looked_for)
                    actual_price = stock_market_looked_for.info["regularMarketPrice"]
                    speak(f"This is what I found:\nThe price of {action} is {actual_price}")
                else:
                    speak("Company not found in the wallet.")
            except Exception as e:
                speak(f"An error occurred: {str(e)}")

        elif "goodbye" in petition:
            speak("See you soon, I´ll be here whenever you need me")
            break


petitions()

"""This is a loop to see the available voices in the system
for voice in engine.getProperty("voices"):
    print(voice)"""
