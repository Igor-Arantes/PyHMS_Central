# PyHMS_Central


## Introdução:
Há uma equipe na Petrobras Petroleo Brasileiro responsável por monitorar a aquisição de dados metereologicos, 
oceanográficos e movimentação de unidade matirimas, portos e aeroportos. Atualmente é necessário acessar remotamente 
equipamento por equipamento. Este acesso demora em média 8 min por equipamento. Com este painel é estimado uma economia de tempo de 
**3h e 20min**  da equipe por dia, totalizando **100h mensalmente**



## Objetivo:
Disponibilizar um painel de fácil visualização todas as unidades coletoras de dados(UDC), 
maritimas ou não que tenham o software PyHMS em operação, se os sensores estão comunicando 
corretamente para que os dados sejam coletados com sucesso.

## Funcionamento:
Com base em um arquivo json, com as informações necessárias das UCDs alvos, é montado uma lista de endereços de
APIs correspondentes para consumo, com as respostas da consulta as APIs é montado uma tabela e destacado com cores
Vermelho para quando há uma falha de comunicação com o sensor, Verde 
quando há uma medição correta e  Amarelo quando não foi possível se conectar à UCD.

## Imagens

### Painel Principal
![Painel Principal](https://github.com/Igor-Arantes/PyHMS_Central/blob/main/Pagina_Principal.JPG)
### Painel de configuração
![Painel de Configuração](https://github.com/Igor-Arantes/PyHMS_Central/blob/main/Pagina%20de%20Configura%C3%A7%C3%A3o.JPG)
## Bibliotecas Utilizadas

[Pandas 1.1.5](https://pandas.pydata.org/docs/reference/index.html)  

[Streamlit 0.84](https://docs.streamlit.io/en/stable/api.html)


## Melhorias Futuras:

- Habilitar Multithreading para consulta as APIs
- Se comunicar com o Dadas para incluir as demais UCDs
- Ao se comunicar com o Dadas inserir todos os sensores possíveis
- Comunicação com o BD de produção para identificar parametros que estão reprovados ou que haja teste condicional
------------------
