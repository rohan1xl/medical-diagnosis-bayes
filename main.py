import argparse
from pgmpy.inference import VariableElimination
from model import create_bayesian_network, visualize_network

def get_user_symptoms():
    print("\nPlease answer the following questions about your symptoms (yes/no):")
    symptoms = {}
    questions = {
        'Fever': 'Do you have fever?',
        'Cough': 'Do you have cough?',
        'SoreThroat': 'Do you have sore throat?',
        'Sneezing': 'Are you experiencing sneezing?',
        'LossOfSmell': 'Have you lost your sense of smell?'
    }
    
    for symptom, question in questions.items():
        while True:
            answer = input(f"{question} (yes/no): ").lower()
            if answer in ['yes', 'no']:
                symptoms[symptom] = 1 if answer == 'yes' else 0
                break
            print("Please answer with 'yes' or 'no'")
    
    return symptoms

def main():
    # Create and visualize the Bayesian network
    print("Initializing Medical Diagnosis System...")
    model = create_bayesian_network()
    visualize_network(model)
    
    # Get symptoms from user
    symptoms = get_user_symptoms()
    
    # Perform inference
    inference = VariableElimination(model)
    
    # Calculate probabilities for each disease
    diseases = ['Flu', 'COVID', 'Allergy']
    probabilities = {}
    
    for disease in diseases:
        result = inference.query(variables=[disease], evidence=symptoms)
        probabilities[disease] = result.values[1] * 100  # Probability of having the disease
    
    # Print results
    print("\nPredicted Disease Probabilities:")
    for disease, prob in probabilities.items():
        print(f"{disease}: {prob:.1f}%")
    
    # Find most probable disease
    most_probable = max(probabilities.items(), key=lambda x: x[1])
    print(f"\n>> Most Probable Disease: {most_probable[0]} ({most_probable[1]:.1f}%)")
    
    print("\nNote: A visualization of the Bayesian network has been saved as 'sample_output.png'")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Medical Diagnosis System')
    parser.add_argument('--gui', action='store_true', help='Launch the Tkinter GUI')
    args = parser.parse_args()

    if args.gui:
        # import gui lazily to avoid circular imports
        try:
            import gui
        except Exception as e:
            print('Failed to import GUI module:', e)
        else:
            gui.run_gui()
    else:
        main()
