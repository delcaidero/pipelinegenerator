
'''
Ejemplo

def test_get_numerical_features_simple():
    """En este vamos a probar que logra distiguir
    entre cadenas de texto y numeros enteros"""

    df = pd.DataFrame({
        "numerica": [5],
        "categorica":["rojo"]
    })
    
    assert get_numerical_features(df) == ["numerica"]

'''
from pipelinegenerator.generator import make_pipeline

def test_make_pipeline_without_args():
    """En este vamos a probar que no funciona sin argumentos"""
    assert make_pipeline() == 0