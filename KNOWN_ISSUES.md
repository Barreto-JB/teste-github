# Problemas e limitações conhecidas

Baseline de 27/11/2026, atualizar após verificação.
- Agenda: uma fonte integrada, 3 espaços no snapshot V67–V69; cobertura incompleta, horários e preços da fonte a confirmar, eventos passados devem ser excluídos. Não afirmar agenda completa.
- Fotografias: 3 fotografias reais reutilizadas por local; FNAC mostra edifício do Palácio do Gelo, Aula Magna mostra exterior do IPV, não auditório. Procurar fotos mais específicas autorizadas; sem ilustrações genéricas.
- Mobilidade: OSM regional, refs VIS não são limites administrativos, 3689 pontos com notas/revisão, associações a percursos não equivalem a linhas únicas. Horários oficiais e posições em tempo real não integrados; API MOBI 403.
- IMT: ZIP histórico STUV recuperado uma vez, tentativa seguinte devolveu HTML Incapsula, não contornar. Transdev resposta inválida. Bibliotecas geográficas foram testadas, mas isso não significa dados extraídos.
- Supermercados: cabaz manual; catálogos automáticos e promoções não validados/licenciados para publicação.
- Combustíveis: importação local; preço público automático pendente.
- Cinema, meteorologia, turismo detalhado, restaurantes, serviços, estacionamento, emprego, PWA e notificações: funcionalidades pendentes ou parciais.
- QA: testes Playwright locais aprovados em V71, mas harness ainda não versionado no repo; Lighthouse, WCAG completa, CI e disponibilidade 99,9% ainda não medidos/estabelecidos.
- Deploy: GitHub Pages pode servir anterior depois do push; confirmar versão e assets. V71 primeiro check ainda anterior; verificar antes de considerar publicado.
- Wikimedia: 429 observado em pedidos; respeitar Retry-After/backoff, procurar alternativas autorizadas sem contornar.

Para cada problema novo: ID, severidade, impacto, reprodução, evidência, estado, mitigação, responsável por papel, próximo teste. Fechar apenas com correção confirmada.
