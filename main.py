import speech_recognition as sr
import os
import webbrowser
import openai
import datetime
import random

chatStr=""

def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = apikey
    chatStr += f"sudhanshu: {prompt}\n Assistant"

    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      prompt=chatStr,
      temperature=1,
      max_tokens=256,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )

    print(response["choices"][0]["text"])
    say(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]

    if not os.path.exists("openai"):
        os.mkdir("Openai")

    with open(f"prompt-  {random.randint(1,362574369)}","w") as f:
        f.write(text)




def ai(prompt):
    openai.api_key = apikey
    text=f"Openai response for Prompt: {prompt} \n *************************\n"

    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      prompt="text-davinci-003",
      temperature=1,
      max_tokens=256,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )

    print(response["choices"][0]["text"])
    text+=response["choices"][0]["text"]
    if not os.path.exists("openai"):
        os.mkdir("Openai")

    with open(f"prompt-  {random.randint(1,362574369)}","w") as f:
        f.write(text)







def say(text):
    os.system(f"say {text}")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "some Error Occurred. Sorry from assistant"


if __name__ == '__main__':
    print('PyCharm')
    say("Hello i am your Desktop assistant")
    while True:
        print("Listening...")
        query = takeCommand()
        sites = [["youtube","https://www.youtube.com"],["wikipedia","https://www.wikipedia.com"],["google","https://www.google.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                webbrowser.open(site[1])
                say(f"Opening {site[0]} sir...")

            elif "open music" in query:
                musicPath = ""
                os.system(f"open {musicPath}")

            elif "the time" in query:
                strfTime = datetime.datetime.now().strftime("%H:%M:%S")
                say(f"sir the time is {strfTime}")

            elif "open facetime".lower() in query.lower():
                os.system(f"open /System/Applications/FaceTime.app")

            elif "openai".lower() in query.lower():
                ai(prompt=query)

            elif "please quit".lower() in query.lower():
                exit()

            elif "reset chat":
                chatStr = ""

            else:
                print("chatting...")
                chat(query)
        # say(query)

