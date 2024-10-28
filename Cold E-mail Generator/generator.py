from langchain_groq import ChatGroq

groq_api_key = "your own api key"
print(groq_api_key)
llm = ChatGroq(
    model="llama-3.1-70b-versatile",
    temperature=0,
    groq_api_key=groq_api_key
    # other params...
)

response=llm.invoke("first person to step on moon")
print(response)
