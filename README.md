# Sistema Bancário Otimizado com Funções em Python

Este projeto é a solução para o desafio "Otimizando o Sistema Bancário com Funções Python" do bootcamp de Python da DIO. O objetivo era refatorar um sistema bancário simples, que originalmente tinha toda a sua lógica em um script monolítico, para um programa modularizado e baseado em funções.

## Sobre o Desafio

O ponto de partida foi um script com operações de saque, depósito e extrato contidas em um único loop `while True`. O desafio consistiu em:
1.  **Refatorar** o código existente, separando cada operação em sua própria função.
2.  **Aplicar** regras específicas para os argumentos de cada função (posicionais, nomeados).
3.  **Expandir** o sistema para incluir o cadastro de usuários (clientes).
4.  **Adicionar** a funcionalidade de criação de contas correntes, vinculando-as aos usuários.

## Funcionalidades Implementadas

O projeto final cumpre todos os requisitos da checklist:

### 1. Operações Bancárias (Refatoradas)
As operações básicas foram separadas em funções, tratando o `saldo`, `extrato` e outras variáveis como estado que é passado e retornado por elas.

* **Saque (`def saque(...)`)**:
    * Recebe argumentos apenas por nome (*keyword-only*).
    * Valida saldo, limite por saque e número de saques diários.
* **Depósito (`def deposito(...)`)**:
    * Recebe argumentos apenas por posição (*positional-only*).
    * Valida que apenas valores positivos sejam depositados.
* **Extrato (`def exibir_extrato(...)`)**:
    * Recebe `saldo` por posição e `extrato` por nome.
    * Exibe todas as transações ou um aviso se não houver movimentações.

### 2. Gestão de Usuários (Clientes)
Foi criada a função `cadastrar_usuario` para gerenciar os clientes do banco.

* **Validação de CPF**: O sistema impede que dois usuários sejam cadastrados com o mesmo CPF.
* **Coleta de Dados**: O usuário fornece nome, data de nascimento e CPF.
* **Formatação de Endereço**: O endereço é solicitado em partes (rua, número, bairro, cidade/UF) e armazenado como uma **string única** no formato: `Logradouro, numero - bairro - cidade/UF`.

### 3. Gestão de Contas
Foi implementada a função `criar_conta` para gerenciar as contas bancárias.

* **Agência Fixa**: Todas as contas criadas possuem a agência `0001`.
* **Número Sequencial**: O número da conta é gerado sequencialmente (1, 2, 3, ...), com base no número de contas já existentes.
* **Vínculo com Usuário**: Uma conta só pode ser criada se o CPF do usuário fornecido já existir no sistema, garantindo que toda conta tenha um usuário.
* **Regras de Negócio**: Um mesmo usuário (CPF) pode ter várias contas, mas uma conta pertence a um único usuário.

## Como Executar

1.  Certifique-se de ter o Python 3 instalado.
2.  Clone este repositório:
    ```bash
    git clone [https://github.com/Hytesy/Desafio_bancario_DIO.git](https://github.com/Hytesy/Desafio_bancario_DIO.git)
    ```
3.  Navegue até a pasta do projeto e execute o script:
    ```bash
    cd Desafio_bancario_DIO
    python implementação_bancaria.py
    ```
4.  Siga as instruções do menu interativo no terminal.
