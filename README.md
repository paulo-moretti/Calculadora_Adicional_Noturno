# Calculadora de Horas Trabalhadas

## Descrição
Este projeto é uma **Calculadora de Horas Trabalhadas**, desenvolvida em Python com a biblioteca Tkinter para a interface gráfica. O objetivo é permitir que os usuários insiram seus horários de entrada, saída e intervalos para calcular as horas trabalhadas e as horas noturnas computadas.

## Funcionalidades
- Interface intuitiva para inserção de dados.
- Cálculo automático de horas normais e horas noturnas computadas.
- Geração de um **relatório em formato Word (.docx)** com os dados e totais.
- Suporte a até **31 dias** para entrada de dados.

## Tecnologias Utilizadas
- **Python**
- **Tkinter** (para interface gráfica)
- **python-docx** (para geração do documento Word)

## Instalação
Antes de executar o projeto, certifique-se de ter o Python instalado.

1. Clone este repositório:
   ```bash
   git clone https://github.com/paulo-moretti/Calculadora_Adicional_Noturno.git
   cd Calculadora_Adicional_Noturno
   ```

2. Instale as dependências necessárias:
   ```bash
   pip install python-docx
   ```

## Como Usar
1. Execute o script Python:
   ```bash
   python calculadora_horanoturna.py
   ```
2. Insira as datas e os horários de trabalho.
3. Clique em **"Calcular"** para processar os dados.
4. Clique em **"Baixar Relatório Word"** para salvar um documento com os resultados.

## Exemplo de Relatório Gerado
O arquivo gerado será um **.docx** contendo uma tabela com:
- Data
- Entrada
- Intervalo Início e Fim
- Saída
- Horas Normais Trabalhadas
- Horas Noturnas Computadas
- Totais no final do documento

## Contribuição
Caso queira contribuir com melhorias, sinta-se à vontade para abrir um **Pull Request** ou relatar problemas na aba **Issues**.

## Licença
Este projeto está licenciado sob a **MIT License**. Sinta-se livre para modificá-lo e distribuí-lo conforme desejar.

---

### Autor
[Paulo Moretti](https://github.com/paulo-moretti)

