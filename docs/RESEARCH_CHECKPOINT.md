# Checkpoint de investigação e implementação V31

**25/11/2026.** Contagens anteriores reportadas, não uma nova auditoria: 614 eventos históricos, 78 organizadores, 10.645 ocorrências de calendário; MOBI 167 linhas/4.394 paragens; MUV 24 linhas/21.254 horários (18.465 completos); CKAN 6 datasets/327 recursos. Ficheiros originais do PC ainda inacessíveis. Não reconstruir JSONs fictícios. Consultar SOURCE_REGISTRY.json para endpoints e estados.

Dados efetivamente disponíveis em pacote privado: 145 observações de combustível e 39 IDs de posto, 136 observações atualizadas no dia, 9 antigas; dois pares suspeitos de duplicação física. Importação SQLite validou estrutura, não direitos nem atualidade. Snapshot ausente do Git por prudência.

Implementado: frontend responsivo, pesquisa, 25 freguesias de referência, 16 ligações oficiais, cabaz manual de seis cadeias, desconto imediato simples e deslocação, importação local de preços; API e administração locais, SQLite, quarentena, hash e auditoria. Dados agregados sem autorização bloqueados.

Prioridades seguintes: recuperar originais da Viseu Agenda, MOBI, MUV e NOS; completar validação de licenças CKAN; integração de supermercados autorizada com GTIN, preços por loja e promoções; catálogo de organizadores; PWA, mapa, API de produção e autenticação. Comparar eventos futuros únicos no mesmo território e intervalo. Não afirmar superioridade sem auditoria.
