import streamlit as st

# from langchain_openai import OpenAI
# from langchain_core.prompts import PromptTemplate
# import chromadb
# import openai
# from langchain_openai import OpenAIEmbeddings

# openai.api_key=OPENAI_API_KEY
# embedding_model = OpenAIEmbeddings(model="text-embedding-3-small",openai_api_key=openai.api_key)
# chroma_client = chromadb.Client()
# collection = chroma_client.get_collection(name='lecture_notes')
# def query_chroma(query):
#     query_embedding = embedding_model.embed_query(query)
#     results = collection.query(
#         query_embeddings=query_embedding,
#         n_results=5  # Adjust the number of results as needed
#     )

#     response_parts = []
#     for doc in results['documents'][0]:
#         # metadata = res['metadata']
#         # if metadata['type'] == 'text':
#         #     response_parts.append(metadata['sentence'])
#         # elif metadata['type'] == 'link':
#         #     response_parts.append(f"Link: {metadata['link']}")
#         # elif metadata['type'] == 'table':
#         #     response_parts.append(f"Table: {json.loads(metadata['table'])}")
#         # elif metadata['type'] == 'image':
#         #     response_parts.append(f"Image: {metadata['image']}")
#         response_parts.append(doc)

#     return " ".join(response_parts)

# prompt_template = PromptTemplate(
#     input_variables=["context", "question"],
#     template="Context: {context}\n\nQuestion: {question}\n\nAnswer:"
# )

# llm = OpenAI(temperature=0.7, model_name="gpt-3.5-turbo-instruct")

# def generate_response(context, question):
#     prompt = prompt_template.format(context=context, question=question)
#     response = llm(prompt)
#     return response


# def query_agent(query):
#     context = query_chroma(query)
#     response = generate_response(context, query)
#     return response

st.title("Interactive Query Bot")
st.write("Ask a question and get an answer based on the stored data.")

# Input field for the query
query = st.text_input("Enter your question:")

if st.button("Get Answer"):
    with st.spinner('Generating response...'):
        context, response = query_agent(query)
        st.success("Response generated!")
        
        # Display the context
        st.subheader("Context:")
        st.write(context)
        
        # Display the response
        st.subheader("Answer:")
        st.write(response)

# Add additional features or customization below
st.sidebar.title("About")
st.sidebar.info(
    """
    This app uses a combination of ChromaDB, Sentence Transformers, and OpenAI's GPT-3 to 
    generate answers based on stored data. Built with Streamlit for an interactive experience.
    """
)