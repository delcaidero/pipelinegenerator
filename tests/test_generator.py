from pipelinegenerator.generator import make_pipeline, fit, export_pipeline


def test_make_pipeline_simple():
    """En este vamos a probar que no funciona sin argumentos"""
    assert make_pipeline() == 0


def test_fit_simple():
    """En este vamos a probar que no funciona sin argumentos"""
    assert fit() == 0


def test_export_pipeline_simple():
    """En este vamos a probar que no funciona sin argumentos"""
    assert export_pipeline() == 0
