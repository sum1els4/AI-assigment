# Text Summarization Application

This project is a text summarization application that provides functionalities to summarize text from PDF or TXT files. It utilizes various Natural Language Processing (NLP) techniques to preprocess the text, apply summarization methods, and evaluate the performance of these methods.

## Project Structure

The project is organized as follows:
```
text-summarization-app
├── src
│   ├── app.py                     # Main entry point of the application
│   ├── utils
│   │   ├── data_preprocessing.py   # Functions for text data preprocessing
│   │   ├── summarization_methods.py # Implementation of summarization techniques
│   │   └── evaluation_metrics.py    # Functions to evaluate summarization performance
│   ├── models
│   │   ├── extractive_model.py      # Extractive summarization model
│   │   └── abstractive_model.py     # Abstractive summarization model
│   └── crawlers
│       └── web_crawler.py          # Web crawler for gathering sample data
├── data
│   ├── raw
│   │   └── sample_data.txt         # Raw text data for testing
│   └── processed
│       └── cleaned_data.txt        # Cleaned and preprocessed text data
├── notebooks
│   ├── exploratory_data_analysis.ipynb # Jupyter notebook for exploratory data analysis
│   └── model_comparison.ipynb      # Jupyter notebook for model performance comparison
├── requirements.txt                 # List of dependencies
├── README.md                        # Project documentation
└── .gitignore                       # Files and directories to ignore in version control
```

## Features

- **Text Preprocessing**: Clean and prepare text data for summarization.
- **Summarization Methods**: Implement both extractive and abstractive summarization techniques.
- **Evaluation Metrics**: Evaluate summarization performance using metrics like ROUGE and BLEU scores.
- **Web Crawling**: Gather sample data from specified forums or social media platforms.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/text-summarization-app.git
   cd text-summarization-app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Set the Python path to include the `src` directory:
   ```bash
   export PYTHONPATH=$(pwd)/src  # On Windows: set PYTHONPATH=%cd%\src

2. Upload a PDF or TXT file for summarization through the application interface.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.