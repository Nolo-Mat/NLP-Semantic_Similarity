# Movie Recommendation System

This is a simple movie recommendation system that suggests the next movie to watch based on the similarity of movie descriptions. The system uses spaCy with the 'en_core_web_md' language model to calculate the similarity between the input description and each movie description.

## Installation

1. Clone the repository:

   git clone <[repository_url](https://github.com/Nolo-Mat/NLP-Semantic_Similarity)>

2. Install the required dependencies. It is recommended to use a virtual environment:

   python -m venv venv
   source venv/bin/activate  # For Unix/Linux
   venv\Scripts\activate.bat  # For Windows
   pip install -r requirements.txt

3. Download the 'en_core_web_md' language model for spaCy:

    python -m spacy download en_core_web_md

## Usage

1. Open the movies.txt file and add movie descriptions in the following format:

   Movie A: When Hiccup discovers Toothless isn't the only Night Fury, he must seek "The Hidden World", a secret Dragon Utopia before a hired tyrant named Grimmel finds it first.
   Movie B: After the death of Superman, several new people present themselves as possible successors.
   ...

2. Run the watch_next.py script:

    python watch_next.py

3. Enter the description of the movie you have watched when prompted.

4. The system will suggest the title of the most similar movie based on the input description.

## Contributing

Contributions are welcome! If you find any issues or want to enhance the movie recommendation system, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License.

