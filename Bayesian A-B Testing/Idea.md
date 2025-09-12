# Contexto
Temos um chatbot de varejo para o WhatsApp e enviamos mensagens de venda para que as pessoas possam comprar os nossos produtos de forma automatizada, diretamente no WhatsApp.

## Cenário atual
Enviamos uma mensagem apenas com texto e um botão de falar com o chatbot. Sem imagem, afinal, fazer essas imagens para cada mensagem seria mais caro e demorado para implementar. Atualmente fazemos um disparo por semana.

## Objetivo
Queremos testar as 4 variantes para entendermos se alguma das modificações sugeridas é capaz de trazer melhorias significativas na conversão.

## Métrica de sucesso do teste
A mensagem deve ter a probability to the be best em 85% ou mais, e um risk menor que 1%.

--- Início da descrição das variantes
## O design do teste é o seguinte:
### Variante A (Controle)
Essa variante é a mensagem que já enviamos atualmente. Ela conta apenas com texto e um botão, que leva diretamente para a o ponto de compra automatizada do chatbot.

### Variante B (Foco na imagem)
Essa variante contém o mesmo texto e botão da variante A, mas também tem uma imagem. Com ela, queremos saber se ter uma imagem impacta na conversão.

### Variante C (Botão extra, sem imagem)
Esta mensagem é quase igual a variante A. Texto igual, sem imagem, mas com dois botões ao invés de um. O primeiro botão continua sendo aquele que leva para o ponto do fluxo em que existe a compra automatizada; o novo botão direciona o usuário para falar com o atendente.

### Variante D (Botão extra, com imagem)
Esta mensagem é igual a Variante C, com a adição de uma imagem (a mesma imagem da Variante B).

--- Fim da descrição das variantes