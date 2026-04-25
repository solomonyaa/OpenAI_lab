from openai import OpenAI

# Initialize the client
# client = OpenAI(api_key="your_api_key_here")
client = OpenAI()

# A single interaction (The "Stateless" way)
response = client.chat.completions.create(
    model="gpt-4o",  # or "gpt-3.5-turbo"
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Please explain how a quantum computer works."}
    ],
    # SECURITY TIP: 
    # Setting store to False (if available in your tier) tells OpenAI 
    # not to persist this specific message in their 'History' dashboard.
    store=False, 
    temperature=0.3
)

# Printing the result
print(response.choices[0].message.content)

