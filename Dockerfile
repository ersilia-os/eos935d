FROM bentoml/model-server:0.11.0-py38
MAINTAINER ersilia

RUN pip install rdkit-pypi==2022.3.1b1
RUN pip install future==1.0.0
RUN pip install six==1.17.0
RUN pip install tqdm==4.64.1
RUN pip install pandas==1.3.5
RUN pip install torch==1.4.0
RUN pip install torchtext==0.3.1
RUN pip install ipython==8.12.3
RUN pip install comet_ml==3.49.8
RUN pip install git+https://github.com/KavrakiLab/MetaTrans.git


WORKDIR /repo
COPY . /repo
