# Critérios de publicação

## Gates obrigatórios
- Escopo, critérios de aceitação e evidência de benefício real; diff revisto, sem alterações alheias, segredos ou dados privados. Sem dependências ou permissões desnecessárias. Sem código malicioso/injeções. Git diff --check e sintaxe/build quando aplicável.
- Dados: fontes e licenças confirmadas, atribuição, contratos, IDs, deduplicação, datas, unidades, cobertura, validação de regressão e snapshot anterior preservado. Sem dados inventados ou rótulos falsos. Imagens reais/licenciadas, sem links quebrados.
- Testes de funcionalidade alterada e regressões dos fluxos críticos existentes. Testes unitários/integração quando aplicável, testes browser reais; verificar consola, rede, loading/erro/vazio, teclado e responsividade. Zero erros críticos, sem regressões conhecidas. Se não for possível testar com segurança, não publicar alteração funcional.
- Capturas e inspeção visual desktop/mobile (1440x1000 e 390x844, incluir 320px ou tablet quando relevante), sem overflow/tapamento de conteúdo. Foco, contraste, labels e navegação por teclado. WCAG 2.2 AA como alvo.
- Performance: medir baseline e regressão quando mudança significativa; não afirmar Lighthouse sem execução. Documentar limitações, não bloquear documentação pura por ausência de teste visual.
- Branch de trabalho atualizada, commit descritivo, merge/fast-forward autorizado sem force push. Confirmar commit remoto e GitHub Pages com versão, recursos e smoke público. Se deploy pendente, reportar apenas push confirmado. Se falha, rollback apenas próprio commit e retestar.

## Alvos mensuráveis (não resultados já medidos)
| Métrica | Alvo | Medição |
|---|---|---|
| Lighthouse performance | >=90 | Mobile/desktop, mesma configuração, comparar antes/depois |
| Lighthouse accessibility | >=95 | Auditoria + testes manuais, não equivale a certificação |
| WCAG | 2.2 AA | Teclado, contraste, semântica, fluxos, revisão manual |
| Disponibilidade | 99,9% | Monitorização temporal com janela/denominador; não inferir de HTTP isolado |
| Erros críticos JS | 0 | pageerror/console, fluxos testados |
| Fluxos críticos testados | 100% dos catalogados | Denominador declarado; manter testes reproduzíveis |
| Proveniência/licença | 100% dos dados publicados | Manifesto e atribuição verificáveis |

Medir o que realmente foi executado; não inventar percentagens. Se alvo ainda não medido, registar pendência e implementar medição. Falha de gate obrigatório impede publicação; documentar alvos não atingidos, corrigir regressões e priorizar melhoria.

## Matriz de regressão mínima
- Home, agenda, explorar, mobilidade, poupar, fontes, passatempos, privacidade e pesquisa (rotas existentes).
- Agenda: carregamento, validade, pesquisa, filtros categoria/data/grátis/local, detalhes, fotografias reais e créditos.
- Mobilidade: mapa, tiles, pesquisa, zonas, seleção, paginação, estados sem dados e navegação de saída.
- Cabaz: adicionar, preços, comparar, descontos/deslocações, remover, persistência e privacidade; importação de combustíveis.
- Apoio: 3 links, texto PT-PT, #FFDD00, nova aba e rel seguro, mobile sem sobreposição, foco.
- Segurança: escape de texto, validação de URLs, sem dados pessoais/tokens. Sem falsos sucessos.

Cada execução regista testes executados/resultado, ambiente, screenshots quando aplicável, falhas e correções, commit, deploy e pendências. Versionar scripts de teste e integrar CI como tarefa prioritária.
