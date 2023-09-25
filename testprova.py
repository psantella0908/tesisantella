import openai
openai.api_key = "sk-*************************************Nt"
input_text = "start"
system_message = """."""


def ask_gpt(messages):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.2,
        max_tokens=2000
    )
    return completion.choices[0].message["content"]


print("Questo è un bot progettato per assistere gli studenti affetti da DSA. Per terminare inserire 'END'.")
history = []
messages = [{"role": "system", "content": system_message}]
while input_text != "END":
    input_text = input("Inserisci la domanda: ")
    if input_text == "END":
        print("Conversazione terminata. \n")
        break
    messages.append({"role": "user", "content": input_text})
    history.append("Utente: " + input_text)
    response = ask_gpt(messages)
    messages.append({"role": "assistant", "content": response})
    history.append("Assistente: " + response)
    print("\nAssistente : ", response)
    print("\n")

print("Ecco il riassunto della conversazione: ")
for s in history:
    print(s)
    print("\n")
