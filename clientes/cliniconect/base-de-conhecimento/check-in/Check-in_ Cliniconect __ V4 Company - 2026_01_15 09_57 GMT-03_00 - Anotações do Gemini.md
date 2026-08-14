15 de jan. de 2026

## Check-in: Cliniconect \<\> V4 Company \- Transcrição

### 00:00:00

   
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Opa, bom dia,  
**Erick Ferreira Macedo:** Bom dia. Só um  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Eric.  
**Erick Ferreira Macedo:** minuto. Beleza. Voltei aqui.  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** E aí, Eric, como é que tá essa essas mudanças no comercial  
**Erick Ferreira Macedo:** Vamos lá.  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** teu?  
**Erick Ferreira Macedo:** Ah, cara, sei lá, tipo, tá normal. Ó, sim, tinha tem esses problemas aí que o Coalison tinha reclamado que não tava conseguindo mexer, mas tá tá entrando,  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Uhum.  
**Erick Ferreira Macedo:** tá tá fazendo lá.  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Show, cara. Eric, vamos lá. Eh, para conseguir acertar, finalizar aqui o essa parte do CRM, cara,  
**Erick Ferreira Macedo:** Beleza. Só uma questão,  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** o Aham.  
**Erick Ferreira Macedo:** eh, só para iniciar aqui. Hoje eu vou ter que sair 10:30 que eu tô uma consulta online.  
   
 

### 00:00:56

   
**Erick Ferreira Macedo:** Então, assim, hoje é 10:30 mesmo.  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Mas eles usam Clean Connect ou não?  
**Erick Ferreira Macedo:** Não usa,  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Ah,  
**Erick Ferreira Macedo:** não.  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** então então nem vai.  
**Erick Ferreira Macedo:** Tá valendo. Nem vou.  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Bom, eh, Eric, seguinte, o vamos focar aqui então CRM, tá? O que eu tenho que a gente precisa ver, alinhar ali é essa questão do WhatsApp,  
**Erick Ferreira Macedo:** Você  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** do bote conversa, porque eh para fazer a conexão, eu você mencionou que em determinadas etapas que ele ativa, então eu não sei se tá tendo alguma, enfim, se tá se tem alguma API por fora, alguma coisa ali que tá puxando essa, essa informação,  
**Erick Ferreira Macedo:** chegou a criar algum web hook lá no RD?  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** porque eu peguei o no RD novo, Não, o que ele tem é o o token do RD CR do CRM, o Clean Connect 1, que é o antigo.  
   
 

### 00:01:47

   
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** O token dele, do teu usuário tá lá no no bot conversa, então imagino que tá integrando por ele, pelo pelo RDCRM1. Aí eu vou trocar pro RDCRM2, só que você mencionou que não é toda a atualização que ele faz a que ele dispara  
**Erick Ferreira Macedo:** Não, ele só dispara quando o lead chega.  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** ali.  
**Erick Ferreira Macedo:** Olha só, única coisa que ele faz, tipo assim, chegou um lead, eh, ele  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Uhum.  
**Erick Ferreira Macedo:** dispara,  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Mas esse quando você fez essa conexão, foi só puxando ali ou teve alguma programação envolvida? Você  
**Erick Ferreira Macedo:** não, não teve programação, não teve progrção não,  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** só  
**Erick Ferreira Macedo:** só teve configuração no web lá do RD e no eh no web hook, na configuração do web hook do bot conversa,  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Uhum. Ah, tá. Porque eu eu  
   
 

### 00:02:32

   
**Erick Ferreira Macedo:** que lá no bot conversa você faz a Quando chega o evento,  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** pro  
**Erick Ferreira Macedo:** né, você pega lá o Jason e faz algumas validação,  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Aham. Ah, tá. Então é que então é isso mesmo,  
**Erick Ferreira Macedo:** né?  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** eu vou ter que puxar do do outro RD mesmo. É porque eu não não encontrei tipo web hook, eh integração nativo, nada disso ligando o bot conversa diretamente lá. O que tem é o token da RD CRM que tá lá no no bot  
**Erick Ferreira Macedo:** Não é, é um é um web hook,  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** conversa.  
**Erick Ferreira Macedo:** né? Tipo, no box bot conversa, eu gerei um web hook e fui lá no RD e coloquei o web hook do bot  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** É,  
**Erick Ferreira Macedo:** conversa.  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** é.  
**Erick Ferreira Macedo:** E aí, obviamente, ele ele deve validar pelo token.  
   
 

### 00:03:10

   
**Erick Ferreira Macedo:** Não sei. Eu acho que ele não tá usando. Acho que não problema não é esse token, porque se tivesse algum problema de token, ele nem iria enviar pelo bot conversa. Mas, ô Calefe, faz assim,  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Aham.  
**Erick Ferreira Macedo:** pode deixar stand by isso daqui que eu já pedi para uma pessoa olhar aqui interna isso daí.  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Ah, tá. Show. Porque é um, eu vi que tem alguns detalhezinhos ali, pode ser que dê problema, mas é só trocar o pro outro RD, tá? Pro Clean Connect 4\. De resto, cara, toda a parte de configuração ali de pipeline tá tá estruturada.  
**Erick Ferreira Macedo:** Hã,  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Pera aí que eu tô no teu no antigo aqui. Tá toda estruturada. Eh,  
**Erick Ferreira Macedo:** prazer.  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** já tão mexendo ali, tem as tarefas, o Alisson começou a mexer, mas daí deu esse problema do do WhatsApp, daí eu ele parou.  
   
 

### 00:03:52

   
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** E as dificuldades que eu tô tendo com Al é realmente a questão de visualização ali dele, né? Tipo, ele tá como admis, enfim, acho que talvez um se acostumar um pouco ali com o RD também. E é o Felipe e o Alisson, né? Os dois vai tocar o CRM, né?  
**Erick Ferreira Macedo:** Isso. Só que o Felipe,  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Show.  
**Erick Ferreira Macedo:** eh, na verdade, na verdade, ele vai começar segunda-feira no comercial, né? Não era para ele começar hoje,  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Ah, tá.  
**Erick Ferreira Macedo:** entendeu? Mas eu já falei assim para eles,  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Ah,  
**Erick Ferreira Macedo:** porque entrou um menino aqui novo no no suporte e aí eu esses dois dias,  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** beleza.  
**Erick Ferreira Macedo:** hoje e amanhã vou pedir para ele passar as atividades pro menino, né? Fazer a transição ali mais tranquila.  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Sim. Beleza.  
   
 

### 00:04:41

   
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Eu vi que vocês fizeram uns testes de integração aqui.  
**Erick Ferreira Macedo:** Exato.  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** É, tem uns testes aqui que rolou no  
**Erick Ferreira Macedo:** Teste de integração.  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** CRM.  
**Erick Ferreira Macedo:** É que a gente então porque a gente vai tá fazendo eh a gente tá fazendo um comake, né, o tipo N8N lá para para que quando chega um lead, um tipo eh, chega um lead pro Felipe, o o a integração envia mensagem no WhatsApp. pelo WhatsApp do Felipe, né? Aí quando for pro Alisson, envia pro celular do Alisson, porque tipo assim, receber só num celular e passar pro outro, você perde muito lead com isso,  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Sim,  
**Erick Ferreira Macedo:** perde muito.  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** a gente pode fazer  
**Erick Ferreira Macedo:** Aí eles estão fazendo essa essa integração ali. E mas é  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Show. Se pessoal precisar de alguma ajuda ali com integração,  
**Erick Ferreira Macedo:** isso.  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** porque tem umas peculiaridades ali do RD, né, que tipo assim, a de propriedade criada, coisa assim.  
   
 

### 00:05:40

   
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Mas show.  
**Erick Ferreira Macedo:** Uhum.  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Eh, eu acho que tá, podemos dizer que tá 100% ali, né? O 100% não, né? Tá bem  
**Erick Ferreira Macedo:** É, vamos, tem que, é, tem que fazer funcionar,  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** caminhado.  
**Erick Ferreira Macedo:** eh, tem que ver ali como que o pessoal vai seguir, mas parece que sim. E as tarefas você criou lá em todas as  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Isso. Tem as tarefas aqui em todas as fases,  
**Erick Ferreira Macedo:** fases?  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** ó. Até te a gente tinha  
**Erick Ferreira Macedo:** Essas tarefas aí, você se baseou em no que mesmo?  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** um um fluxo que tinha encaminhado há um tempo. Aí eu fiz na naquele modelo, tá? daquele fluxo.  
   
 

### 00:06:14

   
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** O que que a gente tem aqui nas negociações? Eh,  
**Erick Ferreira Macedo:** Só no pré-venda que tem tarefa ou no no vendas também?  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** como  
**Erick Ferreira Macedo:** Você tem dois, tem dois funil, né? O de pré-venda e o de os dois tarefa ou  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** os dois tarefa? Tem as tarefas aqui quando entra em teste,  
**Erick Ferreira Macedo:** só?  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** eh, e quando entra em negociação aqui, que é tipo, ele finalizou o teste, aí tem as tarefas de follow-up para negociar com  
**Erick Ferreira Macedo:** Угуm.  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** ele. As automações das tarefas, Droga, cliquei no marketing ali sem querer ver que ele vai voltar. As automações ficam todas aqui eh escondidinhas, automações de venda. Aí tem todas elas aqui, ó, as as automações. Então aqui, ó, do trial, né, que é do ele faz essas mensagens aqui,  
   
 

### 00:07:03

   
**Erick Ferreira Macedo:** diferencial.  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** essas tarefas, as tarefas de cada dia, todas configuradas aqui e elas aparecem todas aqui. Então, entrou lá no dia, tem aqui, ó, essa tarefa aqui para ser completada. Essa outra vai aparecendo ali para eles de acordo responsável  
**Erick Ferreira Macedo:** Угуm.  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** mesmo. Então,  
**Erick Ferreira Macedo:** Você me reenvia esse  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** cada vez que eles movimentam aqui, né, de um Sim,  
**Erick Ferreira Macedo:** PDF? Você ficou de reenviar esse PDF aí para  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** vou te encaminhar, cara.  
**Erick Ferreira Macedo:** mim.  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Eu é que eu fui achar que tava num sistema meio eh antigo para caramba aqui, meu. Aí ele tava  
**Erick Ferreira Macedo:** E como que tá os o os leads aí?  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** até  
**Erick Ferreira Macedo:** Como que você chegou? Eh, tem aí tipo como que tá o as campanhas, como que tá o preço por lead?  
   
 

### 00:07:53

   
**Erick Ferreira Macedo:** Diminuiu,  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** aqui, ó. Então, puxei aqui do dia 1 até dia 14,  
**Erick Ferreira Macedo:** aumentou.  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** tá? Que que a gente tem de eh só tá o 14 eu não peguei, tá? Só tá até dia 13\. Eu fiz ontem essa atualização aqui.  
**Erick Ferreira Macedo:** Uhum.  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Então o nosso custo por MQL aqui, ele variou pouco, tá? Comparado com o final do ano ali, ele ficou bem bem estável, porque também a gente não teve muitas ações novas ali que rodaram, né, disso aqui. Então o preço manteve o custo por lead chegou a variar um pouco para baixo, tá? Diminuiu o tamanho dele. É, tava 16, agora tá bateu em 15\. E a taxa de qualidade também teve uma pequena queda, por isso, né, na verdade, a taxa de qualidade que caiu implicou no MQL eh diminuir.  
   
 

### 00:08:39

   
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Então assim, tá tá tá estável, tá o o processo aqui. Então é, na verdade, é o melhor solo pra gente poder plantar uma coisa nova, porque se ele tá estável, se eu plantar uma coisa nova, eu consigo verificar se ele aumentou, diminuiu, eh se melhorou ou não, de fato. Aí, inclusive, Eric, a de campanha tá as mesmas, tá? Campanhas aqui, é, rodando. Não não tivemos mudança ali nas campanhas, inclusive porque eu tô aqui contigo pros criativos novos que a gente elaborou lá, daquilo que a gente conversou. Eh, deixa eu abrir aqui em planejamento. Deixa eu abrir aqui a campanha. aqui. Deixa eu apresentar outra coisa aqui. Aqui. Boa. Ó, então, eh, alguns mais básicos, tá?  
   
 

### 00:09:42

   
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Então, isso aqui destacamos o multidisciplinar com três profissionais. repasse aí a o foco é o repasse de de comissões está tirando o seu sono. Então a gente tá focando em algumas coisas específicas, algumas dores específicas que abrange ali as clínicas multidisciplinar,  
**Erick Ferreira Macedo:** Угуm.  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** que é a questão de repaso de comissão. Então a gente fala que isso repasse de comissão está tirando seu sono. E daí a gente vende aqui uma parte da plataforma, né, que é realize o cálculo de relatórios automáticos de acordo com procedimentos, profissionais, valores e porcentagens definidas por você. Então, eh, isso aqui é uma um tô vendo que a gente tá mudando um pouco, né? Não tá sendo aquela lista de de tre, a gente focou num elemento só. Então, essa é uma das mudanças ali que a gente propôs. E aí eu fiz alguns bem bem parecidos aos a o bent ali que a gente olhou, né?  
   
 

### 00:10:32

   
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Então, falei,  
**Erick Ferreira Macedo:** pelo computador.  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** peguei aqui, eh, por que clínicas multidisciplinares estão migrando para Clinic Connect? E aqui eu coloquei o WhatsApp, o TIS. Aí até tipo assim, isso aqui seria a melhor forma de eu representar o Tis. Você acredita?  
**Erick Ferreira Macedo:** Tem que pensar, cara. Mas pode ser. Eu acho que poderia tá faturamento de convênios, né?  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** É,  
**Erick Ferreira Macedo:** Acho que é melhor.  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** é que para ficar pequenininho aqui, né? Tipo, é um um ícone,  
**Erick Ferreira Macedo:** Aham.  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** mas aqui embaixo eu falo, ó, gestão de convênios e faturamento,  
**Erick Ferreira Macedo:** Aham.  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** o agendamento e daí eu listo aqui essas funcionalidades que eu coloquei ali em cima,  
   
 

### 00:11:08

   
**Erick Ferreira Macedo:** Sim.  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** né, que eu destaquei aqui embaixo para ficar um pouco mais claro pra pessoa também. agenda confirmação pro WhatsApp,  
**Erick Ferreira Macedo:** Eu  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** gestão de pacotes e mensalidades e gestão de convênio e  
**Erick Ferreira Macedo:** assim, eh,  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** faturamento.  
**Erick Ferreira Macedo:** eu essa essas bolinhas aí, eu acho que dá pra gente melhorar ela. Eu achei muito eh grande. Eu acho que dá para melhorar o layout dela e dá para colocar mais dores aí.  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Tipo, mais dores, que exemplo você poderia me dar aí?  
**Erick Ferreira Macedo:** Ah, posso puxar aqui para você no biblioteca de anúncios do  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** É, é que quer ver o o  
**Erick Ferreira Macedo:** Facebook.  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** adibery libery.  
**Erick Ferreira Macedo:** Qual que era aquele lá conex, né? Conex.  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Deixa eu ver se ele tá aqui. Tem a seu fíio que a gente olhou.  
   
 

### 00:12:16

   
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Ah, calma aí. Eu tenho eu tenho o o briefing aqui.  
**Erick Ferreira Macedo:** Não sei se  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Clean connect.  
**Erick Ferreira Macedo:** tem  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Deixa eu puxar aqui no brief.  
**Erick Ferreira Macedo:** aparece também.  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Ó, aqui no briefing,  
**Erick Ferreira Macedo:** Nossa,  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** ah, a gente puxou esse daqui, ó.  
**Erick Ferreira Macedo:** ó. Eh, isso.  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Tá vendo? Aí, por isso que eu até fiz até bem bem parecido aqui, ó.  
**Erick Ferreira Macedo:** Aham.  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** botei aí alguns elementos e aqui embaixo explicando os KPIs ali, que no caso do seu seu seria as funcionalidades.  
**Erick Ferreira Macedo:** Ó, eu eu acho que aí, cara, tipo assim, duas coisas, a as bolinhas, acho que o layout ali, sei, não, não, eu acho que dá para melhorar aquele layout que você fez ali do isso e sei lá, eu acho que não vale.  
   
 

### 00:13:21

   
**Erick Ferreira Macedo:** Tipo assim, eh, aí você colocar funcionalidade para mim não, não sei, eu não vejo sentido muito colocar funcionalidade. Aí eu acho que aí precisaria ser métricas mesmo se fosse fazer algo do  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Uhum.  
**Erick Ferreira Macedo:** tipo.  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Então, ah, dá para usar.  
**Erick Ferreira Macedo:** Ou se for se ou se for funcionalidade, precisa estar mais ajeitadinho isso aí, eh,  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Uhum.  
**Erick Ferreira Macedo:** para que com a gente consiga colocar mais funcionalidades aí.  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Uhum. Mas o, por exemplo, se eu for utilizar métrica, tipo, eu sei, tem uma lá que é os do 30% acho que de falta que vem relacionado ao agendamento ali. Tem alguma outra métrica relacionada a a porque eu peguei eu peguei os as três principais ali, que o pessoal vem buscando agendamento, o WhatsApp que é um umidade importante e  
**Erick Ferreira Macedo:** É funcionalidade, né? Eu acho que isso da é isso daí é funcionalidade,  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** o é são exatamente são funcionalidades aqui.  
   
 

### 00:14:15

   
**Erick Ferreira Macedo:** não é métricas, né? Eu eu acho que para isso daí, do jeito que você tá fazendo para representar funcionalidade, eh, eu acho que que não. Eu acho que porque assim, se a gente for falar, a gente tá representando funcionalidade, a gente tem que representar mais funcionalidades, né?  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Por  
**Erick Ferreira Macedo:** E ah,  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** quê?  
**Erick Ferreira Macedo:** porque você perde um L, você perde um lead ali talvez que interessa isso, mas tem uma funcionalidade, por exemplo, que é renovação de pacote. Aí você vai perder o cara porque não chama a atenção  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Ah, não, mas daí eu tenho um outro que apresenta parte de renovação de pacote,  
**Erick Ferreira Macedo:** dele.  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** sabe? Tipo, eh, tipo assim, o qual que são os que mais chamam  
**Erick Ferreira Macedo:** Pô, é assim, ó. Você você tem que ver que que você tá tentando falar com essa mensagem.  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** atenção?  
**Erick Ferreira Macedo:** tá tentando a abrangir clínicas de convênio, aí você tem que colocar as funcionalidades que que faz sentido para clínicas de convênio.  
   
 

### 00:15:08

   
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Mhm.  
**Erick Ferreira Macedo:** Agora, tipo, se você tá falando, tem que entender o que que tá querendo fazer aí, entendeu? Se for clínica de convênio aí,  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Угуm.  
**Erick Ferreira Macedo:** eh, clínicas multidisciplinares que usa convênio, aí a gente pode trabalhar com algumas funcionalidades que trabalha com que vai afetar mais clínicas de convênio. Aí eu acho que vale a pena colocar a parte do financeiro eh e repass comissão que são, se a gente quiser tacar a clínica que trabalha com convênio,  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** E se for uma que não tem convênio assim,  
**Erick Ferreira Macedo:** né?  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** uma normal ali, o que que funcionalidade  
**Erick Ferreira Macedo:** Clínica multidisciplinar.  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** é?  
**Erick Ferreira Macedo:** Aí a gente pode falar bastante da da assinatura de documentos, pode falar dos pacotes, né?  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Uhum.  
**Erick Ferreira Macedo:** Se for no particular, mais o particular pode falar da eh n dos protocolos abas também pode falar,  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Mas protocol aba,  
   
 

### 00:16:04

   
**Erick Ferreira Macedo:** mas hã do méo eh dos protocolos ab,  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** tipo,  
**Erick Ferreira Macedo:** mas não dá muita ênfase, né? mais falar  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** mas tipo assim, que nem eu tenho multidisciplinar,  
**Erick Ferreira Macedo:** ali  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** mas eu não atuo com aba, aí eu vou ver ali que eles têm aba, tipo o que que vai me impactar.  
**Erick Ferreira Macedo:** não? Sim. Eh, mas é que hoje em dia, tipo, a 80% das clínicas multidisciplinais ou mais trabalha com aba assim?  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Hum.  
**Erick Ferreira Macedo:** Eu acho que é mais, eu acho que é mais de 80%.  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Nossa, 80%.  
**Erick Ferreira Macedo:** Diz para cima, viu?  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Caramba,  
**Erick Ferreira Macedo:** É muito raro você pegar uma clínica multidisciplinar que não trabalha com aba. Muito, muito raro mesmo.  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** é que aba é meio multidisciplinar também, né?  
**Erick Ferreira Macedo:** Na verdade é o que dá mais dinheiro pra clínica,  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** É sim.  
   
 

### 00:16:55

   
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Eu tento tento falar isso para minha  
**Erick Ferreira Macedo:** sabe? Hoje terapia AB é o que dá mais dinheiro pra clínica. Uma clínica multidisciplinar. você fazer fazer uma clínica multidisciplinar eh sem terapia aba  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** mulher.  
**Erick Ferreira Macedo:** hoje em dia, cara, você vai sofrer muito, não vai ter muito retorno, né? Porque as terapias caras que dá o retorno é as terapia aba, até que o convênio paga melhor, né?  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Mhm.  
**Erick Ferreira Macedo:** Ela paga muito melhor para por uma sessão de terapia aba do que para uma sessão de fisioterapia, psicologia. Tipo, é,  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Uhum.  
**Erick Ferreira Macedo:** é tipo cinco vezes maior às vezes chega o que o convênio passa.  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** E tá pensando aqui assim, se eu fosse, tá? Vamos,  
**Erick Ferreira Macedo:** Deixa eu só ver os outros para ver se a gente vai se talvez tenha coisa nos  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** vamos, vamos avançar, tá? Aí,  
   
 

### 00:17:44

   
**Erick Ferreira Macedo:** outros.  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** esse aqui é quase aquele o que listado, só que de outra forma, né?  
**Erick Ferreira Macedo:** É, esse daqui já ficou melhor, ó. Já se a gente já conseguiu falar de mais, do jeito que foi representado, a gente conseguiu falar de mais funcionalidades.  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Uhum.  
**Erick Ferreira Macedo:** Deixa eu ver. Eh, gestão de convênio, gestão financeira económica, gestão de pacotes e mensalidades, gestão de saneamento, reparo de comissão, assinatura digital.  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** É o que sempre tem nos criativos lá. Só mudou a  
**Erick Ferreira Macedo:** É,  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** visualização.  
**Erick Ferreira Macedo:** eu acho que nesse daí talvez a gente poderia eh só pegar aonde que tá onde onde que tá essas funcionalidades e e deixar em negrito o que mais chama atenção em cada  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Aham.  
**Erick Ferreira Macedo:** parte.  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Tipo, já já até sei aqui, ó. botar o logo do WhatsApp  
**Erick Ferreira Macedo:** É logo do  
   
 

### 00:18:44

   
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** aqui.  
**Erick Ferreira Macedo:** WhatsApp.  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Ah, eu eu tenho as partes que fica em negrito já, tipo, marcadas ali no briefing, eh, que normalmente a gente utiliza tá tudo aqui já,  
**Erick Ferreira Macedo:** É  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** é só alterar.  
**Erick Ferreira Macedo:** beleza.  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** E aí tem esse daqui. Aí eu peguei essa dor específica que é você trabalha e o plano não te paga por erros nat, que é as glosas que gera, né? que eu aí eu fui pegar alguns exemplos, peguei bastante gente reclamando, tipo assim, eh, bot li lá no no Redit, li nos fóruns lá e tal,  
**Erick Ferreira Macedo:** Угуm.  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** o pessoal falou assim: "Ah, eu faço a Tiz, aí tem um errinho, aí eu plano não faz o repasso, aí eu me lasço por causa disso." Então, Cliconet ajuda eu a não ter erro na na TIS, porque tem todo ali. Então, você trabalha e o plano não te paga por erros na TI, a Clíniconet ajuda no gerenciamento e preenchimento das guias para você fugir das glosas.  
   
 

### 00:19:39

   
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Aí,  
**Erick Ferreira Macedo:** Угуm.  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** eh, a gente, eu acho que a gente não conseguiu achar exatamente qual que é a tela do do TIS aqui. Onde seria essa tela?  
**Erick Ferreira Macedo:** Deixa eu ver se Ah,  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Eu tenho aqui um do  
**Erick Ferreira Macedo:** pode deixar essa tela mesmo aí. Pode deixar uma tela. Essa tela aí era legal. Não sei se Ah,  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** mesmo.  
**Erick Ferreira Macedo:** sei lá. Eu acho que convênios deixar alguma parte ali, alguma parte aí. gestão de convênios, porque do jeito que tá aí a é a pessoa tem que ler tudo, né? Mas sei lá, deixar em alguma parte aí gestão de convênios para para que ela, sei lá,  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** É,  
**Erick Ferreira Macedo:** se ela tá olhando o criativo, de alguma forma isso vai chamar atenção nela,  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** é, acho que eu vou fazer tipo botar uma setinha dessa assim e escrever gestão de convênio,  
   
 

### 00:20:24

   
**Erick Ferreira Macedo:** né?  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** sabe? Tipo, saindo da tela. Acho que vai ser um caminho assim.  
**Erick Ferreira Macedo:** É, pode ser.  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Bom, aí aqui eu vou até botar o que é melhorzinho aqui que eu pedi para ele fazer, que é essa aqui, ó, para ficar parecendo realmente que é um stories de uma pessoa, sabe? Então, tá vendo? Até que eu botei o o da Clinic Connect aqui.  
**Erick Ferreira Macedo:** Ага.  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Eh, então a ideia, uma pessoa mandou uma pergunta ali, né? Ah, como você organiza os os repasses na sua clínica multidisciplinar? Aí a pessoa contando a historinha ali, ah, era o caos, fazer isso na mão todo mês, mas automatizei tudo. O sistema já sabe a regra de cada um, valor fixo e calcula sozinho a cada atendimento.  
   
 

### 00:21:08

   
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Quem organizou essa parte financeira aqui foi a Clinic Connect. pro modo de repasse deles é sensacional, evita muito estresse, como se fosse um storage de uma pessoa mesmo.  
**Erick Ferreira Macedo:** Aham.  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** E aqui essa imagem aqui totalmente criada via iata. Esse aqui, essa essa clínica não existe,  
**Erick Ferreira Macedo:** Uhum.  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** apesar que eu acho que eu já entrei numas 30 dessa já. Eh,  
**Erick Ferreira Macedo:** Ah.  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** e aqui como você evita glosas na sua clínica multidisciplinar? Aqui a gente sofria muito com isso, mas geramos as glossas mudando o processo. Planeja gerar erro e inconsistência de dados que causa recusa. Faturamento T usa um sistema que preenche e envia as guias sozinhos já no padrão ANS. Aí isso aqui eu queria confirmar contigo.  
   
 

### 00:21:49

   
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Sim. E quem salvou o financeiro, quem salvou o financeiro aqui foi a Clin Connect. O modo de faturamento deles blindou a gente contra esses erros. Então é justamente a ideia como se fosse uma pessoa realmente postando no stories. Seш  
**Erick Ferreira Macedo:** Aham. Eu acho só ali, né, que talvez dá uma falsa ilusão, tipo a é o sistema que preenche e envia as guias sozinho, né, da acho que não é tão automatizado assim, né? Eu acho que a gente pode só mudar essa frase aí, que eh ele ajuda no preenchimento da das guias, né, e facilita o envio,  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Ja.  
**Erick Ferreira Macedo:** mas não faz isso sozinho e facilita o envio.  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Hum. Pera que eu perdi o aqui. Foi aí. Esse NS aqui é real, né? Não, eu fiquei com com dúvida se NS. Falei: "Será que é mesmo?" Uhum.  
   
 

### 00:22:47

   
**Erick Ferreira Macedo:** É sim. O próprio T é da NS, né?  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Boa.  
**Erick Ferreira Macedo:** Hã?  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Curtiu esse aqui.  
**Erick Ferreira Macedo:** Não, achei legal. Achei legal.  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Eu acho que esses aqui vão dar bastante resultado, cara. Esses bem orgânicozão assim, dá dá bastante resultado. Aí tem aqui a versão gourmet dele, né, que é a mesma coisa, só que gourmet. Eh, mas no geral a gente produziu esses criativos aqui. Eh, eu tô com os roteiros de vídeo para  
**Erick Ferreira Macedo:** Então,  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** construir esses dois  
**Erick Ferreira Macedo:** o o único assim que eu não gostei foi dos dois primeiros,  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** aqui.  
**Erick Ferreira Macedo:** dos restantes. Eu achei legal.  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Esse aqui também não.  
**Erick Ferreira Macedo:** Aham.  
   
 

### 00:23:25

   
**Erick Ferreira Macedo:** Você,  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Qual foi o  
**Erick Ferreira Macedo:** você quiser testar, você pode testar, mas eh eu colocaria pelo menos mais uma dor  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** T  
**Erick Ferreira Macedo:** aí, cara, além do comissões.  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** é é mais fácil fazer outro criativo daí contador para eles rodar rodar junto porque daí eu  
**Erick Ferreira Macedo:** Sério? Não pode ser. Então,  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** consigo  
**Erick Ferreira Macedo:** mas eh você quiser testar, pode testar. Verdando não ter gostado. Agora esse daí eu acho que a gente precisa mudar,  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Show.  
**Erick Ferreira Macedo:** a gente precisa melhorar esses esses redondinhos aí, essa arte redondinha e se for colocar nesse sentido, eu acho que faz sentido a gente buscar métricas,  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Uhum.  
**Erick Ferreira Macedo:** né,  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** E de métrica assim,  
**Erick Ferreira Macedo:** para colocar.  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** que que você consegue me trazer de  
**Erick Ferreira Macedo:** Ah,  
   
 

### 00:24:10

   
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** métrica?  
**Erick Ferreira Macedo:** tem que colocar no tem que olhar no Nboard lá do T connect, né? as métricas que dá para colocar inicialmente.  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Deixa eu ver aqui, ó. Vou falar para você que o do Atiron tá funcionando ainda.  
**Erick Ferreira Macedo:** Só  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Tá.  
**Erick Ferreira Macedo:** o o  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Atiron. Connec. É.  
**Erick Ferreira Macedo:** dele.  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Ixe, tá meio pesadinho aqui. Aí foi.  
**Erick Ferreira Macedo:** O que que tá?  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Cadê o dashboard aqui? Aí, essas métricas aqui  
**Erick Ferreira Macedo:** Compartilha comigo até. Ah, tá, tá compartilado.  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** de  
**Erick Ferreira Macedo:** É, então acho que dá para colocar, tipo, eh, tem que pegar, faz uma pesquisa aí pra gente no no Gemin cara, pega dessas métricas aí, quais das que tem aí, qual que faz que chamaria mais  
   
 

### 00:25:02

   
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Aham.  
**Erick Ferreira Macedo:** atenção?  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Eh, o que que eles talvez  
**Erick Ferreira Macedo:** Por exemplo,  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** procedimento  
**Erick Ferreira Macedo:** eu acho que eh eu eu fiz um levantamento das métricas top, né, só que eu a gente não tem o sistema. eu preciso desenvolver elas.  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Hum.  
**Erick Ferreira Macedo:** Tipo, eu fiz um levantamento umas métricas bem top assim, tipo taxa de ocupação da agenda,  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Ah, isso aí.  
**Erick Ferreira Macedo:** né? É legal. Eh, CAC, CAC paraa clínica também é legal.  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** O CAC mesmo, tipo porção de cliente paciente  
**Erick Ferreira Macedo:** O CAC mesmo é curso de aquisição do paciente,  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** cap.  
**Erick Ferreira Macedo:** só que a gente não tem, né? Ah, o CAC que,  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Aham. É  
**Erick Ferreira Macedo:** né, que a gente usa bastante,  
   
 

### 00:25:44

   
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** sim.  
**Erick Ferreira Macedo:** só que a gente não tem, mas eu fiz um levantamento de umas métricas, tipo ticket médio por paciente,  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Aham.  
**Erick Ferreira Macedo:** taxa de retenção do tratamento, receita hora por profissional, taxa de crossell,  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Jesus.  
**Erick Ferreira Macedo:** percentual de paciente que utiliza mais de uma especialidade. Então, eu peguei umas umas métricas legais assim de clínica, né, só que eh a gente não tem. Então, por enquanto que a gente não tem, a gente trabalha com o que a gente tem. Então, eu acho que é legal a gente olhar aí a parte da eh ah, status do agendamento, né? poderia ser uma métrica, mas não com esse nome. Eu acho que a gente poderia colocar eh percentual  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** de agendamento, sei lá, percentual de comparecimentos.  
**Erick Ferreira Macedo:** percentual de poderia ser percentual de comparecimento, né? Mas acho que ainda tem que é outro nome,  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Falta, talvez falta.  
**Erick Ferreira Macedo:** né?  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Falta porque é  
   
 

### 00:26:44

   
**Erick Ferreira Macedo:** Porque tipo não é que é que é vários, né? uma eh tipo, eu tô nesse gráfico aí,  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** dor.  
**Erick Ferreira Macedo:** eu vou olhar um percentual de todos o o histórico, né, de dos  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** É, mas tipo assim,  
**Erick Ferreira Macedo:** agendamentos.  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** quando eu abro aqui assim, o que que eu eu o que que eu olharia se eu fosse um gestor de falta  
**Erick Ferreira Macedo:** Ah, se tivesse aí, você ia, por exemplo,  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** falta o  
**Erick Ferreira Macedo:** você ia você ia você ia você ia ver tudo.  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** primeiro.  
**Erick Ferreira Macedo:** Você ia ver quantos atendimentos eh se você ia conseguir saber quantos atendimentos você teve, né?  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Uhum.  
**Erick Ferreira Macedo:** Eh, quantas faltas você teve?  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Não, mas tipo assim, qual que qual que eu bateria o olho primeiro? Eu falar assim,  
**Erick Ferreira Macedo:** Mas qual?  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** cara, eu acho que falta falta e confirmados assim, ah, porque os agendados assim, beleza, mas o vai ser aquele risquinho de falta que vai me chamar atenção, tipo assim, ó, quanta pessoa faltou, porque é o dinheiro que eu tô perdendo,  
   
 

### 00:27:33

   
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** sabe? Acho que falta é o e e as cores aqui,  
**Erick Ferreira Macedo:** Aham.  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** ele vai bate com isso aqui, né? Cor ali. Ah, tá. Só para que a gente vai ter que simular um aqui,  
**Erick Ferreira Macedo:** Sim.  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** né? Para poder tirar o print.  
**Erick Ferreira Macedo:** É. E a outra assim, ó. Então, a percentual de faltas, né? Taxa de faltas, alguma coisa assim. Eh, outro gráfico que é legal aí. Esse esse segundo é legal. você consegue saber em em relação ao mês anterior quantos pacientes novos você teve.  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** M.  
**Erick Ferreira Macedo:** Então é percentual de crescimento, taxa de de crescimento, né? Não seria uma taxa de crescimento,  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Uhum.  
   
 

### 00:28:17

   
**Erick Ferreira Macedo:** né? Mas seria eh em relação ao mês anterior, quantos pacientes novos você teve?  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Aham. É, novos pacientes cham eu, cara,  
**Erick Ferreira Macedo:** é percentual de novos percentual de novos caixa de nossos  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** eu vou eu vou até vou até pegar,  
**Erick Ferreira Macedo:** novos pacientes,  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** tem algumas unidades assim que atende bastante clínicas assim.  
**Erick Ferreira Macedo:** né?  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Vou ver se eles têm algum alguma coisa que eles usam de métrica e tal lá com eles de falar de retenção e tal. Pode ser que eles façam isso. Aí eu vou ver se eles têm isso. Aí eu até compartilho contigo de até desses estudos de métricas tava olhando, né? Quer dizer, já tem até algumas tipo ane assim é quase um SAS, né? An cohorte de de retenção e tudo mais.  
   
 

### 00:29:02

   
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Mas beleza. Eh, e o do T, se eu for tirar um print,  
**Erick Ferreira Macedo:** É,  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** dá para tirar desse daqui. É que é meio meio fraco, acho mesmo,  
**Erick Ferreira Macedo:** não Vai em, acho que se mais que faria sentido,  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** né?  
**Erick Ferreira Macedo:** vai em convênios, vai em guias. Nova guia, nova guia, que é o cadastro da guia, né? Acho que essa tela que faria mais sentido assim,  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Ah, tá.  
**Erick Ferreira Macedo:** mas não tem também.  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Deixar isso aqui.  
**Erick Ferreira Macedo:** Depois que você cadastra a guia, você consegue ver a guia mesmo,  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Ah, boa. Será que eu fizer aqui nesse vai rolar ou ou não?  
**Erick Ferreira Macedo:** sabe? Acho que vai,  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Porque sistema lá ele aceita  
   
 

### 00:29:42

   
**Erick Ferreira Macedo:** acho que vai. Depois você cadastra guia, você consegue ver a guia.  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** qualquer porcaria. Não vai aceitar qualquer porcaria que eu escrevi aqui.  
**Erick Ferreira Macedo:** Não, deixa eu ver  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Vai.  
**Erick Ferreira Macedo:** só.  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Tá. Ixe, isso aqui vai longe para preencher isso aqui  
**Erick Ferreira Macedo:** É,  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** tudo.  
**Erick Ferreira Macedo:** vai longe. Não é, é bem.  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Não, show. Bom, você tem teu tua consulta online agora. Eh, vou encaminhar para você também de qualquer forma os criativos ali. Eh, se quiser fazer algum comentário extra, tá?  
**Erick Ferreira Macedo:** Não, mas já fica validado assim. Vamos só mexer nesse último, então, nesse segundo. Quer dizer,  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Aham.  
**Erick Ferreira Macedo:** e aí,  
**Lucas Calefi Gonçalves (Calefi \- SCN\&Co):** Show.  
**Erick Ferreira Macedo:** beleza. Me passa o PDF lá do workflow lá que você da das tarefas.  
   
 

### A transcrição foi encerrada após 00:30:55

*Esta transcrição editável foi gerada por computador e pode conter erros. As pessoas também podem alterar o texto depois que ele for criado.*