import networkx as nx
import matplotlib.pyplot as plt
from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD


def create_bayesian_network():
    # Create a Bayesian Network structure
    model = BayesianNetwork([
        ('Flu', 'Fever'), ('Flu', 'Cough'), ('Flu', 'SoreThroat'),
        ('COVID', 'Fever'), ('COVID', 'Cough'), ('COVID', 'LossOfSmell'),
        ('Allergy', 'Sneezing'), ('Allergy', 'SoreThroat')
    ])

    # Prior probabilities for diseases
    cpd_flu = TabularCPD(variable='Flu', variable_card=2, values=[[0.95], [0.05]])
    cpd_covid = TabularCPD(variable='COVID', variable_card=2, values=[[0.97], [0.03]])
    cpd_allergy = TabularCPD(variable='Allergy', variable_card=2, values=[[0.85], [0.15]])

    # Conditional probabilities for symptoms
    cpd_fever = TabularCPD(
        variable='Fever', variable_card=2,
        values=[[0.95, 0.4, 0.8, 0.2], [0.05, 0.6, 0.2, 0.8]],
        evidence=['Flu', 'COVID'], evidence_card=[2, 2]
    )

    cpd_cough = TabularCPD(
        variable='Cough', variable_card=2,
        values=[[0.9, 0.3, 0.7, 0.1], [0.1, 0.7, 0.3, 0.9]],
        evidence=['Flu', 'COVID'], evidence_card=[2, 2]
    )

    cpd_sore_throat = TabularCPD(
        variable='SoreThroat', variable_card=2,
        values=[[0.9, 0.2, 0.8, 0.1], [0.1, 0.8, 0.2, 0.9]],
        evidence=['Flu', 'Allergy'], evidence_card=[2, 2]
    )

    cpd_loss_of_smell = TabularCPD(
        variable='LossOfSmell', variable_card=2,
        values=[[0.95, 0.2], [0.05, 0.8]],
        evidence=['COVID'], evidence_card=[2]
    )

    cpd_sneezing = TabularCPD(
        variable='Sneezing', variable_card=2,
        values=[[0.9, 0.1], [0.1, 0.9]],
        evidence=['Allergy'], evidence_card=[2]
    )

    # Add CPDs to the model
    model.add_cpds(cpd_flu, cpd_covid, cpd_allergy, cpd_fever, cpd_cough,
                  cpd_sore_throat, cpd_loss_of_smell, cpd_sneezing)

    return model


def visualize_network(model):
    # Create a directed graph
    G = nx.DiGraph()
    G.add_edges_from(model.edges())

    # Draw the network
    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(G)
    
    # Draw nodes
    nx.draw_networkx_nodes(G, pos, node_color='lightblue', 
                          node_size=2000, alpha=0.7)
    nx.draw_networkx_nodes(G, pos, 
                          nodelist=['Flu', 'COVID', 'Allergy'],
                          node_color='lightgreen',
                          node_size=2000, alpha=0.7)
    
    # Draw edges
    nx.draw_networkx_edges(G, pos, arrows=True)
    
    # Add labels
    nx.draw_networkx_labels(G, pos)
    
    plt.title("Medical Diagnosis Bayesian Network")
    plt.axis('off')
    plt.savefig('sample_output.png')
    plt.close()
