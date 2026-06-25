from setuptools import setup, find_packages

setup(
    name="WKRadarM1",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.0",
    ],
    author="WK Radar Integration Team",
    description="Biblioteca para integração com a API do WK Radar (Módulo 1)",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    keywords="wk radar api erp integration",
    python_requires=">=3.7",
)
