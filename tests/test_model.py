from model import create_bayesian_network
from pgmpy.inference import VariableElimination


def test_model_inference_basic():
    m = create_bayesian_network()
    inf = VariableElimination(m)
    evidence = {'Fever': 1, 'Cough': 1, 'SoreThroat': 0, 'Sneezing': 0, 'LossOfSmell': 0}

    probs = {}
    for d in ['Flu', 'COVID', 'Allergy']:
        q = inf.query(variables=[d], evidence=evidence)
        probs[d] = float(q.values[1])

    # probabilities should be between 0 and 1
    for v in probs.values():
        assert 0.0 <= v <= 1.0

    # at least one disease should have non-zero probability
    assert any(v > 0.0 for v in probs.values())
