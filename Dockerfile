FROM centos:7.2.1511

RUN yum install -y \
     vim\
     python-pip\
     wget

RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/anaconda.sh && \
    /bin/bash ~/anaconda.sh -b -p /opt/conda && \
    rm ~/anaconda.sh && \
    echo "export PATH=/opt/conda/bin:$PATH" >> ~/.bashrc

ENV PATH /opt/conda/bin:$PATH

COPY . /app
WORKDIR /app

# Create the environment:
RUN conda env create -f environment.yml

# Make RUN commands use the new environment:
SHELL ["conda", "run", "-n", "kddcup", "/bin/bash", "-c"]

ENTRYPOINT ["python", "local_test.py"]

