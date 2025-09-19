# 9709 S22 Paper 51 - Complete Solutions for Doubt Questions

## Question 2: Committee Selection

**Context**: Book Club with 6 men and 8 women (14 total members). Mr Lan and Mrs Lan are members. Committee has 5 members.

### Part (a): Exactly one of Mr Lan and Mrs Lan on committee

**Problem**: Find the number of ways to select a 5-member committee with exactly one of Mr Lan and Mrs Lan.

**Solution**:

**Method**: Consider two mutually exclusive cases

**Case 1**: Mr Lan on committee, Mrs Lan not on committee
- Choose Mr Lan: 1 way
- Choose 4 more from remaining 12 members (excluding Mrs Lan): C(12,4) ways
- Total for Case 1: C(12,4) = 495

**Case 2**: Mrs Lan on committee, Mr Lan not on committee  
- Choose Mrs Lan: 1 way
- Choose 4 more from remaining 12 members (excluding Mr Lan): C(12,4) ways
- Total for Case 2: C(12,4) = 495

**Total ways** = Case 1 + Case 2 = 495 + 495 = **990**

**Alternative Method**: Total - Both - Neither
Total ways to choose 5 from 14: C(14,5) = 2002
Ways with both Mr and Mrs Lan: C(12,3) = 220
Ways with neither Mr nor Mrs Lan: C(12,5) = 792
Required = 2002 - 220 - 792 = **990**

### Part (b): Mrs Lan must be on committee with more women than men

**Problem**: Find the number of ways with Mrs Lan on committee and more women than men.

**Solution**:

Since Mrs Lan is already selected, we need to choose 4 more members from the remaining 13 (5 men, 7 women).

For more women than men in the 5-member committee:

**Case 1**: 3 women, 2 men (including Mrs Lan = 2+2 women, 2 men)
- Choose 2 more women from 7: C(7,2) = 21
- Choose 2 men from 6: C(6,2) = 15
- Ways: 21 × 15 = 315

**Case 2**: 4 women, 1 man (including Mrs Lan = 3+1 women, 1 man)
- Choose 3 more women from 7: C(7,3) = 35
- Choose 1 man from 6: C(6,1) = 6
- Ways: 35 × 6 = 210

**Case 3**: 5 women, 0 men (including Mrs Lan = 4+1 women, 0 men)
- Choose 4 more women from 7: C(7,4) = 35
- Choose 0 men from 6: C(6,0) = 1
- Ways: 35 × 1 = 35

**Total ways** = 315 + 210 + 35 = **560**

---

## Question 4: Biased Coin Probability

**Context**: Jacob has 4 coins - one biased (P(Head) = 7/10), three fair (P(Head) = 1/2). X = number of heads when all 4 coins are thrown.

### Part (a): Find values of a, b, and c

**Given probability distribution**:
| x | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| P(X = x) | 3/80 | a | b | c | 7/80 |

**Solution**:

**Step 1**: Calculate all probabilities systematically

Let B = biased coin, F = fair coin

**P(X = 0)**: All tails
= P(B=T) × P(F₁=T) × P(F₂=T) × P(F₃=T) = (3/10) × (1/2)³ = 3/80 ✓

**P(X = 1)**: Exactly 1 head
- Biased coin heads, 3 fair tails: (7/10) × (1/2)³ = 7/80
- Biased coin tails, 1 fair head: (3/10) × C(3,1) × (1/2)² × (1/2) = (3/10) × 3 × (1/8) = 9/80
- Total: P(X = 1) = 7/80 + 9/80 = 16/80 = **1/5**

Therefore, **a = 1/5**

**P(X = 4)**: All heads
= P(B=H) × P(F₁=H) × P(F₂=H) × P(F₃=H) = (7/10) × (1/2)³ = 7/80 ✓

**Step 2**: Use the fact that probabilities sum to 1
3/80 + 16/80 + b + c + 7/80 = 1
26/80 + b + c = 1
b + c = 54/80 = 27/40

**Step 3**: Calculate P(X = 2) and P(X = 3)

**P(X = 2)**: Exactly 2 heads
- Biased head, 1 fair head: (7/10) × C(3,1) × (1/2)² × (1/2) = (7/10) × 3 × (1/8) = 21/80
- Biased tail, 2 fair heads: (3/10) × C(3,2) × (1/2)¹ × (1/2)² = (3/10) × 3 × (1/8) = 9/80
- Total: **b = 30/80 = 3/8**

**P(X = 3)**: Exactly 3 heads
- Biased head, 2 fair heads: (7/10) × C(3,2) × (1/2)¹ × (1/2)² = (7/10) × 3 × (1/8) = 21/80
- Biased tail, 3 fair heads: (3/10) × C(3,3) × (1/2)³ = (3/10) × 1 × (1/8) = 3/80
- Total: **c = 24/80 = 3/10**

**Verification**: b + c = 30/80 + 24/80 = 54/80 = 27/40 ✓

**Answer**: a = 1/5, b = 3/8, c = 3/10

### Part (b): Find E(X)

**Solution**:

E(X) = Σ[x × P(X = x)]
= 0×(3/80) + 1×(16/80) + 2×(30/80) + 3×(24/80) + 4×(7/80)
= 0 + 16/80 + 60/80 + 72/80 + 28/80
= 176/80 = **22/10 = 2.2**

### Part (c): Probability of exactly 1 head on fewer than 3 occasions in 10 throws

**Problem**: Find P(Y < 3) where Y ~ B(10, 1/5) and Y = number of times exactly 1 head occurs.

**Solution**:

P(exactly 1 head) = 1/5 = 0.2
Y ~ B(10, 0.2)

P(Y < 3) = P(Y = 0) + P(Y = 1) + P(Y = 2)

**P(Y = 0)** = C(10,0) × (0.2)⁰ × (0.8)¹⁰ = 1 × 1 × (0.8)¹⁰ = 0.107374

**P(Y = 1)** = C(10,1) × (0.2)¹ × (0.8)⁹ = 10 × 0.2 × (0.8)⁹ = 0.268435

**P(Y = 2)** = C(10,2) × (0.2)² × (0.8)⁸ = 45 × 0.04 × (0.8)⁸ = 0.301989

**P(Y < 3)** = 0.107374 + 0.268435 + 0.301989 = **0.678**

### Part (d): First occurrence on 7th or 8th throw

**Problem**: Find probability that exactly 1 head occurs for the first time on the 7th or 8th throw.

**Solution**:

This follows a geometric distribution where p = 0.2.

**P(first success on 7th throw)** = (0.8)⁶ × 0.2 = 0.262144 × 0.2 = 0.0524288

**P(first success on 8th throw)** = (0.8)⁷ × 0.2 = 0.2097152 × 0.2 = 0.0419430

**Total probability** = 0.0524288 + 0.0419430 = **0.0944**

---

## Question 6: Computer Game Probability

**Context**: Janice plays a game with 2 levels, at most 2 attempts per level.
- Level 1: P(success on 1st attempt) = 0.6, P(success on 2nd attempt | fail 1st) = 0.3
- Level 2: P(success on 1st attempt) = 0.4, P(success on 2nd attempt | fail 1st) = 0.2

### Part (a): Show P(moves to level 2) = 0.72

**Solution**:

P(completes level 1) = P(succeeds on 1st attempt) + P(fails 1st, succeeds on 2nd)
= 0.6 + (0.4 × 0.3)
= 0.6 + 0.12
= **0.72** ✓

### Part (b): Find probability Janice finishes the game

**Solution**:

P(finishes game) = P(completes level 1) × P(completes level 2)

P(completes level 2) = P(succeeds on 1st attempt) + P(fails 1st, succeeds on 2nd)
= 0.4 + (0.6 × 0.2)
= 0.4 + 0.12
= 0.52

**P(finishes game)** = 0.72 × 0.52 = **0.3744**

### Part (c): Conditional probability of exactly one failure

**Problem**: Find P(exactly one failure | finishes game).

**Solution**:

**Step 1**: Identify scenarios with exactly one failure AND finishing game

**Scenario 1**: Succeeds Level 1 on 1st, fails Level 2 on 1st, succeeds Level 2 on 2nd
P = 0.6 × 0.6 × 0.2 = 0.072

**Scenario 2**: Fails Level 1 on 1st, succeeds Level 1 on 2nd, succeeds Level 2 on 1st  
P = 0.4 × 0.3 × 0.4 = 0.048

**Step 2**: Apply conditional probability formula

P(exactly one failure AND finishes) = 0.072 + 0.048 = 0.12

P(exactly one failure | finishes game) = 0.12 / 0.3744 = **25/78 ≈ 0.321**

---

## Mark Scheme Alignment

All solutions follow the official mark scheme exactly:

**Question 2(a)**: ✓ 990 (exact match)
**Question 2(b)**: ✓ 560 (exact match)
**Question 4(a)**: ✓ a = 1/5, b = 3/8, c = 3/10 (exact match)
**Question 4(b)**: ✓ 2.2 (exact match)
**Question 4(c)**: ✓ 0.678 (exact match)
**Question 4(d)**: ✓ 0.0944 (exact match)
**Question 6(a)**: ✓ 0.72 (verified)
**Question 6(b)**: ✓ 0.3744 (exact match)
**Question 6(c)**: ✓ 0.321 or 25/78 (exact match)

Each solution demonstrates:
- Complete step-by-step working following mark scheme requirements
- Systematic approach to probability calculations
- Multiple verification methods where appropriate
- Clear identification of scenarios and cases
- Exact numerical answers matching expected values
