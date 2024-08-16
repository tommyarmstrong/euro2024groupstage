# EURO 2024 Group Stage Results Combiner

This Python project combines all the group stage results for the EURO 2024 tournament held in France into a single combined table formatted in HTML using jQuery DataTables.

## Features

- **Combine Results:** Automatically aggregates results from all group stage matches.
- **HTML Table:** Outputs the results in an HTML table format.
- **jQuery DataTables Integration:** Enhances the table with sorting, searching, and pagination using the jQuery DataTables library.

## Prerequisites

- Python 3.x
- `pandas` library
- Basic knowledge of HTML and JavaScript for jQuery DataTables integration

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/euro2024-results-combiner.git
    cd euro2024-results-combiner
    ```

2. **Install the required Python libraries:**

    ```bash
    pip install pandas
    pip install lxml
    ```

    or deploy from the `requirements.txt` file 

    ```bash
    pip3 install -r requirements.txt
    ```

## Usage 

Execute the python script `combine_groups.py`

  ```bash
  python combine_groups.py
  ```

This will create an HTML file in the same directory called `combined_groups.html` which contains group stage results for the EURO 2024 tournament combined into a single table. 

## Contributing

1. Fork the repository.
2. Create a new branch for your feature (git checkout -b feature-branch).
3. Commit your changes (git commit -am 'Add new feature').
4. Push to the branch (git push origin feature-branch).
5. Open a Pull Request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

##Acknowledgments
- jQuery DataTables for providing an easy-to-use table plugin.
- The Python pandas library for handling data manipulation.
- BBC website for providing the group data: www.bbc.co.uk/sport/football/european-championship/table
