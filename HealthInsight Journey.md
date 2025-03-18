# The Journey of Building the HealthInsight Package

## Introduction
The *HealthInsight* package was conceived with the goal of analyzing health-related data using efficient Python computations. The project aimed to provide a well-structured package that could be published on PyPI and used by the broader Python community.

The journey followed a well-structured workflow, split into two major phases:

1. **Design Phase:**  
   - Defining the project’s purpose.  
   - Writing the core functionalities.  
   - Implementing unit tests.  
   - Refining and optimizing the code.  

2. **Build Phase:**  
   - Managing dependencies with Poetry.  
   - Running tests using pytest, tox, and coverage.  
   - Publishing to GitHub with documentation via MkDocs.  
   - Deploying to PyPI using Git and Poetry.  

---

## Phase 1: Conceptualization and Development

### 1. Structuring the Project
To align with best practices, the project followed a structured directory layout:

```
healthinsight_pkg/
│   ├── healthinsight/             # Core package directory
│   │   ├── __init__.py            # Makes the directory a package
│   │   ├── calculations.py        # Contains HealthCalc class
│   │   ├── analysis.py            # Other analytical functions
│   │
│   ├── tests/                     # Unit tests for validation
│   │   ├── test_calculations.py   
│   │   ├── test_analysis.py
│   │
│   ├── README.md                   # Project description
│   ├── pyproject.toml               # Poetry configuration
│   ├── poetry.lock                  # Dependencies
│   ├── dist/                         # Generated distribution files
│   ├── mkdocs.yml                    # Documentation settings
```

This structure ensured modularity, easy maintenance, and adherence to packaging best practices.

### 2. Implementing the Core Functionalities
The *HealthInsight* package contained key computational functionalities for analyzing health-related data. These were implemented in `calculations.py` and `analysis.py`.

Some key functions included:
- **`HealthCalc.calculate_bmi(weight, height)`** – Computes Body Mass Index (BMI).
- **`HealthCalc.heart_rate_analysis(age, resting_hr)`** – Analyzes heart rate ranges.
- **Additional helper functions** for various health metrics.

### 3. Writing Unit Tests
Unit tests were written using `pytest` inside the `tests/` directory. Each function had corresponding test cases to ensure correctness.

For example, in `test_calculations.py`:

```python
def test_calculate_bmi():
    assert HealthCalc.calculate_bmi(70, 1.75) == pytest.approx(22.86, 0.1)
```

Pytest was used to run tests:

```sh
poetry run pytest tests/
```

---

## Phase 2: Building and Deployment

### 1. Managing Dependencies with Poetry
Poetry was used to handle dependencies, packaging, and publishing.  
Key steps included:

- **Initializing the package:**
  ```sh
  poetry init
  ```
- **Adding dependencies:**
  ```sh
  poetry add numpy pandas
  ```
- **Checking package integrity:**
  ```sh
  poetry check
  ```

### 2. Publishing to GitHub with Documentation
After the core functionality was implemented, the project was uploaded to GitHub for version control and collaboration.

- **Creating the GitHub repository:**
  ```sh
  git init
  git remote add origin https://github.com/Femvrich001/healthInsight-pkg.git
  git add .
  git commit -m "Initial commit"
  git push -u origin main
  ```

- **Generating documentation using MkDocs:**
  ```sh
  mkdocs serve
  mkdocs gh-deploy
  ```

### 3. Deploying to PyPI
After testing, the package was built and published on PyPI.

- **Building the package:**
  ```sh
  poetry build
  ```
- **Uploading the package:**
  ```sh
  poetry publish --build
  ```

#### Handling Twine Upload Issues
If Poetry had issues uploading, Twine was used instead:

```sh
twine upload dist/*
```

---

## Challenges and Solutions
### 1. Poetry Configuration Issues
- Early issues with deprecated fields in `pyproject.toml` were fixed by updating them to the latest format.

### 2. GitHub Repository Mistakes
- Incorrect remote URLs were fixed using:
  ```sh
  git remote set-url origin <correct-repo-url>
  ```

### 3. Import Errors in Installed Package
- The `__init__.py` file was updated to expose the required functions properly.

### 4. Twine Authentication Issues
- The PyPI token was stored securely in `~/.pypirc` to resolve upload failures.

---

## Final Thoughts and Future Improvements
The development of *HealthInsight* was an insightful experience, combining Python best practices, documentation handling, and package deployment. Future improvements could include:

- **Expanding functionality** to support more health metrics.
- **Providing a command-line interface (CLI)** for ease of use.
- **Enhancing test coverage** for edge cases.

This structured approach will serve as a roadmap for future projects, ensuring efficiency and clarity in development.

