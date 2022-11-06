"""
Este módulo permite generar pipelines para un dataset cualquiera.
-- Activar o desactivar el PCA
-- Cambiar el número de componentes del PCA
-- Elegir las variables numéricas y categóricas que queremos usar
"""

import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.decomposition import PCA
from random import randint
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV


#def make_pipeline(use_pca=True, components=3, num_var=[], cat_var=[]):
def make_pipeline():
    """
    Generador de pipelines

    Args:
    -----
        use_pca ([boolean]): [description]
        components ([int]): [description]
        #num_var ([list]): [description]
        #cat_var ([list]): [description]

    Examples:
    ---------

    >>> from pipelinegenerator.generator import make_pipeline
    >>> pipelinegenerator.generator.make_pipeline(use_pca=True, components=3, num_var=["age"], cat_var=["sex"])
    1

    """

    #pipeline de variables numericas incluyendo PCA
    num_pipeline = Pipeline([("imputer", SimpleImputer()),
                             ("ss", StandardScaler()),
                             ("pca", PCA(n_components=2))
                            ])

    #Column transformer incluyendo las categoricas
    ct = ColumnTransformer([
        ("cat", OneHotEncoder(), ["pclass", "sex", "embarked"]),
        ("num", num_pipeline, ["age", "fare", "sibsp", "parch"])
    ])

    #pipeline final con modelo
    # faltaria quitar el modelo >repasar video
    pipeline = Pipeline([
        ("ct", ct),
        ("model", DecisionTreeClassifier())
    ])

    #valores para la METAESTIMACION
    #param_grid ={
    #    "ct__num__pca__n_components": [1,2,3,4],
    #    "model__max_depth": [2,3,4,5,6,7,8]
    #}


    #return list(df.select_dtypes(include=[np.number]).columns)
    return pipeline


def fit(generated_pipeline, X, y):
    """
    Entrenador del pipeline

    Args:
    -----
        pipeline ([boolean]): [description]
        X ([df]): [description]
        y ([df]): [description]

    Examples:
    ---------

    >>> from sklearn.datasets import fetch_openml
    >>> from sklearn.model_selection import train_test_split
    >>> from pipelinegenerator import make_pipeline, fit
    >>> X, y = fetch_openml("titanic", version=1, as_frame=True, return_X_y=True)
    >>> seed = 1234
    >>> X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=seed)
    >>> generated_pipeline = make_pipeline()
    >>> fit(generated_pipeline, X_train, y_train)
    1

    """
    generated_pipeline.fit(X, y)
    return generated_pipeline


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