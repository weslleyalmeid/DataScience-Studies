Programação Linear (LP):
- Não possuí variáveis inteiras, apenas contínuas
- Não existe operações não lineares na função objetivo e restrições


Primeiro exemplo:

max x + y

-x + 2y <= 8
2x + y <= 14
2x - y <= 10
0 <= x <= 10
0 <= y <= 10

Instação do Gurobi

sudo mv ~/Downloads/gurobi9.5.1_linux64.tar.gz /opt
cd /opt
sudo tar -xzf gurobi9.5.1_linux64.tar.gz

export GUROBI_HOME=/opt/gurobi951/linux64
export PATH=$GUROBI_HOME/bin:$PATH
export LD_LIBRARY_PATH=$GUROBI_HOME/lib:$LD_LIBRARY_PATH
grbgetkey key
gurobi_cl $GUROBI_HOME/examples/data/afiro.mps

Instalação Pyomo

sudo apt install libglpk-dev libgmp3-dev
sudo apt-get install glpk-utils libglpk-dev
pip install glpk

Instação do CBC
sudo apt install coinor-cbc


Lembre-se CBC, Guropi e GLPK são utilizados para programação linear


Instalação do CPLEX
export PYTHONPATH="${PYTHONPATH}:/opt/ibm/ILOG/CPLEX_Studio201/cplex/bin/x86-64_linux/cplex"
export PYTHONPATH="${PYTHONPATH}:/opt/ibm/ILOG/CPLEX_Studio201/cplex"


Docker Coinor

```bash
# baixando e inicializando imagem
docker pull coinor/coin-or-optimization-suite
docker create --name=coin-or -it coinor/coin-or-optimization-suite

# iniciando container
docker start coin-or

# copiando arquivo SRC_PATH:NAME_FILE to DEST_PATH:NAME_FILE
docker container cp ./01_pyomo_ex.py 6ee23ede17ef:/tmp/counne.py

# é necessário instalar python, pip e vim
# executar script python
# docker container exec -it id_container [COMMAND]
docker container exec -it 6ee2 python3 /tmp/counne.py
```