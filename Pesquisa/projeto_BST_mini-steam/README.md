
# Mini-Steam 🎮

## Sobre o Projeto

O **Mini-Steam** é uma aplicação simplificada que simula funcionalidades básicas de uma plataforma de jogos, como organização, busca e categorização de jogos. O projeto foi desenvolvido utilizando **Python** com ênfase em **Programação Orientada a Objetos (POO)** e estruturas de dados eficientes, como **Árvores Binárias de Busca (BST)** e **Tabelas Hash**.

---

## Funcionalidades

### 🎯 Principais Funcionalidades:
1. **Inserção de jogos**:
   - Cada jogo contém informações como ID, nome, desenvolvedora, preço e gêneros associados.
   
2. **Busca de jogos por preço**:
   - Busca jogos com preço exato.
   - Busca jogos dentro de uma faixa de preços.

3. **Busca de jogos por gênero**:
   - Utiliza uma tabela hash para organizar e buscar jogos rapidamente com base nos gêneros.

4. **Organização por árvore binária**:
   - Os jogos são organizados em uma **Árvore Binária de Busca (BST)**, permitindo consultas eficientes.

5. **Listagem de jogos**:
   - Exibição dos jogos armazenados em diferentes filtros.

---

## Estrutura do Projeto

O projeto está dividido em várias classes e métodos, cada um com uma função específica:

### 🛠️ Classes Principais:
1. **`Jogo`**:
   - Representa um jogo, contendo informações como:
     - ID
     - Nome
     - Desenvolvedora
     - Preço
     - Gêneros

2. **`ArvoreJogos`**:
   - Implementa a Árvore Binária de Busca (BST) para organização de jogos por preço.
   - Métodos principais:
     - Inserção de jogos na árvore.
     - Busca de jogos por preço exato.
     - Busca de jogos dentro de uma faixa de preços.

3. **`HashGeneros`**:
   - Utiliza uma tabela hash para organizar jogos com base nos gêneros.
   - Métodos principais:
     - Adicionar jogos à tabela hash.
     - Buscar jogos por gênero.

4. **`MotorBusca`**:
   - Gerencia as funcionalidades do sistema, integrando a árvore e a tabela hash.

---

## Tecnologias Utilizadas

- **Python **: Linguagem de programação principal.
- Estruturas de dados:
  - Árvore Binária de Busca (BST)
  - Tabela Hash
