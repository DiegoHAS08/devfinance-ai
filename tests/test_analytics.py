from src.analytics import expenses_by_category
import pandas as pd

def test_expenses_by_category():
    data = {
        "category": ["Comida", "Comida", "Transporte"],
        "amount": [10, 20, 15]
    }

    df = pd.DataFrame(data)

    result = expenses_by_category(df)

    assert result["Comida"] == 30