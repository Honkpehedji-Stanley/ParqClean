import pandas as pd
from parqclean.validate import check_required_columns

def test_missing_columns():
    df = pd.DataFrame({"a":[1,2]})
    try:
        check_required_columns(df, {"a":"int","b":"str"})
        assert False, "Should have raised"
    except ValueError:
        assert True
