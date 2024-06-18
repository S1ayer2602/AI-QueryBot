# AI-QueryBot

AI-QueryBot is an interactive query agent that leverages ChromaDB, Sentence Transformers, and OpenAI's GPT-3 to generate answers based on stored data. Built with Streamlit for an engaging user experience, it allows users to ask questions and receive contextually relevant answers.

## Features

- Extracts and processes text, links, tables, and images from web pages.
- Stores data in ChromaDB for efficient querying.
- Generates embeddings using Sentence Transformers.
- Utilizes OpenAI's GPT-3 for generating answers.
- Interactive web interface built with Streamlit.

## Setup

### Prerequisites

- Python 3.7 or higher
- OpenAI API key
- Required Python packages

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/S1ayer2602/AI-QueryBot.git
    cd AI-QueryBot
    ```

2. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up your OpenAI API key:

    Replace `'your-openai-api-key'` with your actual OpenAI API key in `app.py`.

### Usage

1. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

2. Open your browser and navigate to the provided URL to interact with AI-QueryBot.

## How It Works

1. **Data Extraction**: Scrape text, links, tables, and images from web pages using Beautiful Soup.
2. **Embedding Generation**: Generate embeddings for the extracted data using Sentence Transformers.
3. **Data Storage**: Store the data and embeddings in ChromaDB.
4. **Query Processing**: Use LangChain to query ChromaDB and generate responses with OpenAI's GPT-3.
5. **Interactive Interface**: Streamlit provides a user-friendly interface for asking questions and displaying answers.

## Example

1. Enter a question in the input field.
2. Click "Get Answer".
3. The app will display the context and generate a relevant answer based on the stored data.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an issue to discuss any changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## About

QueryBot AI was created to demonstrate the integration of advanced AI technologies for interactive data querying and response generation. It combines the power of ChromaDB, Sentence Transformers, and OpenAI's GPT-3, all wrapped in a user-friendly Streamlit interface.


