def load_texts():
    salary_text = """
    Salaries are usually structured monthly or annually.
    Monthly salary is the amount you receive each month.
    Annual salary is monthly salary multiplied by 12.
    Deductions such as taxes, provident fund, and insurance reduce take-home pay.
    """

    insurance_text = """
    Insurance benefits cover health, life, and accidental claims.
    Premium is the amount paid periodically to maintain coverage.
    Claims are made by submitting required documents to the insurance provider.
    Coverage includes hospitalization, surgeries, and medications depending on policy.
    """

    texts = [salary_text, insurance_text]
    metadatas = [{"topic": "salary"}, {"topic": "insurance"}]

    return texts, metadatas




