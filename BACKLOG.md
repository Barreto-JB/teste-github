# Backlog operacional

Estado inicial 2026-11-27. Escolher trabalho por impacto, confiança, esforço, risco e dependências. P0 bloqueia publicação se afeta produto; P1 alta; P2 normal. Atribuir estado (a fazer / em curso / bloqueado / entregue) e evidência em cada execução. Não marcar concluído sem critérios e teste.

| ID | Prioridade | Trabalho | Aceitação verificável | Estado |
|---|---|---|---|---|
| B01 | P0 | Baseline V71 | Página pública e JS com texto Paga-me um café; smoke público | A verificar |
| B02 | P1 | Testes e CI versionados | QA reproduzível sem caminhos pessoais, GitHub Actions, gates | A fazer |
| B03 | P1 | Ampliar agenda | Nova fonte autorizada, IDs únicos, contagem antes/depois, fotos reais, filtros | A fazer |
| B04 | P1 | Refresh agenda | Snapshots, falha preserva anterior, execução programada verificável | Parcial |
| B05 | P1 | Cinema | Sessões reais autorizadas com cinema/data/hora, filtro e validade | Bloqueado pela fonte/licença |
| B06 | P1 | Mobilidade oficial | Horários/GTFS validados ou fonte autorizada alternativa | Bloqueado parcialmente |
| B07 | P1 | Qualidade OSM | Validar limites, duplicados físicos, notas e percursos; distinguir regional | A fazer |
| B08 | P1 | Combustíveis | Dados atuais autorizados, unidade e data, mapa/filtro | A fazer |
| B09 | P1 | Meteorologia | Fonte oficial autorizada, previsão/avisos, falhas e validade | A fazer |
| B10 | P1 | Supermercados | Fonte/licença e preços normalizados, unidade, data, comparação verificável | Bloqueado parcialmente |
| B11 | P1 | Explorar Viseu | POI, serviços e turismo com coordenadas, licenças, filtros e fotos reais | A fazer |
| B12 | P1 | Acessibilidade/performance | Baseline Lighthouse mobile/desktop, teclado, contraste, WCAG, correções medidas | A fazer |
| B13 | P2 | PWA | Manifest, instalação e offline seletivo, cache versionado e atualização testada | A fazer |
| B14 | P2 | Favoritos | Persistência local, remover/exportar quando necessário, privacidade | A fazer |
| B15 | P2 | Restaurantes/estacionamento | Dados licenciados, localizações, horários/preços verificáveis | A fazer |
| B16 | P2 | Emprego/comunidade/notificações | Fontes, validade e consentimento opt-in | A fazer |
| B17 | P2 | Modernização incremental | ADR e prova de necessidade; piloto TypeScript/Astro, regressões aprovadas | A avaliar |
| B18 | P2 | Monitorização e dependências | Métricas disponibilidade, falhas de ingestão, dependências e rollback | A fazer |

Preservar V66 identidade, V67 agenda/mapa, V68 filtro por espaço, V69 fotografias reais, V70/V71 apoio voluntário. Não repetir tarefas sem regressão ou melhoria mensurável.
