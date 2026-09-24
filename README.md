# Currency Exchange Rate Monitor

Um utilitário em Python que consome dados em tempo real de uma API de câmbio, processa as cotações com **Pandas** e exibe tabelas formatadas diretamente no terminal.

## Funcionalidades
- **Consumo de API REST**: Integração com a *ExchangeRate-API* para cotações atualizadas em BRL.
- **Filtragem Eficiente**: Uso de *Dictionary Comprehension* e conjuntos (`set`) para busca de alta performance.
- **Tabelas Interativas**: Exibição da tabela das 10 principais moedas globais ou da lista completa.
- **Tratamento de Exceções**: Navegação resiliente no terminal contra erros de digitação e oscilações de rede.

## Tecnologias Utilizadas
- Python 3.10+
- [Pandas](https://pandas.pydata.org/)
- [Requests](https://requests.readthedocs.io/)
