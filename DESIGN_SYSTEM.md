# Design system editorial

Identidade: Viseu em Agenda, portal independente local. Português europeu, voz direta, útil e coerente. Evitar linguagem genérica, excesso de gradientes, badges decorativos ou interfaces vazias que apenas liguem para terceiros.

## Princípios
- Verde escuro, superfícies claras, texto escuro; tokens existentes em styles.css são referência, rever contraste antes de mudar. Tipografia editorial nos títulos, sans-serif legível no corpo; hierarquia, grid, espaçamento e componentes consistentes.
- Fotografias reais de Viseu, do evento, local ou edifício que o acolhe, com licença individual comprovada, créditos e legenda precisa. Não usar ilustrações genéricas/IA como substituto; mostrar ausência de foto se necessário. Imagens locais otimizadas, proporção e dimensões, lazy loading, alt significativo quando informativo.
- Componentes reutilizáveis: navegação, pesquisa, cards, filtros, estados de dados, mapas/listas, formulários, cabaz, rodapé. Links externos claramente identificados; funcionalidades e informação dentro do portal sempre que possível.
- Layout responsivo, teclado, foco visível, contraste WCAG 2.2 AA como alvo, labels, sem dependência exclusiva de cor, sem hover obrigatório, áreas táteis adequadas, reduced motion. Não tapar conteúdo ou impedir navegação.
- Estados explícitos: carregamento, vazio, erro, desatualizado, sem foto, fonte indisponível. Exibir datas, unidade, local e fonte. Não simular conteúdo real.

## Apoio voluntário
Preservar «☕ Paga-me um café», fundo #FFDD00, texto escuro, link https://buymeacoffee.com/barretomendes em nova aba com rel noopener noreferrer. Home, rodapé e dock discreto; mobile com área reservada, sem sobrepor conteúdo. Sem tokens, scripts de pagamento ou dados bancários.

## Revisão visual
Capturar e inspecionar desktop (1440x1000), mobile (390x844) e tamanhos extremos quando afetados. Verificar scroll, overflow, elementos fixos, zoom, imagens, textos longos, estados de erro, interações e foco. Comparar antes/depois. Não redesenhar por rotina; justificar impacto e preservar experiência existente.
