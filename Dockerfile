FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

RUN conda install -c conda-forge rdkit==2021.03.4
RUN conda install future==0.18.2
RUN conda install six==1.16.0
RUN conda install tqdm==4.64.1
RUN conda install pandas==1.3.5
RUN conda install pytorch==1.1.0 torchvision -c pytorch
RUN pip install torchtext==0.3.1
RUN pip install ipython
RUN pip install "git+https://github.com/KavrakiLab/MetaTrans.git"

WORKDIR /repo
COPY . /repo
