## O Desafio

#### Desafio disponibilizado no blog [sejaumdatascientist](https://sejaumdatascientist.com/)
#### Link [DESAFIO](https://sejaumdatascientist.com/como-usar-data-science-para-fazer-a-empresa-vender-mais/)

Nesse contexto, você foi contratado como um consultor de Ciência de Dados para construir um modelo que prediz se o cliente estaria ou não interessado no seguro de automóvel. 

Com a sua solução, o time de vendas espera conseguir priorizar as pessoas com maior interesse no novo produto e assim, otimizar a campanha realizando apenas contatos aos clientes mais propensos a realizar a compra.

Como resultado da sua consultoria, você precisará entregar um relatório contendo algumas análises e respostas às seguintes perguntas:

Principais Insights sobre os atributos mais relevantes de clientes interessados em adquirir um seguro de automóvel.
Qual a porcentagem de clientes interessados em adquirir um seguro de automóvel, o time de vendas conseguirá contatar fazendo 20.000 ligações?
E se a capacidade do time de vendas aumentar para 40.000 ligações, qual a porcentagem de clientes interessados em adquirir um seguro de automóvel o time de vendas conseguirá contatar?
Quantas ligações o time de vendas precisa fazer para contatar 80% dos clientes interessados em adquirir um seguro de automóvel?
Os Dados
O conjunto de dados está disponível na plataforma do Kaggle, através desse link: https://www.kaggle.com/anmolkumar/health-insurance-cross-sell-prediction 

Cada linha representa um cliente e cada coluna contém alguns atributos que descrevem esse cliente, além da sua resposta à pesquisa, na qual ela mencionou interesse ou não ao novo produto de seguros. 

**O conjunto de dados inclui as seguintes informações:**

- **Id**: identificador único do cliente.
- **Gender**: gênero do cliente.
- **Age**: idade do cliente.
- **Driving License**: 0, o cliente não tem permissão para dirigir e 1, o cliente tem para dirigir ( CNH – Carteira Nacional de Habilitação )
- **Region Code**: código da região do cliente.
- **Previously Insured**: 0, o cliente não tem seguro de automóvel e 1, o cliente já tem seguro de automóvel.
- **Vehicle Age**: idade do veículo.
- **Vehicle Damage**: 0, cliente nunca teve seu veículo danificado no passado e 1, cliente já teve seu veículo danificado no passado.
- **Anual Premium**: quantidade que o cliente pagou à empresa pelo seguro de saúde anual.
- **Policy sales channel**: código anônimo para o canal de contato com o cliente.
- **Vintage**: número de dias que o cliente se associou à empresa através da compra do seguro de saúde.
- **Response**: 0, o cliente não tem interesse e 1, o cliente tem interesse.



<br>

**Estruturação do projeto**

```
├── LICENÇA
├── Makefile <- Makefile com comandos como `make data` ou` make train`
├── README.md <- O README de nível superior para desenvolvedores que usam este projeto.
├── data
│ ├── external  <- Dados de fontes de terceiros.
│ ├── interim  <- Dados intermediários que foram transformados.
│ ├── processed  <- Os conjuntos de dados canônicos finais para modelagem.
│ └── raw <- O despejo de dados original e imutável.
│
├── docs <- Um projeto Sphinx padrão; veja sphinx-doc.org para detalhes
│
├── models  <- modelos treinados e serializados, previsões de modelos ou resumos de modelos
│
├── cadernos <- Cadernos Jupyter. A convenção de nomenclatura é um número (para pedido),
│ as iniciais do criador e uma breve descrição delimitada por `-`, por exemplo,
│ `1.0-jqp-initial-data-explo- ration`.
│
├── references  <- Dicionários de dados, manuais e todos os outros materiais explicativos.
│
├── reports  <- Análise gerada como HTML, PDF, LaTeX, etc.
│ └── figures  <- Gráficos e figuras gerados para serem usados ​​em relatórios
│
├── requirements.txt <- O arquivo de requisitos para reproduzir o ambiente de análise, por exemplo,
│ gerado com `pip freeze> requirements.txt`
│
├── setup.py <- Torne este projeto pip instalável com `pip install -e`
├── src <- Código-fonte para uso neste projeto.
│ ├── __init__.py <- Torna src um módulo Python
│ │
│ ├── data <- Scripts para baixar ou gerar dados
│ │ └── make_dataset.py
│ │
│ ├── features <- Scripts para transformar dados brutos em recursos para modelagem
│ │ └── build_features.py
│ │
│ ├── models  <- Scripts para treinar modelos e, em seguida, usar modelos treinados para fazer
│ │ │ predictions
│ │ ├── predict_model.py
│ │ └── train_model.py
│ │
│ └── visualization <- Scripts para criar visualizações exploratórias e orientadas a resultados
│ └── visualize.py
│
└── tox.ini <- arquivo tox com configurações para executar tox; veja tox.readthedocs.io
```