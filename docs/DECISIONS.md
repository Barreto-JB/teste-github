# Decisões de arquitetura
- Fundação HTML/CSS/JS + Node 22 + SQLite, sem dependências, reversível; não é a stack final de produção.
- Identidade editorial provisória; tipografia serifada, verde escuro, papel quente, terracota, ilustração original abstrata.
- Fontes em modo link-only, 25 nomes de freguesias referenciados na CAOP/DGAL. Dados de pesquisa restritos mantidos localmente.
- Administração loopback com token de ambiente. Não expor sem revisão de segurança.
- Branch isolada em repositório de teste; nenhuma alteração à main.
