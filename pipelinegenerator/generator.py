"""
Este módulo permite generar pipelines para un dataset cualquiera.
-- Activar o desactivar el PCA
-- Cambiar el número de componentes del PCA
-- Elegir las variables numéricas y categóricas que queremos usar
"""

import pickle
import numpy as np
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.decomposition import PCA


def make_pipeline(use_pca: bool =False, components: int =0, num_var: list=[], cat_var: list=[]):
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
    >>> import numpy as np
    >>> from pipelinegenerator.generator import make_pipeline, fit, export_pipeline
    >>> from sklearn.datasets import fetch_openml
    >>> from sklearn.model_selection import train_test_split
    >>> from sklearn.tree import DecisionTreeClassifier
    >>> # Crear el pipeline
    >>> generated_pipeline = make_pipeline(use_pca=True, components=3, num_var=["age", "fare", "sibsp", "parch"], cat_var=["pclass", "sex", "embarked"])
    >>> # carga del dataset
    >>> X, y = fetch_openml("titanic", version=1, as_frame=True, return_X_y=True)
    >>> # division train_test
    >>> X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)
    >>> # Entrenamiento 
    >>> generated_pipeline = fit(generated_pipeline, X_train, y_train)
    >>> generated_pipeline.fit_transform(X_test.head(3))
    array([[0., 0., 1., 1., 1.],
       [1., 0., 0., 1., 1.],
       [0., 1., 0., 1., 1.]])

    """

    if use_pca:
        num_pipeline = Pipeline([
            ("imputer", SimpleImputer()),
            ("ss", StandardScaler()),
            ("pca", PCA(n_components=components))
        ])
    else:
        num_pipeline = Pipeline([
            ("imputer", SimpleImputer()),
            ("ss", StandardScaler())
        ])

    ct = ColumnTransformer([
        ("cat", OneHotEncoder(), cat_var),
        ("num", num_pipeline, num_var)
    ])

    pipeline = Pipeline([
        ("ct", ct)
    ])

    return pipeline


def fit(pipeline: Pipeline, X, y):
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
    pipeline = pipeline.fit(X, y)
    return pipeline


def export_pipeline(pipeline: Pipeline, file: str):
    """
    Export to a pickle file.

    Args:
    -----
        pipeline ([boolean]): [description]
        file ([str]): [description]

    Examples:
    ---------

    >>> from pipelinegenerator.export import export_pipeline
    >>> export_pipeline()
    1

    """
    with open(file, "wb") as f:
        pickle.dump(pipeline, f)