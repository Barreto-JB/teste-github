# Testes locais
Python 3 e Playwright. Num ambiente isolado, instala Playwright e usa Chrome ou configura VISEU_BROWSER para um canal Chromium instalado. Executa a partir do repositório:

    python tests/smoke.py
    python tests/extended.py

Os testes usam um servidor local temporário, dados publicados e contextos isolados. O apoio externo é simulado apenas no teste de navegação; não efetua pagamentos. Google Fonts e tiles OSM requerem rede. Capturas ficam numa pasta temporária ou VISEU_QA_OUTPUT. Para testar um snapshot histórico, define VISEU_SNAPSHOT_CLOCK=1 no smoke; não usar esse modo para afirmar atualidade dos dados públicos. Os testes assumem eventos futuros e fontes de referência atuais; atualizar critérios se cobertura mudar. CI ainda pendente.
