# Fontes e licenças

Registo inicial; dados abaixo são checkpoints de 27/11/2026, não contagens atuais garantidas. Acesso público não equivale a direito de republicação.

| Fonte | Acesso / dados | Licença / estado | Próxima ação |
|---|---|---|---|
| Lagenda | https://lagenda.pt/dados-abertos/concelho/viseu.json | CC BY 4.0; integrado, snapshot 26/11, 43 IDs, 40 atuais/futuros em 3 locais nessa data | Refresh com script, dedupe, validade, verificar horários/preços |
| OpenStreetMap | Overpass, network:wikidata Q134717606 | ODbL 1.0; snapshot 27/11, 4048 pontos regionais, 514 refs VIS, 679 relações de percurso, 3882 pontos associados; 3689 notas/revisão | Validar limites, duplicados físicos, percursos; não é horário nem tempo real |
| OSM tiles | https://tile.openstreetmap.org/ | Política de uso e atribuição; sem prefetch em massa | Monitorizar erros, respeitar quota/política |
| Wikimedia Commons | assets/events/CREDITS.md, assets/CREDITS.md | Licenças individuais e fotos reais; 3 fotos de espaços na agenda V69 | Procurar fotos específicas autorizadas, respeitar 429 |
| MOBI VDL | https://mobiviseudaolafoes.pt/ e https://tracking.elevensystems.pt/vdl?tab=stops | Portal externo; API https://vdl.elevensystems.pt/api identificada, endpoints principais 403 | Alternativas oficiais/GTFS e licença; não contornar |
| IMT | https://www.imt-ip.pt/projetos-nacionais/nap/ | STUV 2023 FileGDB histórico identificado; novo download bloqueado/HTML inválido | Fonte alternativa legal, validar ZIP e licença |
| Dados abertos CIM VDL | https://dadosabertos.cimvdl.pt/ | CKAN, 6 datasets/327 recursos catalogados em checkpoint anterior; licença por recurso | Validar dados úteis e direitos |
| Viseu Agenda | https://viseuagenda.pt/ | HTML/paginação parcialmente identificados, reutilização não confirmada | Investigar feed autorizado e cobertura |
| Organizadores / freguesias | Inventário histórico de 78 organizadores; RSS 15/16 fontes investigadas | Cobertura e licença por fonte pendentes | Verificar individualmente, sem inferir autorização |
| NOS cinema | Sessões e catálogo previamente investigados | API/licença por confirmar | Fonte autorizada, cartazes separados |
| Supermercados | Adaptadores e catálogos investigados | Direitos, atualidade, unidade e acesso por validar | Não publicar preços sem fonte autorizada |
| DGEG | https://precoscombustiveis.dgeg.gov.pt/ | Fonte oficial; integração automática por validar | Direitos, atualidade, feed e esquema |
| IPMA | https://www.ipma.pt/ | Fonte oficial; condições de reutilização por verificar | API/avisos e validade |
| CAOP/DGT | Referência administrativa | Verificar versão/licença específica antes de integrar geometrias | Limites e cobertura concelhia |
| BOL / 3cket / entidades locais | Ligações oficiais | Licenças por confirmar | Fontes autorizadas, não copiar conteúdo |

## Contrato de ingestão
Por fonte: URL, responsável, licença e evidência, data de captura, validade, esquema, identificador estável, âmbito, unidades/fuso, contagem bruta e deduplicada, cobertura, erros e política de refresh/backoff. Validar dados antes de guardar como dataset; separar snapshots por licença, atribuir na UI e disponibilizar derivados conforme obrigações. Não republicar dados pessoais ou brutos de pesquisa. Manter último snapshot válido, distinguir data de captura de data de atualização, evitar falso tempo real. Reportar cada novo estado com evidência (descoberto/acessível/validado/autorizado/integrado).
