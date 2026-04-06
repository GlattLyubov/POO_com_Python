# Sistema de Passagem de Ônibus em Python
Projeto foi desenvolvido como parte do meu aprendizado em Python com nos conceitos de organização de arquivos e Programação Orientada a Objetos (POO).

# Sobre o projeto
Criei alguns projetos com Java, onde tive a oportunidade de me aprofundar em Programação Orientada a Objetos do qual resolvi voltar para este "mini-sistema" de passagem de ônibus que eu havia feito antes e resolvi implementar melhorias na lógica, dividir o código onde cada arquivo tem uma responsabilidade.

# Funcionalidades 
- Menu interativo via terminal;
- Informações do ônibus, cidades e distância;
- Cálculo de passagem com base na origem e destino do passageiro.

# Conhecimentos aplicados 
- Classes e Objetos
- Separação de responsabilidades
- Métodos com retorno
- Estruturas de decisão (if/else)
- Estruturas de repetição (while)

# Tecnologias 
- Python
- VS Code

# RESUMO
Este projeto é uma melhoria de um código que criei que era apenas um "linhão" que executa o código todo de uma vez. Agora, criei um sistema de classes onde cada arquivo tem uma responsabilidade. No início tudo estava amontoado. Agora eu entendo como o Python gerencia módulos e como importar funcionalidades de outros arquivos sem crair bagunça. No antigo código (que era o "passagem.py" e "passagem2.py") o main precisava saber como criar a dataclass, como sortear a poltrona e como formatar a data. Agora, no main principal, ele apenas diz processar_compra() e confia que o módulo de cálculo fará o trabalho. No projeto, eu saí de um modelo onde as cidades eram fixas no while para um modelo onde a classe Cidade gerencia sua prórpia lista e o enumerate faz o trabalho visual.  

Aprendi a base de como sistemas reais são construídos. No mundo profissional ninguém coloca o código inteiro em um arquivo só, a separação que fiz é exatamente o que se espera de um desenvolvedor de software.

# Autor
Desenvolvido por Matheus Cabral
