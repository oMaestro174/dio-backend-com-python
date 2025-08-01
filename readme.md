# Sistema Bancário em Python

Este projeto faz parte de um desafio do curso **Back-End com Python** da DIO.

## Desafio

Fomos contratados por um grande banco para desenvolver o seu novo sistema. Esse banco deseja modernizar suas operações e, para isso, escolheu a linguagem Python. Para a primeira versão do sistema, devemos implementar apenas 3 operações: **depósito**, **saque** e **extrato**.

## Funcionalidades

- **Depósito:**  
  Permite depositar valores positivos na conta bancária. Todos os depósitos são registrados e exibidos na operação de extrato.

- **Saque:**  
  Permite realizar até 3 saques diários, com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo suficiente, o sistema exibe uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques são registrados e exibidos na operação de extrato.

- **Extrato:**  
  Lista todos os depósitos e saques realizados na conta. Ao final da listagem, exibe o saldo atual da conta. Se não houver movimentações, exibe a mensagem:  
  `Não foram realizadas movimentações.`

## Observações

- O sistema trabalha apenas com 1 usuário, não sendo necessário informar agência ou número da conta.
- Os valores são exibidos no formato: `R$ xxx.xx`  
  Exemplo: `1500.45 = R$ 1500.45`

## Código-fonte

Veja o código principal em [banco.py](./banco.py).



## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](./LICENSE) para mais detalhes.

---

> Este é um projeto fictício para fins educacionais. Qualquer semelhança com instituições financeiras reais é mera coincidência.
