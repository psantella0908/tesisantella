import openai
openai.api_key = "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"
system_message= """Sei un assistente per uno studente italiano che frequenta le scuole medie superiori. 
Lo studente ha problemi nel leggere e scrivere per periodi prolungati perché è affetto da Disturbo Specifico dell’Apprendimento. 
Lo studente vorebbe che tenessi conto del suo Disturbo Specifico dell’Apprendimento. Lo studente vorrebbe che lo correggessi quando 
sbaglia a fare lo spelling di parole. Lo studente vorebbe che lo aiutassi a creare un testo senza errori ortografici."""
completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": system_message},
        {"role": "user", "content": "come potresti aiutare uno studente delle scuole medie con DSA?"},
        # {"role": "assistant", "content": "Hi, I am your assistant"}
    ],
    temperature=0.2,
    max_tokens=200
)


print(completion.choices[0].message["content"])
with open("prova.txt", "w") as textprova:
    textprova.write(completion.choices[0].message["content"])
textprova.close()
