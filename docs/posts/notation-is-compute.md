*Part 2 of five in **The Verification Changelog**: Five posts reading 2,500 years of mathematics as the release history of one technology, verification, and what that history means for anyone running AI agents unsupervised.*

Try multiplying CXLVII by XXXIX. In the Roman system, that is a job for a trained specialist with a counting board. Written as 147 × 39, it is homework for a ten-year-old. Same numbers, same result, wildly different cost. The whole difference sits in the data structure.

<figure style="margin: 2rem auto; text-align: center;">
<svg viewBox="0 0 560 250" role="img" aria-label="The same multiplication in Roman numerals, with no written procedure, and in place-value notation as a columnar calculation" style="max-width: 460px; width: 100%; height: auto;">
  <line x1="280" y1="30" x2="280" y2="200" stroke="var(--rule, #444)" stroke-width="1" stroke-dasharray="4 4"/>
  <text x="140" y="75" text-anchor="middle" style="font-family: var(--serif, serif); font-size: 22px;" fill="var(--fg, #e6e4df)">CXLVII</text>
  <text x="140" y="108" text-anchor="middle" style="font-family: var(--serif, serif); font-size: 22px;" fill="var(--fg, #e6e4df)">× XXXIX</text>
  <path d="M 95 130 q 15 14 30 0 q 15 -14 30 0 q 15 14 30 0" fill="none" stroke="var(--fg-soft, #999)" stroke-width="1.5"/>
  <text x="140" y="165" text-anchor="middle" style="font-family: var(--serif, serif); font-size: 22px;" fill="var(--fg-soft, #999)">?</text>
  <text x="140" y="215" text-anchor="middle" style="font-family: var(--sans, sans-serif); font-size: 12px; letter-spacing: 1px;" fill="var(--fg-soft, #999)">EXPERT + COUNTING BOARD</text>
  <text x="450" y="60" text-anchor="end" style="font-family: var(--serif, serif); font-size: 20px;" fill="var(--fg, #e6e4df)">147</text>
  <text x="450" y="87" text-anchor="end" style="font-family: var(--serif, serif); font-size: 20px;" fill="var(--fg, #e6e4df)">× 39</text>
  <line x1="360" y1="97" x2="454" y2="97" stroke="var(--fg, #e6e4df)" stroke-width="1.5"/>
  <text x="450" y="120" text-anchor="end" style="font-family: var(--serif, serif); font-size: 20px;" fill="var(--fg, #e6e4df)">1 323</text>
  <text x="450" y="147" text-anchor="end" style="font-family: var(--serif, serif); font-size: 20px;" fill="var(--fg, #e6e4df)">4 410</text>
  <line x1="360" y1="157" x2="454" y2="157" stroke="var(--fg, #e6e4df)" stroke-width="1.5"/>
  <text x="450" y="182" text-anchor="end" style="font-family: var(--serif, serif); font-size: 20px; font-weight: bold;" fill="var(--accent, #059669)">5 733</text>
  <text x="420" y="215" text-anchor="middle" style="font-family: var(--sans, sans-serif); font-size: 12px; letter-spacing: 1px;" fill="var(--fg-soft, #999)">A CHILD&#8217;S PROCEDURE</text>
</svg>
<figcaption style="font-size: 0.85em; color: var(--fg-soft, #999); max-width: 34em; margin: 0.4rem auto 0;">Same numbers, same result. On the left there is nothing to write down: the notation offers no procedure. On the right the representation itself carries the algorithm: digit by digit, carry, shift, add.</figcaption>
</figure>

The Greeks contributed the first escalation, the deductive proof. The second escalation came from India and Baghdad, and it is the one software people carry in their bones: the algorithm.

## The ninth-century refactor

Between the fifth and seventh centuries, Indian mathematicians built the decimal place-value system, with zero as a number in its own right. Brahmagupta wrote down the rules in 628: how zero behaves under addition and multiplication, how to compute with negative quantities (debts, in his framing). It is easy to file this under convenience. It was a compute innovation. Position encodes magnitude, so ten symbols cover all numbers, and the standard multiplication procedure rides directly on that encoding: multiply digit by digit, carry, shift, add. The representation does the heavy lifting; the human executes a loop.

Around 820, in Baghdad's House of Wisdom, al-Khwarizmi wrote two books that named our field twice over. One explained the Indian art of reckoning; the Latinized form of his name gave us "algorithm". The other, the Kitab al-jabr, gave us "algebra", and something more important than the word: a discipline organized around guaranteed procedures. Classify the equation types, then give each type a method that always works. One procedure per problem class, instead of one clever trick per problem.

Europe took its time. Fibonacci imported the Hindu-Arabic system in 1202 with the Liber Abaci, and the abacus professionals fought it for generations; Florence went as far as banning the new numerals in official records in 1299. The system won anyway, for the least romantic reason available: it scaled.

## Trust, amortized

Here is why this belongs in a series about verification. A proof verifies a statement once, for all cases, by checking the inference structure instead of the instances. An algorithm makes a different bargain: verify the procedure once, then execute it as often as you like, on inputs nobody has seen before, by people or machines who don't understand why it works. Correctness gets certified at design time. At run time you only follow steps.

That is the shape of every library function you have ever called. It is also, by volume, the dominant verification tradition of civilization: for every theorem consulted today, billions of algorithm executions run on the amortized trust of a one-time correctness argument. Proof and algorithm have been the two pillars of mathematical reliability ever since, and their reunification (procedures whose correctness is itself proven) is what verified compilers and proof assistants are still working on. This July, a language model closed a convex-optimization problem that had been open since 1996, and the result was accepted because the proof was checked in Lean. The searcher needed no trust at all. The notation carried it.

## The Leibniz dividend

If the Roman-numeral story feels too ancient to generalize, mathematics ran the experiment a second time, with a control group. Newton and Leibniz invented calculus independently, and the priority dispute poisoned British-continental cooperation. The dispute is a footnote. The lesson sits in the notation gap. Leibniz wrote dy/dx and ∫f(x)dx. Newton wrote dots over letters. In Leibniz's notation the chain rule looks like fractions cancelling, which means the notation performs part of the reasoning for you. Britain stuck loyally with Newton's dots and fell behind continental analysis for a hundred years. The theory was identical on both sides of the Channel; the interface was not, and the throughput of an entire scientific culture went with the interface.

Programming-language people recognize all of this on sight, because our field is the industrialization of the insight. A type system that makes illegal states unrepresentable is Brahmagupta's move: push correctness into the representation so the executor can be simpler and still be right. Choosing between two equivalent representations is never neutral. One of them will let a routine procedure do what the other demands an expert for.

## Where your specs still run on Roman numerals

Which brings me to the working question. We currently spend our days writing instructions for a new class of executor: models and agents. The dominant failure mode I see is prompting harder, stacking paragraphs of exhortation onto a representation that fights the task. The ninth-century answer is to change the notation. Give the executor a schema instead of prose wherever structure matters, and make acceptance criteria machine-checkable instead of adjectival. Design the spec so that following it is a mechanical procedure with a verifier at the end; the executor should never have to interpret. I keep one heuristic from this history: if a task needs your most experienced person every single time, the notation is wrong.

The Roman Empire administered the Mediterranean for centuries with numerals that made multiplication expert work, and nobody inside the system found that strange. How much of your backlog is hard only because of the notation it's written in?

---

*The Verification Changelog, part 2 of 5.*  
[← Proof Is a Technology](/posts/proof-is-a-technology/) · [When Physics Was the Test Suite →](/posts/when-physics-was-the-test-suite/)
