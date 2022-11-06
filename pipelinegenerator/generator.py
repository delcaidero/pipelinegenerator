"""
Este módulo permite generar pipelines para un dataset cualquiera.
-- Activar o desactivar el PCA
-- Cambiar el número de componentes del PCA
-- Elegir las variables numéricas y categóricas que queremos usar
"""

#import numpy as np

def make_pipeline(use_pca=True, components=3, num_var=[], cat_var=[]):
    """
    Generador de pipelines

    Args:
    -----
        use_pca ([boolean]): [description]
        components ([int]): [description]
        num_var ([list]): [description]
        cat_var ([list]): [description]

    Examples:
    ---------

    >>> from pipelinegenerator.generator import make_pipeline
    >>> #import pandas as pd
    >>> #df = pd.DataFrame({'a':[1]})
    >>> make_pipeline(use_pca=True, components=3, num_var=["age"], cat_var=["sex"])
    1



    """
    #return list(df.select_dtypes(include=[np.number]).columns)
    return 0


def fit(pipeline, X, y):
    """
    Entrenador del pipeline

    Args:
    -----
        pipeline ([boolean]): [description]
        X ([df]): [description]
        y ([df]): [description]

    Examples:
    ---------

    >>> from pipelinegenerator.fit import fit
    >>> fit()
    1

    """
    return 0


    def export(pipeline, file):
        """
    Export to a pickle file.

    Args:
    -----
        pipeline ([boolean]): [description]
        file ([str]): [description]

    Examples:
    ---------

    >>> from pipelinegenerator.export import export
    >>> export()
    1

    """
    return 0