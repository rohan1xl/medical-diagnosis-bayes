# Medical Diagnosis System using Bayesian Network

This project implements a medical diagnosis system using Bayesian Networks to predict the probability of different diseases (Flu, COVID, and Allergy) based on observed symptoms.

## Features

- Predicts probabilities for Flu, COVID, and Allergy
- Takes user input for symptoms (Fever, Cough, Sore Throat, Sneezing, Loss of Smell)
- Visualizes the Bayesian Network structure
- Provides probability-based diagnosis

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/medical-diagnosis-bayes.git
cd medical-diagnosis-bayes
```

2. Create and activate a virtual environment (optional but recommended):
```bash
python -m venv .venv
.venv\Scripts\activate  # On Windows
source .venv/bin/activate  # On Unix/macOS
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the program:
```bash
python main.py
```

2. Follow the prompts to input your symptoms (answer yes/no to each question)

3. View the results showing probability for each disease

4. Check the generated `sample_output.png` to see the Bayesian Network visualization

### GUI (Tkinter)

There's a simple Tkinter GUI if you prefer a windowed interface instead of the command line.

1. Run the GUI:

```bash
python gui.py
```

2. The window shows symptom checkboxes. Check the symptoms you have and click "Diagnose".

3. Results will appear in the right-hand panel and a popup shows the most probable disease. The Bayesian network image `sample_output.png` is also shown in the window and can be refreshed with the "Refresh Network Image" button.

Notes:
- The GUI reuses the same Bayesian network model defined in `main.py` so the results match the CLI.
- `tkinter` is included with standard Python on Windows. Pillow is used to display the generated PNG (`sample_output.png`).

## Sample Output

```
Initializing Medical Diagnosis System...

Please answer the following questions about your symptoms (yes/no):
Do you have fever? (yes/no): yes
Do you have cough? (yes/no): yes
Do you have sore throat? (yes/no): no
Are you experiencing sneezing? (yes/no): no
Have you lost your sense of smell? (yes/no): yes

Predicted Disease Probabilities:
Flu: 25.3%
COVID: 70.1%
Allergy: 4.6%

>> Most Probable Disease: COVID (70.1%)

Note: A visualization of the Bayesian network has been saved as 'sample_output.png'
```

## Project Structure

```
medical-diagnosis-bayes/
├── main.py              # Main program file
├── requirements.txt     # Python dependencies
├── README.md           # This file
└── sample_output.png   # Generated Bayesian network visualization
```

## How It Works

The system uses a Bayesian Network to model the relationships between diseases and symptoms. The network structure and conditional probabilities are defined based on medical knowledge. When symptoms are input, the system uses Bayesian inference to calculate the probability of each disease.

## Author
ROHAN KUMAR

## License

This project is open source and available under the MIT License.
