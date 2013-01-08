## Progetto Qualità 
===================

I primi sistemi di Information Retrieval lavoravano su collezioni di qualità omogenea come documenti giuridici e articoli medici. 
Con l’avvento del web, le tecniche tradizionali di reperimento dell’informazione sono risultate poco efﬁcaci
in quanto incapaci di distinguere la qualità dei documenti; di qui la necessità di
ideare algoritmi in grado di selezionare le pagine web in base sia alla rilevanza
che alla qualità. Tra questi algoritmi, un posto di rilievo hanno assunto quelli di
link analysis, che cercano di inferire la qualità delle pagine web dalla struttura
topologica del grafo associato al web. Il lavoro descritto in questa relazione è stato
svolto all’interno di un progetto che ha lo scopo di valutare l’effettiva efﬁcacia di
tali algoritmi.

Il nostro lavoro è consistito nello sviluppo di un’applicazione web che, data
un’opportuna popolazione di pagine web, metterà a disposizione una serie di
funzionalità mirate alla raccolta di giudizi sulla qualità delle pagine stesse. Il
software citato esegue una pre-elaborazione dei risultati restituiti dai motori di
ricerca e a tal proposito sono stati sviluppati tre moduli: Interrogatore, che si
preoccuperà di estrapolare gli URL dai risultati; Campionatore che, data una
teoria euristica ragionevole, ﬁltrerà i risultati restituiti dall’Interrogatore e inﬁne
Downloader che si occuperà di memorizzare le pagine su disco.
