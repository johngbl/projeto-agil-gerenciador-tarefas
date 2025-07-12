# 📌 Projeto Ágil - Gerenciador de Tarefas

## ✅ Objetivo

Desenvolver um sistema simples de gerenciamento de tarefas utilizando conceitos de Engenharia de Software e Metodologias Ágeis. O projeto simula o ciclo de desenvolvimento de um software real, desde o planejamento até a entrega, com foco em controle de qualidade e gestão de mudanças.

## 🧠 Escopo do Projeto

Este sistema permite que usuários realizem operações básicas de CRUD (Create, Read, Update, Delete) sobre tarefas. Cada tarefa possui:
- Título
- Descrição
- Status (Pendente, Em Progresso, Concluído)
- (Escopo Expandido) Prazo de Entrega

## 🚀 Funcionalidades

- Criar nova tarefa
- Listar todas as tarefas
- Atualizar informações da tarefa
- Deletar tarefa
- Filtrar tarefas por status
- Simulação de mudança de escopo (campo `prazo_entrega`)

## ⚙️ Tecnologias Utilizadas

- Linguagem: **Python 3.10**
- Framework: **Flask**
- Banco de Dados: **SQLite**
- Testes: **pytest**
- CI/CD: **GitHub Actions**
- UML: **draw.io**

## 🧪 Testes Automatizados

Utilizamos testes unitários para garantir a confiabilidade do sistema. Os testes são executados automaticamente via GitHub Actions a cada `push` no repositório.  
Os testes cobrem as funcionalidades principais do CRUD e validações de entrada.

## 🔄 Gestão de Mudanças

Durante o desenvolvimento, foi simulada uma **mudança de escopo**, adicionando o campo `prazo_entrega` às tarefas. A alteração foi justificada, documentada e incorporada no quadro Kanban e no código.

## 🛠️ Metodologia Adotada

- **Kanban**: Utilizado para organizar as tarefas na aba *Projects* do GitHub.
- **SCRUM**: Ciclo de trabalho em sprints simuladas.
- **DevOps**: Integração contínua com testes automatizados via GitHub Actions.

## 🗂️ Organização do Repositório

```
📁 projeto-agil
├── 📁 src
│   └── app.py
├── 📁 tests
│   └── test_tarefas.py
├── 📁 docs
│   └── diagramas.drawio
├── 📄 README.md
├── 📄 requirements.txt
└── 📄 .github/workflows/testes.yml
```

## 🧾 Instruções para Execução Local

### Pré-requisitos
- Python 3.10+
- Git
- pip

### Passos

```bash
git clone https://github.com/johngbl/projeto-agil-gerenciador-tarefas.git
cd projeto-agil-gerenciador-tarefas
pip install -r requirements.txt
python src/app.py
```

Acesse no navegador: `http://localhost:5000`

## 📋 Requisitos

### Funcionais
- Criar, listar, editar e excluir tarefas
- Atualizar status da tarefa
- Armazenar e exibir prazo de entrega

### Não Funcionais
- Tempo de resposta < 2s
- Testes automatizados a cada push
- Repositório com pelo menos 10 commits bem descritos

## 🧱 Modelagem UML

- Diagrama de Casos de Uso
- Diagrama de Classes

(Disponível na pasta `/docs/diagramas.drawio`)

## 🔄 Simulação de Mudança de Escopo

Foi adicionada uma nova funcionalidade: `prazo_entrega`.  
Essa mudança envolveu:
- Alteração no modelo de dados
- Atualização da documentação (README)
- Nova tarefa no quadro Kanban
- Novo teste automatizado

## 👨‍💻 Autor

**Gabriel [Seu Sobrenome]**  
Engenharia de Software - Projeto Ágil com GitHub  
TechFlow Solutions - 2025

## 🧠 Aprendizados

- Aplicação prática de Engenharia de Software
- Gerenciamento ágil com GitHub
- CI/CD com GitHub Actions
- Organização de projeto profissional
