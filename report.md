# Relatório Final – Análise Estática e Refatoração do Projeto HTTPie

## 1. Introdução
Este relatório apresenta a análise estática e o plano de refatoração realizados sobre o projeto HTTPie. O trabalho tem como objetivo identificar problemas estruturais, más práticas, vulnerabilidades e oportunidades de melhoria utilizando ferramentas de análise estática, além de propor e implementar uma refatoração controlada.

## 2. Descrição do Projeto Selecionado
- **Projeto:** HTTPie  
- **Repositório:** https://github.com/joaovxdd/httpie-refactor-trabalho 
- **Descrição:** Ferramenta de linha de comando para requisições HTTP com saída amigável.  
- **Linguagem:** Python  
- **Tamanho:** +20.000 LOC  
- **Popularidade:** +70k estrelas  

## 3. Ferramentas Utilizadas na Análise Estática
- **Pylint** – Análise de estilo  
- **Flake8** – Conformidade PEP8  
- **Bandit** – Segurança  
- **Coverage.py** – Cobertura de testes  
- **SonarCloud** – Métricas e debt analysis  

## 4. Métricas Coletadas (Simuladas)
- **Pylint Score:** 7.85/10  
- **Flake8 Issues:** 134  
- **Vulnerabilidades Bandit:** 3  
- **Cobertura de Testes:** 62%  
- **Duplicação:** 7%  
- **Complexidade média:** 9.4  

Arquivos mais problemáticos:
- `httpie/client.py`  
- `httpie/sessions.py`  
- `httpie/core.py`  

## 5. Problemas Identificados
### 5.1 Complexidade elevada
Funções longas, responsáveis por múltiplas tarefas.

### 5.2 Tratamento insuficiente de exceções
Chamadas HTTP sem timeout e sem `try/except`.

### 5.3 Más práticas de estilo
- Linhas > 120 caracteres  
- Variáveis nomeadas de forma pouco clara  
- Falta de docstrings  

### 5.4 Vulnerabilidades de segurança
- Ausência de timeout em requisições  
- Mensagens de erro pouco seguras  

### 5.5 Código duplicado
Blocos replicados relacionados à preparação de requisição.

## 6. Plano de Refatoração
1. **Adicionar timeout e tratamento de exceções**
2. **Reduzir complexidade** (funções menores)
3. **Melhorar legibilidade** (typing, docstrings, renomeação)
4. **Adequar PEP8** (flake8)
5. **Aumentar segurança** (mensagens sanitizadas)

## 7. Exemplo de Refatoração

### Antes:
```python
def send_request(url, method, data):
    response = requests.request(method, url, data=data)
    return response.text