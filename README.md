# 🏦 Sistema Bancário em Python

Sistema de gerenciamento de contas bancárias desenvolvido em Python com orientação a objetos. Permite criar contas, realizar depósitos, saques e consultar saldo via terminal.

## 📋 Funcionalidades

- Criar conta bancária com nome e número
- Validação de conta duplicada — impede cadastrar o mesmo número duas vezes
- Depósitos com validação de valor (não aceita zero ou negativo)
- Saques com validação de saldo insuficiente
- Consulta de saldo
- Listagem de todas as contas cadastradas
- Interface colorida no terminal com a biblioteca `rich`

## 🛠️ Tecnologias utilizadas

- Python 3
- [Rich](https://github.com/Textualize/rich) — formatação colorida no terminal

## ▶️ Como executar

**1. Clone o repositório**
```bash
git clone https://github.com/kaiquexrr/projeto-conta-bancaria.git
cd projeto-conta-bancaria
```

**2. Instale a dependência**
```bash
pip install rich
```

**3. Execute o programa**
```bash
python conta_bancaria.py
```

## 🖥️ Como usar

Ao executar, um menu principal aparece no terminal:

```
[1] Criar conta
[2] Listar contas
[3] Acessar conta
[4] Sair
```

Ao acessar uma conta, um segundo menu permite realizar operações:

```
[1] Depositar
[2] Sacar
[3] Ver saldo
[4] Sair
```

## 💡 Conceitos aplicados

- Programação Orientada a Objetos — classe `ContaBancaria` com atributos e métodos
- Método `__str__` para representação legível dos objetos
- Tratamento de exceções com `try/except` nas entradas numéricas
- Validação de entradas do usuário (valores inválidos, negativos e zerados)
- Validação de duplicidade no cadastro de contas
- Separação de responsabilidades — lógica de negócio nos métodos da classe, navegação na função `menu_principal`
- Estrutura com `if __name__ == '__main__'`

## 📌 Melhorias futuras

- [ ] Persistência de dados — salvar contas em arquivo JSON ou banco de dados
- [ ] Histórico de transações por conta
- [ ] Criar classe `Banco` para encapsular a lista de contas
- [ ] Validar formato numérico do número da conta

---

Desenvolvido por [Kaique](https://github.com/kaiquexrr) durante os estudos de Python e POO.

