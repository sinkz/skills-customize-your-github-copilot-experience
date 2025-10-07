---
mode: agent
description: Criar uma nova tarefa de programação
---

# Criar Nova Tarefa de Programação

Seu objetivo é gerar uma nova tarefa de casa para os estudantes da Mergington High School.

## Passo 1: Coletar Informações da Tarefa

Se não for já fornecido pelo usuário, pergunte sobre o que será a tarefa.

## Passo 2: Criar Estrutura da Tarefa

1. Crie um novo diretório na pasta `assignments` com um nome único baseado no tópico da tarefa
2. Crie um novo arquivo no diretório chamado `README.md` com a estrutura do arquivo [assignment-template.md](../../templates/assignment-template.md)
3. Preencha os detalhes da tarefa no arquivo README
4. (Opcional) Adicione código inicial ou anexos se a tarefa precisar deles - adicione esses arquivos à mesma pasta da tarefa

## Passo 3: Atualizar Configuração do Site

Atualize a lista de tarefas no arquivo de configuração do site [config.json](../../config.json) para incluir a nova tarefa. Para o campo dueDate, use a data atual mais 7 dias a menos que especificado de outra forma.
