import setuptools

setuptools.setup(
    name="ml_project",
    version="0.1.0",
    description="Homework 1 for MADE MLOps course",
    author="Parviz Karimov",
    license="",
    python_requires="<=3.9.12",
    packages=setuptools.find_packages(include=["ml_project"]),
    entry_points={
        "console_scripts": [
            "train_model=ml_project.models.train_model:train_model",
            "predict=ml_project.models.predict_model:predict",
            "make_dataset=ml_project.data.make_dataset:make_dataset",
            "generate_data=ml_project.tests.generate_fake_dataset:generate",
        ]
    },
    install_requires=[
        "matplotlib",
        "pandas",
        "numpy",
        "click",
        "Sphinx",
        "coverage",
        "awscli",
        "flake8",
        "python-dotenv>=0.5.1",
        "numpy",
        "pandas",
        "pandas-profiling",
        "pytz",
        "black",
        "pyyaml",
        "plotly",
        "scikit-learn",
        "hydra-core",
        "sdv",
    ],
)
