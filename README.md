# 📌 Projeto Ágil - Gerenciador de Tarefas

## ✅ Objetivo

Desenvolver um sistema simples de gerenciamento de tarefas utilizando conceitos de Engenharia de Software e Metodologias Ágeis. O projeto simula o ciclo de desenvolvimento de um software real, desde o planejamento até a entrega, com foco em controle de qualidade e gestão de mudanças.

## 🧠 Escopo do Projeto

Este sistema permite que usuários realizem operações básicas de CRUD (Create, Read, Update, Delete) sobre tarefas. Cada tarefa possui:
- Título
- Descrição
- Status (Pendente, Em Progresso, Concluído)
- Prazo de Entrega *(Mudança de escopo implementada)*

## 🚀 Funcionalidades

- Criar nova tarefa
- Listar todas as tarefas
- Atualizar informações da tarefa
- Deletar tarefa
- Filtrar tarefas por status
- Simulação de mudança de escopo (`prazo_entrega`)

## ⚙️ Tecnologias Utilizadas

- **Python 3.10+**
- **Flask**
- **SQLite**
- **pytest**
- **GitHub Actions**
- **draw.io** (UML)

## 🧪 Testes Automatizados

Utilizamos testes unitários com `pytest`, executados automaticamente pelo GitHub Actions a cada `push`.  
Os testes cobrem:
- Criação de tarefa
- Listagem
- Atualização
- Exclusão

## 🔄 Gestão de Mudanças

Durante o desenvolvimento, foi simulada uma **mudança de escopo**, com a adição do campo `prazo_entrega` nas tarefas.  
Essa mudança envolveu:
- Alterações no modelo de dados
- Atualização do formulário HTML
- Ajustes no código de backend
- Novos testes criados
- Atualização no README e Kanban

## 🛠️ Metodologia Adotada

- **Kanban**: Projeto gerenciado via GitHub Projects com colunas:
  - A Fazer
  - Em Progresso
  - Concluído

- **SCRUM (simulado)**: Planejamento em sprints curtas para dividir entregas
- **CI/CD com GitHub Actions**

## 📁 Organização do Repositório

```
📁 projeto-agil
├── 📁 src
│   └── app.py
├── 📁 tests
│   └── test_app.py
├── 📁 docs
│   ├── diagrama_classes.png
│   ├── casos_de_uso.png
│   └── diagramas.drawio
├── 📄 README.md
├── 📄 requirements.txt
└── 📄 .github
    └── workflows
        └── testes.yml
```

## 🧾 Instruções para Execução Local

### Requisitos
- Python 3.10+
- pip

### Passos

```bash
git clone https://github.com/johngbl/projeto-agil-gerenciador-tarefas.git
cd projeto-agil-gerenciador-tarefas
pip install -r requirements.txt
python src/app.py
```

Acesse em `http://localhost:5000` no navegador.

## 📋 Requisitos

### Funcionais
- Criar, listar, editar e excluir tarefas
- Atualizar status
- Armazenar e exibir prazo de entrega

### Não Funcionais
- Tempo de resposta inferior a 2 segundos
- Testes executados via pipeline automatizada
- Commits descritivos e distribuídos

## 🧱 Modelagem UML

- **🔗 Diagrama de Casos de Uso:** [Visualizar](docs/casos_de_uso.png)
- **🔗 Diagrama de Classes:** [Visualizar](docs/diagrama_classes.png)

Criados com [draw.io](https://draw.io)

## 🗂️ Kanban no GitHub

A gestão do projeto foi feita utilizando GitHub Projects no formato Kanban.  
🔗 [Acessar o quadro Kanban]([https://github.com/johngbl/projeto-agil-gerenciador-tarefas/projects/1](https://github.com/users/johngbl/projects/3))

## 🖼️ Demonstração

(Insira aqui um print ou gif do app rodando)

## 👨‍💻 Autor

**João Gabriel**  
Curso de Engenharia de Software  
TechFlow Solutions — 2025

## 🧠 Aprendizados

- Aplicação prática dos conceitos de Engenharia de Software
- Testes automatizados com GitHub Actions
- Integração contínua e versionamento com Git
- Gestão ágil de tarefas com GitHub Projects
