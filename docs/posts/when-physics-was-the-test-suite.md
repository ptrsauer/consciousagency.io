*Part 3 of five in **The Verification Changelog**: Five posts reading 2,500 years of mathematics as the release history of one technology, verification, and what that history means for anyone running AI agents unsupervised.*

In 1734, the philosopher George Berkeley published a pamphlet called *The Analyst*, aimed squarely at the mathematics of Newton and Leibniz. His target was the infinitesimal, the vanishing increment *dx* that calculus happily divided by and then discarded as if it had never existed. Berkeley called these quantities "the ghosts of departed quantities," and the jab landed because it was accurate. Nobody could define an infinitesimal. It was nonzero when you needed to divide by it and zero when you needed it gone, sometimes within the same derivation.

It didn't matter. Calculus ran for roughly 150 years on undefined foundations and produced the most successful mathematics anyone had ever seen. Euler alone filled the 18th century with results we still teach, manipulating infinite sums in ways that would fail any modern referee. No collapse. No slow accumulation of nonsense, which is what our intuition about untested systems predicts. The interesting question is why not.

## Physics was the test suite

The era had an external verifier. Celestial mechanics and ballistics: if your calculation was wrong, your prediction failed measurably, against the sky or the cannonball. When Alexis Clairaut used this still-unfounded calculus to predict the 1759 return of Halley's comet and got the perihelion date right to within a month, that was a passing integration test with the whole of Europe watching. The feedback loop was slow, but it was merciless, and it kept the productive front of mathematics honest for a century and a half.

Correctness, in this arrangement, lived with the applications. No definition of the infinitesimal backed it up, no proof about the concepts themselves; the predictions carried the whole weight. I call this **borrowed rigor**: the discipline didn't own its verification, it rented it from physics. And rented verification genuinely works. A hundred and fifty years of it built analysis, mechanics, and most of the mathematical physics we still run on.

But a rental contract has a scope clause. Physics could referee any question of the form "does this calculation match the world?" It could not referee "what *is* a limit?" or "when does this infinite series converge?" Those questions have no experiment. As long as nobody asked them, the gap was invisible.

<figure style="margin: 2rem auto; text-align: center;">
<svg viewBox="0 0 560 290" role="img" aria-label="Map of the questions calculus raises, with the region physics could referee shaded and conceptual questions outside it" style="max-width: 480px; width: 100%; height: auto;">
  <rect x="20" y="25" width="520" height="235" fill="none" stroke="var(--fg, #e6e4df)" stroke-width="1.5"/>
  <text x="36" y="50" style="font-family: var(--sans, sans-serif); font-size: 12px; letter-spacing: 1px;" fill="var(--fg-soft, #999)">EVERY QUESTION CALCULUS RAISES</text>
  <rect x="40" y="105" width="290" height="135" rx="4" fill="var(--accent, #059669)" opacity="0.1"/>
  <rect x="40" y="105" width="290" height="135" rx="4" fill="none" stroke="var(--accent, #059669)" stroke-width="1.5"/>
  <text x="56" y="130" style="font-family: var(--sans, sans-serif); font-size: 12px; letter-spacing: 1px;" fill="var(--accent, #059669)">PHYSICS CAN REFEREE</text>
  <text x="56" y="162" style="font-family: var(--serif, serif); font-size: 15px;" fill="var(--fg, #e6e4df)">Halley&#8217;s comet, 1759 &#10003;</text>
  <text x="56" y="190" style="font-family: var(--serif, serif); font-size: 15px;" fill="var(--fg, #e6e4df)">ballistic arcs &#10003;</text>
  <text x="56" y="218" style="font-family: var(--serif, serif); font-size: 15px;" fill="var(--fg, #e6e4df)">tides, heat, orbits &#10003;</text>
  <text x="440" y="130" text-anchor="middle" style="font-family: var(--serif, serif); font-size: 15px; font-style: italic;" fill="var(--fg, #e6e4df)">what <tspan style="font-style: normal;">is</tspan> a limit?</text>
  <text x="440" y="170" text-anchor="middle" style="font-family: var(--serif, serif); font-size: 15px; font-style: italic;" fill="var(--fg, #e6e4df)">does this series converge?</text>
  <text x="440" y="210" text-anchor="middle" style="font-family: var(--serif, serif); font-size: 15px; font-style: italic;" fill="var(--fg, #e6e4df)">what is dx?</text>
</svg>
<figcaption style="font-size: 0.85em; color: var(--fg-soft, #999); max-width: 34em; margin: 0.4rem auto 0;">Rented verification has a scope clause: physics referees predictions, not concepts. The questions on the right sat outside its jurisdiction for 150 years, unchecked and invisible until Fourier forced them into the open.</figcaption>
</figure>

## All green, still down

Software engineering runs a compressed version of this experiment every week. Cloudflare's global outage of July 2, 2019 is the cleanest public write-up: one new WAF rule, tested, reviewed, deployed through the standard pipeline, and within minutes CPU on every machine in their worldwide network hit 100%, because the rule's regular expression backtracked catastrophically on real traffic. About 27 minutes of global 502s. No test was wrong. Re-running the suite afterwards would produce the same green checkmarks, since the tests asked whether the rule matched what it should match, and it did. Nobody had asked what the match would cost in CPU. The tests verify every case the tests can see. Production asks a question from outside that set.

The failure mode is coverage: a verifier only speaks about the inputs it is shown. Green describes the question set. The system is a different object. Software engineering treats this as a hard-won modern insight. Mathematics ran the same experiment starting around 1800, at civilizational scale.

## The questions physics couldn't referee

In the 19th century, the question set shifted. Joseph Fourier's work on heat conduction, presented in 1807, claimed that essentially arbitrary functions could be written as infinite trigonometric series. That forced the convergence question into the open, and no cannonball trajectory could settle it. The concepts themselves were now the subject, and the external verifier had no jurisdiction there.

The results were embarrassing in a very recognizable way. Augustin-Louis Cauchy, the man leading the new push for rigor, published a theorem in his 1821 *Cours d'analyse* stating that a convergent series of continuous functions has a continuous sum. It is false. Niels Henrik Abel pointed at Fourier series counterexamples in 1826. A published theorem by the era's chief rigorist, wrong, because the underlying notion of convergence was still fuzzy. That is what "tests green, concepts undefined" looks like once the input distribution moves.

The repair took most of the century. Cauchy started it and Karl Weierstrass finished it: the ε-δ definition of the limit, which replaces "infinitely small" with a finite, checkable logical statement. Pedantic-looking, and a precision weapon. With it, Weierstrass constructed his 1872 monster, a function continuous everywhere and differentiable nowhere, and the last informal verifier, geometric intuition, was formally retired. Mathematics stopped renting. It internalized its verification, at the cost of a strictness that working mathematicians of 1750 would have found absurd.

That is the pattern I keep coming back to, verification standards escalating step by step over 2,500 years, and this is its sharpest single episode: an external verifier can cover for missing internal strictness for a very long time, but only inside its own domain. The moment the questions leave that domain, you pay for every definition you skipped, with interest.

The escalation has not stopped. This month a machine-found proof of a problem open since 1996 was accepted for exactly one reason: it checks in Lean. Berkeley would have appreciated that arrangement.

A test suite can be green for years before production asks its question. Calculus was green for 150. In both cases the checks did exactly what checks do. What differed was how long the world took to ask something from outside their jurisdiction. So: which of your green suites is renting its rigor right now?

---

*The Verification Changelog, part 3 of 5.*  
[← Notation Is Compute](/posts/notation-is-compute/) · [The Most Productive Failure →](/posts/the-most-productive-failure/)
