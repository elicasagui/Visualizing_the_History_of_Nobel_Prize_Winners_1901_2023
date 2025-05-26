<!DOCTYPE html>
<html lang="en">

<body>
  <h1>Nobel Prize Winners Data Analysis</h1>

  <h2>Project Overview</h2>
  <p>This project analyzes Nobel Prize laureates from 1901 to 2023. It includes data loading, cleaning, exploratory data analysis, and visualizations to uncover trends by gender, country, decade, and category.</p>

  <h2>Repository Structure</h2>
  <pre><code>
Nobel_Prize_Winners/
├── data/
│   ├── raw/           # Original data files (e.g., nobel.csv)
│   └── processed/     # Cleaned and transformed datasets
├── notebooks/         # Jupyter notebooks for EDA and prototyping
│   └── exploratory_analysis.ipynb
├── src/               # Python source code
│   ├── __init__.py    # Makes src a package
│   ├── load_data.py   # Functions to load and validate data
│   ├── clean_data.py  # Data cleaning and preprocessing
│   ├── analyze.py     # Statistical analysis functions
│   └── visualize.py   # Visualization functions (matplotlib, seaborn)
├── tests/             # Unit tests with pytest
│   ├── __init__.py
│   ├── test_load_data.py
│   ├── test_clean_data.py
│   ├── test_analyze.py
│   └── test_visualize.py
├── requirements.txt   # Project dependencies
├── .gitignore         # Files and directories to ignore
└── README.html        # Project documentation (this file)
  </code></pre>

  <h2>Installation</h2>
  <ol>
    <li>Clone the repository:<br>
      <pre><code>git clone https://github.com/elicasagui/Visualizing_the_History_of_Nobel_Prize_Winners_1901_2023.git
cd Visualizing_the_History_of_Nobel_Prize_Winners_1901_2023
      </code></pre>
    </li>
    <li>Create a virtual environment:<br>
      <pre><code>python -m venv venv
      </code></pre>
    </li>
    <li>Activate the virtual environment (PowerShell):<br>
      <pre><code>Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate  
<!-- This temporarily allows script execution and then activates the venv -->
      </code></pre>
    </li>
    <li>Install dependencies:<br>
      <pre><code>python -m pip install --upgrade pip
python -m pip install -r requirements.txt
      </code></pre>
    </li>
  </ol>

  <h2>Usage</h2>
  <ul>
    <li>Launch JupyterLab:<br>
      <pre><code>jupyter lab
      </code></pre>
      Or, if not recognized:<br>
      <pre><code>python -m jupyterlab
      </code></pre>
    </li>
    <li>Run tests:<br>
      <pre><code>python -m pytest
      </code></pre>
      Ensure all tests in the <code>tests/</code> directory pass.
    </li>
  </ul>

  <h2>Data Pipeline</h2>
  <p>The <code>src/</code> package contains modules for each stage of the data pipeline:</p>
  <ul>
    <li><code>load_data.py</code>: Load raw data from CSV and validate structure.</li>
    <li><code>clean_data.py</code>: Clean and standardize fields (e.g., dates, categories).</li>
    <li><code>analyze.py</code>: Perform statistical computations (e.g., modes, ratios).</li>
    <li><code>visualize.py</code>: Generate plots (line charts, bar charts) for trends.</li>
  </ul>

  <h2>Key Insights</h2>
  <ul>
    <li><strong>Most commonly awarded gender and birth country:</strong> Male and United States of America.</li>
    <li><strong>Decade with highest ratio of US-born laureates:</strong> 2000s (decade starting in 2000).</li>
    <li><strong>Highest proportion of female laureates by decade and category:</strong> 2020s in Literature.</li>
    <li><strong>First woman to receive a Nobel Prize:</strong> Marie Curie, née Sklodowska (Physics).</li>
    <li><strong>Individuals or organizations with multiple Nobel Prizes:</strong>
      <ul>
        <li>International Committee of the Red Cross</li>
        <li>Linus Carl Pauling</li>
        <li>John Bardeen</li>
        <li>Frederick Sanger</li>
        <li>Marie Curie, née Sklodowska</li>
        <li>Office of the United Nations High Commissioner for Refugees (UNHCR)</li>
      </ul>
    </li>
  </ul>

  <h2>📄 License</h2>
  <p>This project was developed during a DataCamp data science course.</p>

  <h2>📄 Created by</h2>
  <p>Eliecer Castro<br>
  Data Scientist</p>
</body>
</html>

