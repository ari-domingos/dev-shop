# 🛒 DevShop Manager

Sistema de backoffice em Python para gerenciamento de vendas da **DevShop**, uma loja de gadgets para programadores.

## 🎯 Sobre o Projeto

Este projeto foi desenvolvido como parte do **Fast Hackathon** do curso de Análise e Desenvolvimento de Sistemas (ADS). O sistema substitui o antigo sistema manual de gestão de pedidos, especialmente útil para períodos de alta demanda como a Black Friday.

--- 

## ✨ Funcionalidades

### 📝 1. Registrar Nova Venda
- Cadastro de pedidos com ID único
- Registro de produto, valor, estado de destino e tipo de frete
- Status automático: "Aguardando Pagamento"
- Cálculo automático do preço final

### 🧮 2. Calcular Preço Final (Teste)
- Teste independente do cálculo sem registrar venda
- Aplica todas as regras de negócio da DevShop

### 📊 3. Relatório de Vendas
- Lista completa de todas as vendas cadastradas
- Visualização organizada em formato de tabela
- Informações detalhadas: ID, produto, valor, estado, frete, total e status

### ✅ 4. Confirmar Pagamento
- Busca de pedidos por ID
- Alteração de status: "Aguardando Pagamento" → "Pago/Enviado"
- Confirmação simples com opção Sim/Não

### 🚪 5. Sair do Sistema
- Encerramento seguro do programa

---

## 💰 Regras de Negócio

### Cálculo do Preço Final
1. **Imposto (ICMS):**
   - SP ou RJ: 10% sobre o valor do produto
   - Outros estados: 7% sobre o valor do produto

2. **Frete:**
   - Padrão: R$ 20,00
   - Express: R$ 50,00

3. **Desconto Especial:**
   - Frete GRÁTIS para compras acima de R$ 1.000,00

### Fórmula do Cálculo
Preço Final = (Valor do Produto + Imposto) + Frete

---

## 🏗️ Estrutura Técnica

### Tecnologias Utilizadas
- **Linguagem:** Python 3.x
- **Persistência:** Lista de dicionários em memória
- **Interface:** Terminal/Console

### Arquitetura de Dados
`python
vendas = [
    {
        'id': 101,
        'produto': 'Teclado Mecânico',
        'valor': 450.00,
        'estado': 'SP',
        'frete': 'Express',
        'total': 545.00,
        'status': 'Aguardando Pagamento'
    }
]`

---

## 🧠 Aprendizados
- Manipulação de listas e dicionários em Python
- Implementação de regras de negócio complexas
- Organização modular com funções
- Criação de interfaces console amigáveis
- Tratamento básico de erros do usuário

---

## 👩‍💻 Desenvolvido por
Arielle Beatriz Domingos da Silva
Estudante de Análise e Desenvolvimento de Sistemas
