---
title: Proof Is a Technology
date: 2026-07-22
order: 1
slug: proof-is-a-technology
description: Babylon verified by application, the Greeks verified the inference. 2,500 years later, that fork decides how much you can trust an unsupervised AI agent.
---

*Part 1 of five in **The Verification Changelog**: Five posts reading 2,500 years of mathematics as the release history of one technology, verification, and what that history means for anyone running AI agents unsupervised.*

Somewhere around 1800 BC, a Babylonian scribe pressed a list of Pythagorean triples into wet clay. We call that tablet Plimpton 322, and it predates Pythagoras by roughly a thousand years. The same scribal culture solved quadratic equations and did its arithmetic in base 60, which is why your clock still slices hours into 60 minutes. Egyptian surveyors re-measured the fields after every Nile flood; geometry means land-measurement, literally. These were serious computational cultures, and they were good.

What they did not have was proof. And here is the uncomfortable part: they did not miss it. Their verification standard was application. The grain got distributed correctly, or it didn't. The pyramid stood, or it didn't. Knowledge came as recipes ("do this, then that, it works"), and every successful use was one more confirming instance. That standard is not primitive. Most of software engineering runs on it today; we just call the confirming instances "passing tests" and "works in production."

But it checks instances. And instances are all it checks.

## The Greek fork

Starting with Thales of Miletus, around 600 BC, Greek mathematicians asked a question the recipe tradition had no slot for: does this hold always, and how could I know that without checking every case? Their answer was the deductive proof, a chain of forced steps from explicitly stated assumptions. Euclid's Elements packaged the method around 300 BC: a handful of axioms, hundreds of theorems, each resting only on what came before. It stayed the standard textbook of rigorous thinking for over two thousand years, a support window no software vendor will ever match.

The shift is easy to under-read. Proof is not "checking more thoroughly." Thorough checking is still instance work, and infinitely many instances stay open no matter how diligent you are. Proof moves verification to a different place altogether: away from the results, onto the structure of the inference. What you check is whether each step was forced. Finitely many steps, each one mechanically checkable, and suddenly a claim about infinitely many cases has a finite verification procedure. That is the entire trick, and it may be the most consequential piece of intellectual technology anyone has ever shipped.

## The diagonal incident

The new technology got its stress test almost immediately, and from inside the house. The Pythagoreans taught that everything is number, where "number" meant ratios of whole numbers. Then one of their own proved that the diagonal of a unit square cannot be written as any such ratio: the square root of two, √2, is irrational. Doctrine said one thing. A short chain of forced steps said the opposite.

<figure style="margin: 2rem auto; text-align: center;">
<svg viewBox="0 0 300 270" role="img" aria-label="Unit square with diagonal of length square root of two" style="max-width: 260px; width: 100%; height: auto;">
  <!-- Pythagoras-Dreieck dezent schattiert -->
  <polygon points="60,210 240,210 240,30" fill="var(--accent, #059669)" opacity="0.08"/>
  <!-- Quadrat -->
  <rect x="60" y="30" width="180" height="180" fill="none" stroke="var(--fg, #e6e4df)" stroke-width="2"/>
  <!-- rechter Winkel unten rechts (dort schliessen die beiden Katheten) -->
  <path d="M 222 210 L 222 192 L 240 192" fill="none" stroke="var(--fg-soft, #999)" stroke-width="1.5"/>
  <!-- Diagonale -->
  <line x1="60" y1="210" x2="240" y2="30" stroke="var(--accent, #059669)" stroke-width="2.5"/>
  <!-- Labels: Katheten unten + rechts, Hypotenuse oberhalb der Linie -->
  <text x="150" y="234" text-anchor="middle" style="font-family: var(--serif, serif); font-size: 17px;" fill="var(--fg, #e6e4df)">1</text>
  <text x="258" y="126" text-anchor="middle" style="font-family: var(--serif, serif); font-size: 17px;" fill="var(--fg, #e6e4df)">1</text>
  <text x="126" y="102" text-anchor="middle" style="font-family: var(--serif, serif); font-size: 18px; font-style: italic;" fill="var(--accent, #059669)">&#8730;2</text>
</svg>
<figcaption style="font-size: 0.85em; color: var(--fg-soft, #999); max-width: 34em; margin: 0.4rem auto 0;">Two sides of length 1, so the diagonal comes out at &#8730;2 by the Pythagorean theorem: a length you can draw with a ruler, but provably never write as a ratio of whole numbers.</figcaption>
</figure>

The remarkable part is what the community did next. They accepted the result. The ship-drowning legend around the discoverer is centuries younger and probably invented; what actually survives is the result worked into the canon, all the way to a full theory of irrational ratios in Euclid's Book X. A proof had contradicted the official worldview of the very school that produced it, and the proof won. That is the founding precedent of the whole enterprise: once the inference structure checks out, seniority, doctrine and vibes have no vote.

Before, a mathematical claim was exactly as trustworthy as the person or tradition behind it. After, the claim carried its own verification with it. You could distrust the author completely and still be forced to accept the theorem.

## A technology with release notes

I find it more productive to treat proof as a technology with a version history. Version 1 was Greek deduction. Islamic algebra shipped a parallel branch, the guaranteed procedure, verified once and executed forever (the next essay is about that branch). Every major upgrade since has followed the same pattern: the community catches its current verifier accepting something it shouldn't, then tightens the standard. The 19th century replaced geometric intuition with ε-δ definitions after intuition started certifying nonsense. After Russell found a contradiction sitting in the foundations, the early 20th century formalized the axioms themselves. And since about 2020 the frontier is machine-checked proof: systems like Lean that verify every inference step down to the axioms, with no human patience required. This essay is the first of five walking that changelog, because the later releases are where things get uncomfortably relevant.

This July, GPT-5.6 closed a convex optimization problem that had been open since 1996. It took a human expert a year of framing and a carefully built prompt to steer it there, and nobody trusts the model's reasoning trace anyway. What made the result reportable was the accompanying proof, formally verified in Lean. A person aimed, a machine searched, a machine checked, and the check carries all the trust. When verification is hard enough, the searcher no longer needs to be trustworthy. Not even human.

That sentence is the reason this history stopped being a hobby topic in 2026. Anyone running AI agents unsupervised gets output whose derivation nobody watched, at a volume nobody can re-derive. The default response is Babylonian: verify by application. Run it, watch the tests go green, ship. Those are instance checks, from the tradition the Greeks made optional two and a half millennia ago. The Greek response, checking the structure of what was done rather than sampling its outputs, is the one our tooling barely supports yet.

Babylon got well over a thousand years out of verification by application, and the pyramids its neighbors built still stand. The Greeks upgraded anyway, because a single diagonal broke their trust in the old standard. What's our diagonal?

*Sources on the July 2026 result: [Hacker News discussion](https://news.ycombinator.com/item?id=48957779) and the [r/math thread](https://old.reddit.com/r/math/comments/1uxj3cy/after_openais_cdc_proof_announcement_gpt56_used_a/).*

---

*The Verification Changelog, part 1 of 5.*  
[Notation Is Compute →](/posts/notation-is-compute/)
