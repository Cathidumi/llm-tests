# llm-tests
repository dedicated to research of LLMs capabilities in generation of structured JSON.

Aqui está uma proposta de arquivo `README.md` focada na estrutura e lógica solicitadas, documentando o funcionamento dos scripts na pasta `GeminiCodes`.

-----

# LLM Tests - Gerador de Formulários Otus (Gemini)

Este repositório contém experimentos e implementações para a geração de arquivos JSON estruturados para a aplicação de formulários Otus, utilizando LLMs (Large Language Models), especificamente a API do Google Gemini.

O foco principal desta documentação é a implementação modular encontrada na pasta `GeminiCodes`.

## 📂 Estrutura Principal (`GeminiCodes`)

A arquitetura recomendada para a geração de formulários divide o processo em duas etapas principais: **Interpretação da Intenção do Usuário** e **Geração de Componentes Específicos**.

### 1\. `userToAITranslator.py`: O Intérprete

> **Função:** Traduzir a linguagem natural do usuário para uma estrutura de dados intermediária.

Este script atua como uma camada de pré-processamento. Ele utiliza o modelo `gemini-2.0-flash` com `Structured Outputs` (via Pydantic) para converter uma solicitação de texto desestruturada (ex: "Crie uma pergunta de texto para nome e uma de número para idade") em uma lista de objetos JSON padronizada.

**Como funciona:**

  * Define uma classe `Translator` que espera: `typeQuestion`, `question` e `options`.
  * Recebe o input do usuário e retorna uma lista limpa de intenções, identificando qual tipo de pergunta (ex: `SingleSelectionQuestion`, `IntegerQuestion`) deve ser criada.

### 2\. `itensPrompts.py`: O Gerador de Itens (Recomendado)

> **Função:** Orquestrador principal que converte a lista de intenções no JSON final do formulário Otus.

Este é o arquivo central da solução recomendada. Ele importa o `userToAITranslator` para entender o pedido e, em seguida, gera cada item do formulário individualmente antes de montar a estrutura final.

**Fluxo de Execução:**

1.  **Entrada:** Recebe a descrição do formulário via função `generateJSON`.
2.  **Tradução:** Chama `userToAITranslator.translation()` para obter a lista de itens desejados.
3.  **Geração Modular:** A função `generateItemContainer` itera sobre a lista traduzida. Para cada tipo de questão (identificada por um `match/case`), ela chama uma função específica (ex: `textQuestion`, `checkboxQuestion`, `singleSelectionQuestion`).
4.  **Prompts Especializados:** Cada função específica (como `singleSelectionQuestion`) contém um prompt do sistema (System Instruction) altamente detalhado com o esquema JSON exato exigido pelo Otus para aquele tipo de dado.
5.  **Montagem:** O script agrega todos os itens no campo `itemContainer` e gera automaticamente a estrutura de navegação (`navigationList`) e metadados (`identity`, `metainfo`).

Esta abordagem é mais robusta pois isola a lógica de criação de cada componente, reduzindo alucinações e erros de sintaxe em formulários complexos.

Aqui está um texto técnico adicional focado especificamente na função `generateJSON` do arquivo `GeminiCodes/itensPrompts.py`, formatado para ser anexado à documentação:

-----

### 🛠️ Detalhamento: Função `generateJSON` (`itensPrompts.py`)

A função `generateJSON` atua como o **orquestrador principal** da solução recomendada. Ela é responsável por integrar a interpretação de linguagem natural, a geração de componentes isolados e a estruturação lógica do formulário final.

#### Assinatura

```python
def generateJSON(userInput: str, acID: str = 'TML', name: str = 'formulario') -> dict
```

#### Parâmetros

  * **`userInput`**: String contendo a descrição em linguagem natural do formulário desejado (ex: "Crie uma pesquisa com nome, idade e uma pergunta de múltipla escolha sobre frutas").
  * **`acID`**: (Opcional) O acrônimo base utilizado para gerar os identificadores únicos (`templateID` e `customID`) de cada item (Padrão: `'TML'`).
  * **`name`**: (Opcional) O nome interno atribuído ao objeto de identidade do formulário.

#### Fluxo de Processamento

A função executa quatro etapas críticas sequencialmente:

1.  **Geração de Conteúdo (`itemContainer`)**:

      * Invoca `generateItemContainer(userInput)`, que primeiramente chama o `userToAITranslator` para quebrar o pedido em uma lista de intenções estruturadas.
      * Itera sobre essas intenções e aciona funções geradoras específicas (como `textQuestion`, `integerQuestion`) para criar cada objeto JSON individualmente.

2.  **Cálculo de Navegação (`navigationList`)**:

      * Com base na contagem total de itens gerados, chama `generate_navigation_structure`.
      * Cria automaticamente o fluxo linear de navegação: *BEGIN NODE* → *Item 1* → *Item 2* → ... → *END NODE*, garantindo que o formulário seja funcional.

3.  **Normalização de Identificadores (Pós-processamento)**:

      * Executa um loop de correção sobre todos os itens gerados para padronizar os IDs.
      * Reescreve os campos `templateID` e `customID` sequencialmente (ex: `TML1`, `TML2`) para garantir consistência e unicidade, independentemente do que foi gerado pelo LLM.
      * Para questões do tipo `CheckboxQuestion`, também normaliza os IDs das opções internas (ex: `TML2a`, `TML2b`).

4.  **Montagem Final**:

      * Insere os contêineres de itens e navegação na estrutura base do objeto `Survey` (que contém metadados como `metainfo`, `identity`, etc.) e retorna o dicionário completo pronto para exportação.

-----

## ⚠️ Implementação Alternativa (`OtusFormsGem.py`)

> **Nota:** O uso deste script é **desaconselhado** para produção ou formulários complexos. Ele é mantido aqui apenas para fins de registro histórico e comparação de métodos.

O arquivo `OtusFormsGem.py` representa uma abordagem monolítica ("one-shot prompt").

**Diferenças Principais:**

  * Ao invés de dividir a tarefa, ele tenta gerar **todo** o array `itemContainer` de uma única vez, enviando um prompt massivo contendo exemplos de todos os tipos possíveis de questões para o modelo.
  * **Por que evitar:** Embora pareça mais simples inicialmente, essa abordagem sofre com:
      * Maior probabilidade de estourar o limite de tokens de saída.
      * Maior taxa de erro na estrutura JSON quando muitas perguntas são solicitadas.
      * Dificuldade em manter o contexto de "passo a passo" para formulários longos.

## 🚀 Como Executar

O projeto possui um servidor API configurado em `main.py` que utiliza a implementação recomendada.

1.  Certifique-se de ter as dependências instaladas (`requirements.txt`).
2.  Configure suas variáveis de ambiente (arquivo `.env`) com a `GEMINI_API_KEY`.
3.  Você pode rodar diretamente o script de teste no final de `itensPrompts.py`:

<!-- end list -->

```bash
python GeminiCodes/itensPrompts.py
```

Ou iniciar o servidor FastAPI com Uvicorn definido em `main.py`:

```bash
uvicorn main:app --host 127.0.0.1 --port 8080
```

O endpoint POST `/survey/` aceita uma descrição e retorna o JSON gerado usando a lógica do `itensPrompts.py`.
