# Descrição do Projeto

Este projeto é um site educacional para compartilhar tarefas de casa e exercícios de programação com estudantes. Os estudantes podem navegar, visualizar e baixar tarefas diretamente do portal.

## Estrutura do Projeto

- [`assignments/`](../assignments/) Cada tarefa de casa é armazenada em sua própria subpasta com uma estrutura consistente.
- [`templates/`](../templates/) Templates reutilizáveis para novo conteúdo
- [`assets/`](../assets/) Contém os recursos do site incluindo CSS, JavaScript, imagens e arquivos de configuração
- [`index.html`](../index.html) A página principal do site que serve como um portal estático para navegar e visualizar tarefas. O conteúdo é configurável através do arquivo [`config.json`](../config.json) para gerar dinamicamente listas e detalhes de tarefas.

## Diretrizes do Projeto

- Manter estilo consistente em todas as páginas
- Manter nomes de arquivos e pastas descritivos e organizados

## Padrões Educacionais

Ao gerar conteúdo para este projeto:

- **Focado em aprendizado**: Todo conteúdo deve ser projetado com objetivos de aprendizado claros e níveis de dificuldade apropriados
- **Amigável para estudantes**: Use linguagem clara e encorajadora que motiva os estudantes

## Commits

Este repositório segue o padrão _Conventional Commits_ para mensagens de commit. Sempre use esse formato ao criar commits e pull requests. Regras principais:

- Formato: `<type>(<scope>): <short description>`
- Tipos comuns: `feat`, `fix`, `docs`, `chore`, `style`, `refactor`, `perf`, `test`, `ci`
- Use escopos curtos que representem a área afetada: `assignments/python-basics`, `assets/js`, `assets/css`, `config`, `templates`, `.github`
- Mensagem curta em inglês ou português (consistente com o restante do commit history), no imperativo e sem ponto final.
- Quando necessário, adicione um corpo explicando a motivação e o impacto.

Exemplos:

- `feat(assignments/data-analysis): add starter dataset and example notebook`
- `fix(assets/js): correct date comparison for due dates`
- `docs(templates): update assignment template with new checklist`
- `chore(.github): add copilot-instructions.md`

Usar Conventional Commits facilita automações (releases, changelogs) e a leitura do histórico por outros colaboradores e por assistentes de IA.
