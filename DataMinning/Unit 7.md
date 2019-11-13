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

For associations rules whose confidence is very high can be considered for further analysis.

Apiori

Given transactions,

| Transactions | Itemsets |
| ------------ | -------- |
| T1           | {A,B,C}  |
| T2           | {A,C}    |
| T3           | {A,D}    |
| T4           | {B,E,F}  |

Given,

```
minimum support = 0.5
minimum confidence = 0.5
minimum lift = 1
```

Hence,

```
min support count = min support * no of transactions
                  = 0.5 * 4
                  = 2
```

The 1 - frequent item sets can be given as,
Item set | Support count
-- | --
{A} | 3
{B} | 2
{C} | 2
{D} | 1
{E} | 1
{F} | 1

Table 1:C1

Filtering on minimum support count,
Item sets | Support count
-- | --
{A} | 3
{B} | 2
{C} | 2

Table 1:L1

From above Table(L1), the two frequent item set can be given as,

| Item set | Support count |
| -------- | ------------- |
| {A,B}    | 1             |
| {A,C}    | 2             |
| {B,C}    | 1             |

Table 3: C2

Filtering an minimum count,

| Item sets | Support count |
| --------- | ------------- |
| {A,C}     | 2             |

Table 4: L2

From above L2, the 3 frequent item sets are empty. We know all non-empty subsets of a frequent item set are also frequent. Thus, the frequent item sets are:

```
{A,C}
{A} & {C}
```

The association rule can be given as

| Association rule | Support count | confidence | lift |
| ---------------- | ------------- | ---------- | ---- |
| A -> C           | 2             | 0.66       | 1.33 |
| C -> A           | 2             | 1          | 1.33 |

For `A -> C`,

```
confidence({A} -> {C}) = transaction both A & C / transaction A
                       = 2 / 3
                       = 0.66
```

```
lift({A} -> {C}) = confidence / fraction of C
                       = 0.66 / (2/4)
                       = 1.333
```

For `C -> A`,

```
confidence({C} -> {A}) = transaction both C & A / transaction C
                       = 2 / 2
                       = 1
```

```
lift({C} -> {A}) = confidence / fraction of A
                       = 1 / (3/4)
                       = 1.333
```

The above rule satisfy minimum support, confidence & lift,
The stray association rules are:

```
A -> & C -> A
```

```
minimum support = 0.5
minimum confidence = 0.7
minimum lift = 1
```
