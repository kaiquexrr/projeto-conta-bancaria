# 🏦 Sistema Bancário em Python

Sistema de gerenciamento de contas bancárias desenvolvido em Python com orientação a objetos. Permite criar contas, realizar depósitos, saques e consultar saldo via terminal.

## 📁 Estrutura do projeto

```
projeto-conta-bancaria/
│
├── main.py              # Ponto de entrada da aplicação
├── models/
│   └── conta.py         # Classe ContaBancaria
├── services/
│   └── banco.py         # Classe Banco (gerencia as contas)
└── ui/
    └── menu.py          # Menus e interface com o usuário
```

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
pip install rich --break-system-packages
```

**3. Execute o programa**

```bash
python3 main.py
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

### Os 4 pilares da POO

**Encapsulamento** — O atributo `saldo` é privado (`__saldo`) e acessado apenas via `@property`, impedindo modificação direta de fora da classe. O saldo só pode ser alterado pelos métodos `depositar()` e `sacar()`.

**Abstração** — A classe `Banco` abstrai o gerenciamento da lista de contas. O menu não precisa saber como as contas são armazenadas — apenas chama `banco.criar_contas()`, `banco.buscar_contas()` e `banco.listar_contas()`.

**Herança** — Base preparada para evolução: `ContaBancaria` pode ser estendida por `ContaCorrente` e `ContaPoupanca` com comportamentos específicos sem reescrever a lógica base.

**Polimorfismo** — Com herança, diferentes tipos de conta podem sobrescrever métodos como `sacar()` e o sistema trata todos de forma uniforme.

### Outros conceitos

- Separação por módulos — modelos, serviços e interface em pastas separadas
- Método `__str__` para representação legível dos objetos
- `@property` para acesso controlado a atributos privados
- Tratamento de exceções com `try/except` nas entradas numéricas
- Validação de entradas do usuário (valores inválidos, negativos e zerados)
- Ponto de entrada com `if __name__ == '__main__'`

## 📌 Melhorias futuras

- Persistência de dados — salvar contas em arquivo JSON ou banco de dados
- Histórico de transações por conta
- Implementar `ContaCorrente` com limite e `ContaPoupanca` com rendimento de juros
- Validar formato numérico do número da conta

---

Desenvolvado por [Kaique](https://github.com/kaiquexrr) durante os estudos de Python e POO.