FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

RUN pip install rdkit-pypi==2021.3.4
RUN pip install future==0.18.2
RUN pip install six==1.16.0
RUN pip install tqdm==4.64.1
RUN pip install pandas==1.3.5
RUN pip install torch==1.1.0 torchvision
RUN pip install torchtext==0.3.1
RUN pip install ipython
RUN pip install comet_ml
RUN pip install git+https://github.com/KavrakiLab/MetaTrans.git@30d88639da9e0b9e8db9b7686ca19f2d24261c34

WORKDIR /repo
COPY . /repo
