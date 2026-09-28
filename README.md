# Atividade de Inteligência Artificial

Este repositório contém as resoluções das atividades avaliativas da disciplina de Inteligência Artificial.

## Q1 - Árvores de Decisão Manuais (ID3, C4.5 e CART)

Implementação manual de árvores de decisão para análise de risco de crédito.

### Base de Conhecimento
Atributos: História de crédito, Dívida, Garantia, Renda, Idade e Emprego.
Classes: Baixo, Moderado e Alto.

| Ex | História | Dívida | Garantia | Renda | Idade | Emprego | Risco |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | Ruim | Alta | Nenhuma | 0-15k | Jovem | Instável | Alto |
| E2 | Desconhecida | Alta | Nenhuma | 15-35k | Média | Instável | Alto |
| E3 | Desconhecida | Baixa | Nenhuma | 15-35k | Sênior | Estável | Moderado |
| E4 | Desconhecida | Baixa | Nenhuma | 0-15k | Jovem | Instável | Alto |
| E5 | Desconhecida | Baixa | Nenhuma | >35k | Sênior | Estável | Baixo |
| E6 | Desconhecida | Baixa | Adequada | >35k | Sênior | Estável | Baixo |
| E7 | Ruim | Baixa | Nenhuma | 0-15k | Jovem | Instável | Alto |
| E8 | Ruim | Baixa | Adequada | >35k | Sênior | Estável | Moderado |
| E9 | Boa | Baixa | Nenhuma | >35k | Sênior | Estável | Baixo |
| E10 | Boa | Alta | Adequada | >35k | Sênior | Estável | Baixo |
| E11 | Boa | Alta | Nenhuma | 0-15k | Jovem | Instável | Alto |
| E12 | Boa | Alta | Nenhuma | 15-35k | Média | Instável | Moderado |
| E13 | Boa | Alta | Nenhuma | >35k | Sênior | Estável | Baixo |
| E14 | Ruim | Alta | Nenhuma | 15-35k | Média | Instável | Alto |
| E15 | Ruim | Alta | Nenhuma | 0-15k | Jovem | Instável | Alto |
| E16 | Ruim | Alta | Nenhuma | 15-35k | Jovem | Instável | Alto |
| E17 | Desconhecida | Alta | Nenhuma | 0-15k | Média | Instável | Alto |
| E18 | Desconhecida | Alta | Nenhuma | 15-35k | Sênior | Estável | Alto |
| E19 | Boa | Alta | Nenhuma | 0-15k | Jovem | Instável | Alto |
| E20 | Boa | Alta | Nenhuma | 15-35k | Média | Instável | Moderado |
| E21 | Ruim | Baixa | Nenhuma | 0-15k | Jovem | Instável | Alto |
| E22 | Desconhecida | Baixa | Nenhuma | 0-15k | Média | Estável | Moderado |
| E23 | Desconhecida | Baixa | Adequada | 15-35k | Sênior | Estável | Moderado |
| E24 | Ruim | Baixa | Adequada | 15-35k | Média | Estável | Moderado |
| E25 | Boa | Baixa | Nenhuma | 15-35k | Jovem | Estável | Baixo |
| E26 | Boa | Baixa | Adequada | 15-35k | Média | Estável | Baixo |
| E27 | Boa | Baixa | Adequada | >35k | Sênior | Estável | Baixo |
| E28 | Desconhecida | Baixa | Adequada | >35k | Sênior | Estável | Baixo |
| E29 | Boa | Alta | Adequada | 15-35k | Média | Estável | Baixo |
| E30 | Boa | Alta | Adequada | >35k | Sênior | Estável | Baixo |

### Árvore ID3 (Ganho de Informação)
```text
História de crédito 
|- Ruim 
    |- Garantia = Adequada -> Moderada
    |- Garantia = Nenhuma -> Alta
|- Boa 
    |- Dívida = Baixa -> Baixo 
    |- Dívida = Alta
        |- Garantia = Adequada -> Baixo
        |- Garantia = Nenhuma 
            |- Renda = 0-15k -> Alto
            |- Renda = 15-35k -> Moderado
            |- Renda > 35k -> Baixo
|- Desconhecido
    |- Dívida = Alta -> Alto
    |- Dívida = Baixa
        |- Renda > 35k -> Baixo
        |- Renda 15-35l -> Moderado
        |- Renda 0-15k
            |- Emprego = Instável -> Alto
            |- Emprego = Estável -> Moderado
```

### Árvore C4.5 (Gain Ratio + Poda)
Nesta base, a árvore resultante é similar à ID3, pois os atributos são predominantemente categóricos e não há ruídos suficientes para justificar uma poda agressiva.

```text
Dívida = Alta?
|- Sim:
    História = Boa?
        |- Sim:
            |- Garantia = Adequada -> Baixo
            |- Garantia = Nenhuma:
                |- Renda 0-15k -> Alto
                |- Renda 15-35k -> Moderado
                |- Renda > 35k -> Baixo
        |- Não -> Alto
|- Não:
    |- História = Ruim?
        |- Sim:
            |- Garantia = Adequada -> Moderado
            |- Garantia Nenhuma -> Alta
        |- Não:
            |- História = Boa -> Baixo
            |- História = Desconhecida:
                |- Renda > 35k -> Baixo
                |- Renda 15-35k -> Moderado
                |- Renda 0-15k:
                    |- Emprego = Instável -> Alto
                    |- Emprego = Estável -> Moderado
```

### Base de Regras (ID3 / C4.5)
1. SE História=Ruim E Garantia=Adequada -> Risco=Moderado
2. SE História=Ruim E Garantia=Nenhuma -> Risco=Alto
3. SE História=Boa E Dívida=Baixa -> Risco=Baixo
4. SE História=Boa E Dívida=Alta E Garantia=Adequada -> Risco=Baixo
5. SE História=Boa E Dívida=Alta E Garantia=Nenhuma E Renda=0-15k -> Risco=Alto
6. SE História=Boa E Dívida=Alta E Garantia=Nenhuma E Renda=15-35k -> Risco=Moderado
7. SE História=Boa E Dívida=Alta E Garantia=Nenhuma E Renda>35k -> Risco=Baixo
8. SE História=Desconhecida E Dívida=Alta -> Risco=Alto
9. SE História=Desconhecida E Dívida=Baixa E Renda>35k -> Risco=Baixo
10. SE História=Desconhecida E Dívida=Baixa E Renda=15-35k -> Risco=Moderado
11. SE História=Desconhecida E Dívida=Baixa E Renda=0-15k E Emprego=Instável -> Risco=Alto
12. SE História=Desconhecida E Dívida=Baixa E Renda=0-15k E Emprego=Estável -> Risco=Moderado

**CART:** Regras binárias equivalentes à árvore CART.

### Análise e Escolha
O ID3 é eficiente, mas propenso a overfitting por não realizar podas. O C4.5 é mais robusto ao utilizar o Gain Ratio e suportar poda, facilitando a interpretação. O CART, sendo binário, é ideal para variáveis numéricas, porém menos intuitivo que as regras diretas.

**Escolha:** C4.5, devido à melhor generalização e capacidade de lidar com atributos categóricos e contínuos.

---

## Q2 - Implementação com Bibliotecas (ID3, C4.5 e CART)

**Biblioteca Utilizada:** Chefboost
**Motivo:** Permite a geração dos três tipos de árvores a partir de uma única base de dados com simplicidade.

### Resultados - ID3
```bash
==== ID3 ====
Accuracy: 100.0% on 30 instances
Confusion matrix: [[12, 0, 0], [0, 7, 0], [0, 0, 11]]
```

### Resultados - C4.5
```bash
==== C4.5 ====
Accuracy: 100.0% on 30 instances
Confusion matrix: [[12, 0, 0], [0, 7, 0], [0, 0, 11]]
```

### Resultados - CART
```bash
==== CART ====
Accuracy: 100.0% on 30 instances
Confusion matrix: [[12, 0, 0], [0, 7, 0], [0, 0, 11]]
```

---

## Q3 - Dataset Kaggle e Métricas de Avaliação

**Dataset:** Pima Indians Diabetes (Kaggle)
**Objetivo:** Prever a coluna `Outcome` (0 = não diabético, 1 = diabético).

Utilizou-se a árvore CART com profundidade limitada para evitar overfitting.

### Estrutura da Árvore
```bash
|--- Glicose <= 143.50
|   |--- IMC <= 27.35
|   |   |--- Glicose <= 105.50
|   |   |   |--- class: 0
|   |   |--- Glicose >  105.50
|   |   |   |--- IMC <= 9.80
|   |   |   |   |--- class: 0
|   |   |   |--- IMC >  9.80
|   |   |   |   |--- class: 0
|   |--- IMC >  27.35
|   |   |--- Idade <= 30.50
|   |   |   |--- Glicose <= 117.50
|   |   |   |   |--- class: 0
|   |   |   |--- Glicose >  117.50
|   |   |   |   |--- class: 0
|   |   |--- Idade >  30.50
|   |   |   |--- Glicose <= 106.50
|   |   |   |   |--- class: 0
|   |   |   |--- Glicose >  106.50
|   |   |   |   |--- class: 1
|--- Glicose >  143.50
|   |--- Glicose <= 154.50
|   |   |--- DiabetesPedigree <= 0.33
|   |   |   |--- Pele <= 18.50
|   |   |   |   |--- class: 1
|   |   |   |--- Pele >  18.50
|   |   |   |   |--- class: 0
|   |   |--- DiabetesPedigree >  0.33
|   |   |   |--- Glicose <= 152.50
|   |   |   |   |--- class: 1
|   |   |   |--- Glicose >  152.50
|   |   |   |   |--- class: 0
|   |--- Glicose >  154.50
|   |   |--- Idade <= 62.50
|   |   |   |--- Insulina <= 544.00
|   |   |   |   |--- class: 1
|   |   |   |--- Insulina >  544.00
|   |   |   |   |--- class: 0
|   |   |--- Idade >  62.50
|   |   |   |--- Pressao <= 85.00
|   |   |   |   |--- class: 0
|   |   |   |--- Pressao >  85.00
|   |   |   |   |--- class: 1
```

### Métricas
- **Acurácia:** 0.79
- **Precisão:** 0.67
- **Recall:** 0.75
- **F1-Score:** 0.71

---

## Q4 - Algoritmo PRISM

O PRISM induz regras por classe, selecionando o par atributo-valor com maior precisão.

### Regras Geradas (Exemplos)
- SE Glicose=(140.25, 199.0] E Gravidez=(6.0, 17.0] E DiabetesPedigree=(0.372, 0.626] ENTÃO Outcome=1
- SE Glicose=(140.25, 199.0] E Gravidez=(6.0, 17.0] E Insulina=(-0.001, 30.5] E Pressao=(80.0, 122.0] ENTÃO Outcome=1

### Métricas de Avaliação
- **Acurácia:** 0.67
- **Precisão:** 0.53
- **Recall:** 0.59
- **F1:** 0.56

---

## Shell de Sistema Baseado em Conhecimento

**Arquitetura:** Base de Conhecimento $\rightarrow$ Motor de Inferência $\rightarrow$ Explicação $\rightarrow$ Interface.

A ferramenta é genérica, permitindo que o usuário cadastre fatos e regras, escolha o tipo de encadeamento (Forward, Backward ou Mixed) e solicite justificativas (`why`, `how`).

### Exemplo de Uso
```bash
python shell_es.py
> add_fact chuva
Fato adicionado.
> add_rule chuva molhado
Regra adicionada.
> add_rule molhado escorregadio
Regra adicionada.
> forward molhado
Sucesso: True
Fatos: {chuva=True, molhado=True}
> why escorregadio
Backward: SE molhado=True ENTÃO escorregadio=True
```
