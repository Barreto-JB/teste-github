# Arquitetura técnica

## Estado atual
Portal estático GitHub Pages (branch viseu-pages), sem build obrigatório. index.html carrega app.js (rotas hash, pesquisa, cabaz, conteúdo), portal67.js (agenda e mobilidade), event-images.js (catálogo curado), styles.css (design), Leaflet local em vendor/, assets/ (fotografias e créditos), data/ (snapshots separados por licença), scripts/refresh_events.py (ingestão Lagenda). Pesquisa e filtros no navegador; cabaz usa armazenamento local; importação de combustíveis fica na memória. Mapas usam tiles externos OSM; não pedir localização sem necessidade. Apoio externo simples, sem integração de pagamentos no código.

Fluxo: fonte pública autorizada -> ingestão Python -> validar/deduplicar/normalizar -> snapshot versionado -> UI -> teste local -> revisão Git -> publicação Pages -> smoke público. Se falha, manter último snapshot válido. Evitar misturar dados com licenças distintas.

## Evolução técnica (proposta, não instalada)
| Tecnologia | Finalidade | Critério de adoção |
|---|---|---|
| TypeScript | Tipos e contratos | Migração incremental de módulos com testes |
| Astro | Estrutura modular e páginas rápidas | Piloto pequeno, preservar URLs e Pages |
| Tailwind CSS | Consistência visual | Só se reduzir manutenção, sem perder design system |
| Leaflet | Mapas | Já usado; respeitar política tiles, medir performance |
| Python | ETL e validação | Já usado; scripts reproduzíveis, ambiente isolado |
| GitHub Actions | CI, testes e publicação | Verificar workflow e permissões, sem alterar segurança/billing |
| Playwright | Testes browser | Já usado localmente; versionar harness e CI |
| Lighthouse | Auditorias | Medir baseline, condições iguais, antes/depois |
| Vitest | Testes unitários | Introduzir quando módulos JS/TS justificarem |
| Renovate | Dependências | Atualizações revistas, testadas e sem merge cego |
| Cloudflare Workers | APIs/cache/serviços dinâmicos | Apenas se Pages insuficiente, com aprovação para recursos externos/custos |
| SQLite / Cloudflare D1 | Dados estruturados | Quando volume/consultas justificarem; D1 depende de autorização externa |

Não migrar tudo imediatamente. Registar decisão arquitetural com problema, alternativas, custo/risco, compatibilidade e rollback. Preferir open source, estático e gratuito quando adequado. Dependências fixadas, licenças verificadas, sem código de terceiros não confiável. Separar apresentação, dados, lógica de negócio e testes, evitar duplicação. Nunca usar segredos no cliente ou repositório.

## Deploy
Fast-forward/merge normal de branch de trabalho atualizada; nunca force push. Verificar versão/cache dos assets, URLs relativas ao subdiretório Pages, conteúdo público e rollback. Não confundir HTTP 200 com deploy da versão correta. Não alterar configuração ou criar infraestrutura externa sem autorização.
