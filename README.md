# 🏢 Gestão Empresarial

Um sistema simples de gestão de empresa feito em **Python**, rodando direto no terminal.

Esse é o meu projeto de estudo: a ideia é ir aplicando aqui **tudo o que eu vou aprendendo** em programação — cada conceito novo, cada estrutura de dados e cada algoritmo que eu estudo vira uma melhoria nesse sistema. Ou seja, ele vai crescer junto comigo. 🚀

---

## 📋 O que o sistema faz hoje

Ao iniciar, o sistema dá boas-vindas ao usuário e mostra um menu:

```
1 - Verificar estoque de produtos
2 - Cadastrar produtos
3 - Consultar funcionários
4 - Realizar logout
```

| Opção | Função | O que faz |
|-------|--------|-----------|
| 1 | `verificar_estoque()` | Lista todos os produtos e suas quantidades |
| 2 | `cadastrar_produto()` | Pede nome e quantidade e adiciona/atualiza o produto no estoque |
| 3 | `consultar_funcionarios()` | Mostra os funcionários com CPF, cargo e salário |
| 4 | `realizar_logout()` | Sai do sistema |

---

## ▶️ Como rodar

Precisa ter o [Python 3](https://www.python.org/downloads/) instalado.

```bash
python gestão-empresarial.py
```

---

## 🧠 Conhecimentos aplicados até agora

- **Variáveis e tipos de dados** — strings, inteiros
- **Entrada e saída** — `input()` e `print()`
- **Conversão de tipos** — `int(input(...))` para ler números
- **Funções** — cada opção do menu é uma função separada (`def`)
- **Dicionários** — o estoque (`produtos`) é um dicionário `nome → quantidade`
- **Dicionários aninhados** — cada funcionário guarda outro dicionário com `cpf`, `cargo` e `salario`
- **Laços de repetição** — `for` percorrendo `.items()` de um dicionário
- **Condicionais** — `if / else` para validar a opção escolhida
- **Funções como valores (dispatch table)** — o menu usa um dicionário que liga cada opção à sua função:

  ```python
  pergunta = {
      "1": verificar_estoque,
      "2": cadastrar_produto,
      "3": consultar_funcionarios,
      "4": realizar_logout
  }
  pergunta[escolha]()
  ```

  Em vez de uma fila enorme de `if/elif`, o programa busca a função direto no dicionário e executa. Mais limpo e fácil de aumentar.

---



---

Feito por **Gustavo** enquanto aprende programação. 💻
