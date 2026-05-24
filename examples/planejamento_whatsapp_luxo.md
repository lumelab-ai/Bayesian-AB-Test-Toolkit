# Planejamento de Teste A/B: Campanha Exclusiva via WhatsApp

## 1. Contexto e Objetivo
**Empresa:** Marca de Moda Premium (Fictícia / Exemplo)
**Canal de Vendas:** WhatsApp (Atendimento via Personal Shoppers)
**Cenário:** Estamos nos preparando para a campanha de Lançamento da Coleção de Inverno. O WhatsApp é o nosso canal mais valioso, onde mantemos relacionamento direto com clientes de alto padrão.
**Objetivo do Teste:** Descobrir qual formato de mensagem ativa (outbound) gera a maior taxa de conversão (respostas positivas demonstrando interesse de compra ou agendamento de visita à loja física/envio de mala) ao ser disparada para a nossa base de contatos.

## 2. Desenho do Experimento
O teste será dividido em 4 variantes (A, B, C e D), enviadas para segmentos aleatórios da nossa base de clientes.

- **Variante A (Controle): Mensagem de Texto Padrão**
  Uma mensagem de texto redigida com tom elegante e de exclusividade, convidando a cliente para conferir a nova coleção.
  
- **Variante B: Texto + Foto do Lookbook (Imagem)**
  A mesma mensagem de texto da Variante A, acompanhada de uma fotografia em altíssima qualidade de uma peça-chave e exclusiva da coleção.

- **Variante C: Texto + Fashion Film (Vídeo)**
  A mesma mensagem de texto, acompanhada de um vídeo curto (15 segundos) e dinâmico, mostrando o caimento, os detalhes e o movimento dos tecidos em uma modelo. *(Nota de disparo: O envio de vídeo pode ter uma taxa de entrega ou download ligeiramente menor dependendo da conexão dos clientes, mas tem alto apelo visual).*

- **Variante D: Texto + Mensagem de Áudio da Personal Shopper**
  Uma pequena introdução em texto, acompanhada de um áudio curto (30 segundos) gravado com tom caloroso e intimista, reforçando a exclusividade do convite.

## 3. Hipóteses
1. **Hipótese Principal:** Acreditamos que a **Variante C (Vídeo)** terá a maior taxa de conversão, pois no segmento de luxo, o movimento, o brilho e os detalhes do tecido conseguem tangibilizar melhor o alto valor percebido da peça do que um texto ou foto estática.
2. **Hipótese Secundária:** A **Variante D (Áudio)** também pode ter um excelente desempenho, já que o luxo está intimamente ligado a um atendimento ultra-personalizado ("one-to-one").
3. Acreditamos que a **Variante A (Texto)** terá o menor desempenho por ser o formato menos envolvente.

## 4. Métricas e Parâmetros
- **Métrica de Sucesso (Conversão):** Total de clientes que engajaram positivamente (confirmaram interesse, pediram peças para provar ou agendaram visita) em até 48 horas após o recebimento.
- **Tamanho da Amostra Estimado:** Disparo para aproximadamente 10.000 contatos por variante (com potencial variação de entrega técnica entre 8.000 e 10.000).
- **Critério de Decisão:** O formato vencedor será adotado como o padrão oficial para campanhas futuras da marca no WhatsApp.

## 5. Especificações dos Criativos e Mensagens

**Variante A (Controle): Texto Padrão**
* **Texto:** "Olá, [Nome]. Selecionamos peças exclusivas da nossa nova Coleção de Inverno pensando no seu estilo. O preview já está disponível e adoraríamos apresentar a você em primeira mão. Posso preparar uma seleção para te mostrar ou agendar uma visita?"
* **Visual/Mídia:** Nenhuma. Apenas texto para focar na mensagem direta e na exclusividade.

**Variante B: Imagem**
* **Texto:** *(Mesmo texto da Variante A)*
* **Imagem:** Uma fotografia em altíssima resolução, capturada em estúdio com iluminação sofisticada e dramática. A imagem destaca um trench coat estruturado da nova coleção, evidenciando a textura premium do tecido e o corte impecável da alfaiataria. Nenhuma inserção de texto promocional sobreposta, mantendo a estética minimalista e puramente luxuosa.

**Variante C: Vídeo (Fashion Film)**
* **Texto:** *(Mesmo texto da Variante A)*
* **Vídeo:** Um clipe de 15 segundos em formato vertical (otimizado para a tela do celular). Mostra uma modelo caminhando elegantemente em um ambiente *clean* vestindo o trench coat destaque. O vídeo foca no caimento real da roupa, no balanço fluido do tecido e inclui breves closes nos acabamentos internos e costuras de alta qualidade. A edição conta com transições suaves e ritmo refinado.

**Variante D: Áudio**
* **Texto de Apoio:** "Olá, [Nome]! Deixei um recadinho rápido para você aqui abaixo. ✨"
* **Áudio:** Uma gravação de voz clara e natural de até 30 segundos, sem ruídos de fundo. A Personal Shopper fala em tom acolhedor, pausado e intimista: *"Olá, [Nome], tudo bem? Nós acabamos de receber o preview da nova Coleção de Inverno e eu lembrei imediatamente de você. O caimento e os tecidos das peças estão excepcionais nesta temporada. Eu adoraria separar alguns looks que são exatamente a sua cara para te mostrar, ou enviar uma mala para você provar em casa. Me avisa o que você acha melhor?"*

---

## 6. Planejamento Especial para Campanha de Black Friday (VIP Private Sale)

Dado o contexto competitivo e a sazonalidade de fim de ano, adaptamos este mesmo experimento A/B para uma campanha estratégica de **Black Friday VIP Private Sale**. 

* **Abordagem de Luxo na Black Friday:** Em vez de realizar descontos agressivos na base de dados (o que prejudicaria o posicionamento de alto padrão da marca), a campanha de Black Friday será baseada em **Acesso Antecipado Exclusivo (Early Access)** a lotes ultra-limitados da nova coleção e agendamento de experiências exclusivas de atendimento antes da abertura oficial ao público geral.
* **Formatos Utilizados:** Manteremos exatamente as mesmas 4 variantes originais (A, B, C e D), focando o apelo persuasivo na exclusividade e na escassez dos estoques especiais preparados para o fim de ano.

---

## 7. Cronograma Detalhado de Execução (Fases do Projeto)

```
[Semanas -2 a -1] ───► [Dia -1] ──────────► [Dias 1 a 3] ───────► [Dia 4 (Análise)] ───► [Dias 5 em diante]
 Criação de Mídia       Homologação Técnica    Disparos Aleatórios    Bayesian Toolkit     Roll-out Vencedor
 (Áudios/Lookbook)      (WhatsApp API)        (Base Total 40k)       (Relatório & Risco)   (Black Friday Week)
```

1. **Fase 1: Preparação e Produção (Semanas -2 a -1 antes da Black Friday):**
   * Gravação e tratamento dos áudios personalizados das Personal Shoppers em estúdio isolado (Variante D).
   * Edição e compressão otimizada do *Fashion Film* vertical de 15 segundos (Variante C).
   * Produção gráfica e exportação em alta qualidade do Lookbook (Variante B).
2. **Fase 2: Homologação e Testes Internos (Dia -1):**
   * Envio de testes internos na plataforma de mensageria para validar a entrega dos arquivos de mídia pesada (vídeos e áudios) e o carregamento do texto formatado.
3. **Fase 3: Disparo e Coleta de Dados (Dias 1 a 3 da campanha de Private Sale):**
   * Envio aleatório e balanceado para a base de clientes VIPs (~40.000 contatos no total, sendo ~10.000 por variante).
   * Monitoramento contínuo das respostas na ferramenta CRM para catalogar as conversões (agendamentos de malas/visitas e reservas de peças).
4. **Fase 4: Análise e Decisão no Bayesian Toolkit (Dia 4):**
   * Consolidação dos dados na planilha padrão `data_ab.xlsx` contendo as colunas `variant`, `reach` e `conversion`.
   * Execução do painel no notebook para calcular o desempenho bayesiano de cada formato de mídia.
5. **Fase 5: Roll-out da Variante Vencedora (Dias 5 em diante):**
   * Adoção oficial do formato vencedor para o disparo de massa da campanha geral de fim de ano para o restante da base de clientes.

---

## 8. Parâmetros Estatísticos Bayesianos (Showcase do Toolkit)

Para determinar a variante vencedora da campanha de Black Friday de forma totalmente estatística e consciente dos riscos de negócio, configuramos o **Bayesian A/B Test Toolkit** com as seguintes regras de parada e escolha:

* **Probabilidade de Ser a Melhor ($P_{best}$):** Mínimo de **85%**. A variante escolhida deve apresentar alta probabilidade de superar as demais, mitigando ruídos e flutuações amostrais comuns em períodos sazonais de alta volatilidade como a Black Friday.
* **Perda Esperada / Risco de Escolha ($Expected\ Loss$):** Limite máximo tolerado de **1%**. Se selecionarmos a variante vencedora sugerida pelo algoritmo, o risco de perda na taxa de conversão média projetada deve ser inferior a 1% relativo em comparação a qualquer outra variante.
* **Priors Beta (Priors de Entrada):**
  * *Prior Histórico:* Utilização de um prior informado $Beta(47, 953)$ baseado na taxa de conversão de atendimento de 4,7% observada nas coleções anteriores de inverno da marca.
  * *Prior Neutro:* Caso o comportamento de compra na Black Friday seja considerado imprevisível em relação ao comportamento padrão do ano, o painel do toolkit será alternado para a opção de prior não-informativo (uniforme) $Beta(1, 1)$.

---

## 9. Plano de Mitigação de Riscos e Salvaguardas

* **Risco 1: Latência e Falha no Download de Mídia Pesada (Variante C - Vídeo):**
  * *Mitigação:* O arquivo do *Fashion Film* de 15 segundos será altamente otimizado e comprimido para não ultrapassar **2.5 MB** de tamanho de arquivo, facilitando o download e a reprodução automática diretamente na visualização do chat dos usuários do WhatsApp com conexões móveis (4G/5G).
* **Risco 2: Bloqueio ou Classificação de Spam pela API do WhatsApp:**
  * *Mitigação:* O disparo de mensagens não será massivo de uma única vez. Utilizaremos *throttling* na fila de despacho, enviando lotes máximos de 2.000 mensagens por hora. Caso a taxa de denúncias ou "opt-out" de qualquer uma das variantes ultrapasse **1.5%** da base, o disparo daquela variante específica será suspenso no CRM.
* **Risco 3: Sobrecarga das Personal Shoppers (Variante D - Áudio e Variante C - Vídeo):**
  * *Mitigação:* O envio de áudio intimista ou vídeo gera alta taxa de resposta instantânea. Os disparos serão fracionados geograficamente ou por carteira de atendimento ao longo de 3 dias, garantindo que a equipe de Personal Shoppers consiga responder a todas as interações de forma rápida, mantendo o padrão luxuoso de atendimento.
