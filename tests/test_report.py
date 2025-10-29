import os
from gui import generate_medical_report, generate_pdf_report


def test_generate_report_txt_and_pdf(tmp_path):
    evidence = {'Fever':1,'Cough':0,'SoreThroat':0,'Sneezing':1,'LossOfSmell':0}
    probs = {'Flu':0.05,'COVID':0.01,'Allergy':0.94}

    txt_file = tmp_path / 'report.txt'
    pdf_file = tmp_path / 'report.pdf'

    report_text = generate_medical_report(evidence, probs, filename=str(txt_file))
    assert os.path.exists(str(txt_file))
    assert 'Medical Diagnosis Report' in report_text

    generate_pdf_report(report_text, str(pdf_file))
    assert os.path.exists(str(pdf_file))
