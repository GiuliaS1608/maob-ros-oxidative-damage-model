# Modelagem Matemática da Produção de Espécies Reativas de Oxigênio (ROS) Mediada pela MAO-B e Dano Oxidativo

**Idioma:** [English](README.md) | Português

Modelo matemático dinâmico e semiquantitativo, baseado em equações diferenciais ordinárias (EDOs), para investigar a produção de espécies reativas de oxigênio (ROS) mediada pela monoamina oxidase B (MAO-B) e sua relação com o dano oxidativo.

O modelo representa a cascata temporal que conecta o metabolismo da dopamina, a formação de peróxido de hidrogênio ($\mathrm{H_2O_2}$), a formação de ROS e o dano oxidativo. Seu objetivo principal é explorar alterações relativas no comportamento do sistema diante de diferentes perturbações paramétricas, em vez de predizer concentrações intracelulares absolutas.

## Visão geral

O estresse oxidativo resulta de um desequilíbrio entre a produção de espécies reativas de oxigênio e a capacidade celular de neutralizá-las. Neste modelo, o metabolismo da dopamina mediado pela MAO-B é representado como uma fonte inicial de $\mathrm{H_2O_2}$, que posteriormente está relacionado à formação de ROS e ao dano oxidativo.

O modelo foi desenvolvido para investigar como alterações em:

- atividade efetiva da MAO-B;
- disponibilidade de dopamina;
- capacidade antioxidante; e
- reparo/remoção do dano celular

modificam a dinâmica temporal da cascata oxidativa.

## Modelo matemático

A etapa enzimática inicial é descrita pela cinética de Michaelis-Menten:

$$
V(S)=\frac{V_{\max}^{*}S}{K_m+S}
$$

O modelo dinâmico completo é dado por:

$$
\frac{dS}{dt} = P-\frac{V_{\max}^{*}S}{K_m+S}-K_sS,
$$

$$
\frac{dH}{dt} = \alpha\frac{V_{\max}^{*}S}{K_m+S}-K_hH,
$$

$$
\frac{dR}{dt} = \beta H-K_rR,
$$

$$
\frac{dD}{dt} = \gamma R-K_dD.
$$

A cascata representada pelo modelo pode ser resumida como:

**Dopamina $S(t)$ $\to$ metabolismo mediado pela MAO-B $\to$ $\mathrm{H_2O_2}$ $H(t)$ $\to$ ROS $R(t)$ $\to$ Dano oxidativo $D(t)$**

A MAO-B não é modelada como uma variável de estado independente. Sua atividade efetiva é representada pelo termo de Michaelis-Menten que contém $V_{\max}^{*}$ e $K_m$.

## Variáveis do modelo

| Variável | Descrição | Unidade |
|---|---|---|
| $S(t)$ | Concentração de dopamina | $\mu\mathrm{M}$ |
| $H(t)$ | Nível normalizado de $\mathrm{H_2O_2}$ | unidades arbitrárias |
| $R(t)$ | Nível normalizado de ROS | unidades arbitrárias |
| $D(t)$ | Nível de dano oxidativo | unidades arbitrárias |

Como $H(t)$, $R(t)$ e $D(t)$ são expressos como índices relativos, o modelo é **semiquantitativo**. Essas variáveis não devem ser interpretadas como concentrações intracelulares absolutas.

## Parâmetros basais

| Parâmetro | Valor | Unidade | Interpretação |
|---|---:|---|---|
| $K_m$ | 229 | $\mu\mathrm{M}$ | Constante de Michaelis-Menten |
| $V_{\max}^{*}$ | 100 | $\mu\mathrm{M}\,\mathrm{min}^{-1}$ | Velocidade máxima efetiva da reação |
| $P$ | 50 | $\mu\mathrm{M}\,\mathrm{min}^{-1}$ | Produção basal de dopamina |
| $K_s$ | 0.7 | $\mathrm{min}^{-1}$ | Remoção fisiológica adicional de dopamina |
| $\alpha$ | 1.0 | — | Fator efetivo de formação/conversão de $\mathrm{H_2O_2}$ |
| $K_h$ | 0.5 | $\mathrm{min}^{-1}$ | Remoção de $\mathrm{H_2O_2}$ |
| $\beta$ | 0.8 | $\mathrm{min}^{-1}$ | Taxa efetiva de formação de ROS |
| $K_r$ | 0.7 | $\mathrm{min}^{-1}$ | Neutralização de ROS |
| $\gamma$ | 0.6 | — | Fator efetivo de formação/conversão do dano oxidativo |
| $K_d$ | 0.9 | $\mathrm{min}^{-1}$ | Reparo/remoção do dano |

Os parâmetros $\alpha$ e $\gamma$ são tratados como fatores efetivos de conversão entre variáveis representadas em diferentes escalas. Como $H(t)$, $R(t)$ e $D(t)$ são variáveis semiquantitativas expressas em unidades arbitrárias, não é atribuída uma unidade física explícita a esses parâmetros. O símbolo "—" indica, portanto, que uma unidade física não é especificada na formulação semiquantitativa atual, e não que o parâmetro seja necessariamente adimensional.

As condições iniciais são:

$$
S(0)=200\ \mu\mathrm{M},\qquad
H(0)=0,\qquad
R(0)=0,\qquad
D(0)=0.
$$

Com exceção de $K_m$, os parâmetros são principalmente parâmetros efetivos escolhidos para representar qualitativamente o comportamento da cascata proposta. Em particular, $\alpha$ e $\gamma$ atuam como fatores efetivos de conversão entre variáveis representadas em diferentes escalas.

## Cenários de simulação

São consideradas cinco condições predefinidas.

| Cenário | Alteração dos parâmetros |
|---|---|
| Basal | Valores de referência |
| MAO-B aumentada | $V_{\max}^{*}: 100 \rightarrow 500$ |
| Produção aumentada de dopamina | $P: 50 \rightarrow 90$ |
| Deficiência antioxidante | $K_h: 0.5 \rightarrow 0.2$ e $K_r: 0.7 \rightarrow 0.3$ |
| Reparo reduzido | $K_d: 0.9 \rightarrow 0.2$ |

### Basal

A condição basal é utilizada como estado de referência. Dopamina, $\mathrm{H_2O_2}$, ROS e dano oxidativo evoluem em direção a um regime estável determinado pelo equilíbrio entre os termos de produção e remoção.

### MAO-B aumentada

A velocidade máxima efetiva é aumentada em cinco vezes. Isso aumenta o consumo de dopamina pela reação mediada pela MAO-B e intensifica a produção de $\mathrm{H_2O_2}$, que se propaga pelo modelo resultando em níveis mais elevados de ROS e dano oxidativo.

O aumento de cinco vezes corresponde a uma **perturbação paramétrica hipotética** utilizada para explorar a resposta do sistema. Portanto, não deve ser interpretado como uma medida experimental direta de uma condição patológica específica.

### Produção aumentada de dopamina

A taxa de produção de dopamina é aumentada de $50$ para $90\ \mu\mathrm{M}\,\mathrm{min}^{-1}$. A maior disponibilidade de substrato sustenta maior metabolismo mediado pela MAO-B e aumenta, consequentemente, $\mathrm{H_2O_2}$, ROS e dano oxidativo.

### Deficiência antioxidante

Os parâmetros associados à remoção de $\mathrm{H_2O_2}$ e à neutralização de ROS são reduzidos. A dinâmica da dopamina permanece semelhante à condição basal, enquanto $\mathrm{H_2O_2}$ e ROS permanecem elevados por períodos mais longos, produzindo maior dano oxidativo.

### Reparo reduzido

O parâmetro associado ao reparo/remoção do dano oxidativo é reduzido. Como $K_d$ aparece apenas na equação de $D(t)$, as trajetórias de dopamina, $\mathrm{H_2O_2}$ e ROS permanecem essencialmente inalteradas em relação à condição basal, enquanto o dano oxidativo se acumula em níveis mais elevados.

## Solução numérica

O sistema é resolvido numericamente utilizando o método clássico de Runge-Kutta de quarta ordem (RK4).

O passo de integração utilizado nas simulações é:

$$
h=0.05\ \mathrm{min},
$$

correspondente a $3\ \mathrm{s}$.

Uma comparação com $h=0.025\ \mathrm{min}$ não produziu alterações relevantes nas trajetórias, sustentando a utilização de $h=0.05\ \mathrm{min}$ nas simulações apresentadas no trabalho.

As simulações utilizam, em geral, um intervalo de $10\ \mathrm{min}$. Para os cenários de deficiência antioxidante e reparo reduzido, o intervalo é estendido para $20\ \mathrm{min}$ para permitir uma melhor visualização de suas dinâmicas.

## Interface interativa

O repositório inclui uma interface desenvolvida em Streamlit para exploração interativa do modelo.

A interface permite:

- selecionar um dos cenários predefinidos;
- comparar o cenário selecionado com a condição basal;
- alterar o tempo de simulação;
- visualizar as trajetórias temporais das quatro variáveis de estado;
- visualizar os parâmetros utilizados em cada simulação;
- criar combinações personalizadas de parâmetros; e
- visualizar um resumo numérico do estado simulado.

A aplicação interativa foi desenvolvida como um complemento computacional e didático ao modelo matemático.

## Instalação

Clone o repositório e acesse o diretório do projeto:

```bash
git clone <repository-url>
cd maob-ros-oxidative-damage-model
```

Crie um ambiente virtual, caso desejado, e instale os pacotes Python necessários:

```bash
pip install -r requirements.txt
```

## Executando a interface

A partir do diretório principal do repositório, execute:

```bash
python -m streamlit run interface/app.py
```

O Streamlit iniciará um servidor local e abrirá a aplicação no navegador.

## Estrutura do repositório

```text
maob-ros-oxidative-damage-model/

-- README.md
-- README-pt.md
-- requirements.txt
-- .gitignore

-- interface/
   -- app.py

-- octave/
   -- ...

-- figures/
   -- ...

-- docs/
   -- ...
```

## Escopo e limitações do modelo

Este modelo é deliberadamente simplificado e semiquantitativo. Seu principal objetivo é investigar as relações temporais entre os mecanismos representados no sistema de EDOs.

Entre suas principais limitações estão:

- $\mathrm{H_2O_2}$, ROS e dano oxidativo são representados como índices normalizados ou relativos, e não como concentrações intracelulares absolutas;
- diversos parâmetros são parâmetros efetivos e não devem ser interpretados como constantes bioquímicas diretamente mensuráveis;
- os mecanismos antioxidantes são representados por termos agregados de remoção/neutralização;
- os processos de reparo e remoção do dano são representados por um único termo efetivo;
- o modelo descreve a dinâmica temporal e não representa explicitamente a distribuição espacial ou os compartimentos celulares;
- o modelo não busca reproduzir toda a rede bioquímica associada ao estresse oxidativo ou à neurodegeneração.

Dessa forma, os resultados das simulações devem ser interpretados principalmente em termos de **alterações relativas e qualitativas entre os diferentes cenários**.

## Autores

**Giulia S. Ferreira**  
**Vinícius F. Wasques**  
**Juliana H. C. Smetana**

Ilum Escola de Ciência - Centro Nacional de Pesquisa em Energia e Materiais (CNPEM), Campinas, São Paulo, Brasil.

## Referência

Este repositório acompanha o trabalho de modelagem matemática:

**Ferreira, G. S.; Wasques, V. F.; Smetana, J. H. C.**  
*Modelagem Matemática da Produção de Espécies Reativas de Oxigênio (ROS) Mediada pela MAO-B e sua Relação com Dano Oxidativo.*
