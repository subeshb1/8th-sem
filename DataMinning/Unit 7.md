## Association

## Strengths of Associations

### 1. Support

The support metric is defined for item sets not association rule i.e

```s
support(A -> C) = support(A U C), range[0,1]
```

The value of support helps us identify the rules worth considering for further analysis. This measure gives an idea of **how frequent an item set is in all the transactions.**

Mathematically,

```s
support({X} -> {Y}) = (Transactions Containing both X & Y) / (Total number of transactions)
```

For eg: If we consider only the items which occurs only 50 times out of 10,000 transactions then,

```s
support = 0.005
```

If an item set happens to have a very low support, we do not have enough information in the relations between it's items & hence no conclusions can be drawn.

## 2. Confidence
This means defines the likeliness of occurrence of consequent on the cart/set given that the cart already has the antecedents.
Mathematically,

```s
confidence ({X} -> {Y}) = (Transactions containing both X & Y) / Transactions containing X
```

For eg: If we consider, transactions containing both X & Y is 50 and the transaction containing X is 300 then, confidence is 0.166.