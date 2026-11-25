# viseu. — portal local independente

Primeira fundação funcional, baseada na investigação V31. Interface editorial responsiva em português de Portugal, sem dependências de rede no frontend. Marca provisória. Dados sem autorização não são publicados. Não é uma versão de produção.

## Executar localmente
Node.js 22.16+ (módulo SQLite integrado, experimental nesta versão). Não é necessário instalar dependências.

```sh
node server.mjs
# http://127.0.0.1:8080
node test.mjs
node test_server.mjs
```

Para a administração local, configura `VISEU_ADMIN_TOKEN` (segredo de pelo menos 24 caracteres) no ambiente do processo. Abre `/admin` e introduz o token. O servidor só escuta em loopback. Nunca exponhas esta versão administrativa à Internet. Para pré-visualização estática, `index.html`, `styles.css` e `app.js` bastam; o comparador funciona sem servidor.

Importação local privada (snapshot original não incluído no Git):

```sh
node server.mjs --import /caminho/viseu_v31_combustiveis.json
node server.mjs --status
node test.mjs /caminho/viseu_v31_combustiveis.json
node test_server.mjs /caminho/viseu_v31_combustiveis.json
```

## O que funciona
- Navegação, pesquisa local, 25 freguesias de referência e 16 ligações/fontes documentadas.
- Lista de compras manual, seis cadeias, comparação de cabaz completo e combinação de lojas com deslocação e desconto imediato simples. Não há preços automáticos nem cupões personalizados integrados.
- Importação privada V31 na UI, filtro por combustível/atualidade, e SQLite para importação administrativa com hash, deduplicação por posto/tipo/snapshot, quarentena e auditoria.
- API local de freguesias/fontes; endpoints de eventos e combustíveis permanecem bloqueados para publicação; administração protegida por token local.

## O que falta
Integrações autorizadas em produção, ingestão agendada, GTIN e promoções complexas, GTFS/tempo real, mapa incorporado, autenticação multiutilizador, PWA, backend de produção, revisão de segurança e E2E completo. Consultar docs/MASTER_PROMPT.md. Nenhum dado de investigação restrito ou segredo é publicado neste repositório. A base SQLite privada deve permanecer fora do Git.
