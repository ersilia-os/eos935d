FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

RUN conda install rdkit -c rdkit
RUN conda install future six tqdm pandas
RUN conda install pytorch=1.1.0 torchvision -c pytorch
RUN pip install torchtext==0.3.1

WORKDIR /repo
COPY . /repo
