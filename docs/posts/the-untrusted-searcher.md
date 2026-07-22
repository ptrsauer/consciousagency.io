*Part 5 of five in **The Verification Changelog**: Five posts reading 2,500 years of mathematics as the release history of one technology, verification, and what that history means for anyone running AI agents unsupervised.*

In 1976, Kenneth Appel and Wolfgang Haken proved the four color theorem, and mathematics crossed a line it has never stepped back over. Their proof reduced the problem to 1,936 configurations and checked them in about 1,200 hours of machine time on an IBM 370. No human has read that case analysis. No human ever will. The objection at the time was serious, not reactionary: a proof you cannot read is a proof you must take on trust, and trust in a mainframe was not what Euclid had in mind.

What the discipline did over the following fifty years is the best trust story I know, because of its ending. Trust did not migrate to the machines. It became unnecessary.

## Ninety-nine percent certain

The four color proof was a warning shot about machines. The classification of finite simple groups was a warning shot about humans: tens of thousands of journal pages, spread over roughly 500 articles by about a hundred authors, declared complete in the 1980s with a gap that took until 2004 to patch. Nobody alive has verified it end to end; a full reading would take more than a career.

Then Thomas Hales submitted his 1998 proof of the Kepler conjecture, 300 pages of mathematics plus gigabytes of code, to the Annals of Mathematics. The journal assigned a panel of twelve referees. After four years they gave up and delivered the strangest verdict in the history of peer review: 99% certain the proof is correct, unable to certify the rest. In most fields, 99% is a triumph. In mathematics it is a confession.

Hales took the confession seriously and spent the next decade on Flyspeck, completed in 2014: a formal verification of the entire proof, every inference checked by machine down to the axioms. The panel had been competent. The artifact had simply outgrown the institution that reviews artifacts. Peer review is trust in people, their training, their attention on a given afternoon. A proof assistant concentrates all required trust into a kernel of a few thousand lines of code that you audit once. Trust the kernel, and the author's reputation stops being load-bearing.

## The searcher stops mattering

Once the checker carries the trust, watch who gets to search. In December 2020, Peter Scholze, a Fields medalist, asked the Lean community to formally verify one of his own recent theorems, because he was not sure of it himself. The Liquid Tensor Experiment verified the hard core of the proof within about half a year; the full formalization ran until 2022. The proof held. In 2024, AlphaProof, together with AlphaGeometry 2, reached silver medal level on International Mathematical Olympiad problems, 28 of 42 points, AlphaProof's solutions expressed in Lean. And this July, a frontier LLM produced a solution to a problem in convex optimization that had been open since 1996, formally verified in Lean.

Nobody asked the obvious questions about that last result. Did the model understand the problem? Was it hallucinating? Irrelevant. The kernel accepted the proof, and a verified proof from an unreliable source is exactly as true as a verified proof from Gauss. This series has been tracking one question since Euclid's original move, "why should you believe me?", and here is where 2,300 years of escalating verification standards land: the checking has become so hard that the searcher needs no credentials at all. No track record, not even a mind.

## The verifier gradient

I work with coding agents daily, and the question there is the question of this whole series. How much unsupervised runway you can give a searcher is a function of what checks its output, and of nothing else. I call this the verifier gradient: an agent's autonomy budget scales with the hardness of its verifier.

The gradient runs from formal artifacts at the top (proof kernels, type checkers, compilers), through deterministic tests, then observable metrics, down to human judgment at the bottom. Each rung down, cut the budget. An agent refactoring under a strict type system and an exhaustive test suite can run overnight unattended, because anything it breaks shows up as a red build by morning. An agent producing a strategy document that a tired human will skim gets minutes of leash, no matter how good the model is.

<figure style="margin: 2rem auto; text-align: center;">
<svg viewBox="0 0 560 250" role="img" aria-label="The verifier gradient: autonomy budget shrinking as the verifier weakens from formal proof down to human judgment" style="max-width: 480px; width: 100%; height: auto;">
  <text x="235" y="38" text-anchor="end" style="font-family: var(--sans, sans-serif); font-size: 12px; letter-spacing: 1px;" fill="var(--fg-soft, #999)">VERIFIER</text>
  <text x="255" y="38" style="font-family: var(--sans, sans-serif); font-size: 12px; letter-spacing: 1px;" fill="var(--fg-soft, #999)">AUTONOMY BUDGET &#8594;</text>
  <g style="font-family: var(--serif, serif); font-size: 15px;">
    <text x="235" y="80" text-anchor="end" fill="var(--fg, #e6e4df)">proof kernel, types</text>
    <rect x="255" y="62" width="285" height="26" rx="3" fill="var(--accent, #059669)" opacity="0.9"/>
    <text x="235" y="128" text-anchor="end" fill="var(--fg, #e6e4df)">deterministic tests</text>
    <rect x="255" y="110" width="195" height="26" rx="3" fill="var(--accent, #059669)" opacity="0.6"/>
    <text x="235" y="176" text-anchor="end" fill="var(--fg, #e6e4df)">observable metrics</text>
    <rect x="255" y="158" width="110" height="26" rx="3" fill="var(--accent, #059669)" opacity="0.38"/>
    <text x="235" y="224" text-anchor="end" fill="var(--fg, #e6e4df)">human judgment</text>
    <rect x="255" y="206" width="40" height="26" rx="3" fill="var(--accent, #059669)" opacity="0.22"/>
  </g>
</svg>
<figcaption style="font-size: 0.85em; color: var(--fg-soft, #999); max-width: 34em; margin: 0.4rem auto 0;">The verifier gradient. Each rung down the verification gets softer and the unsupervised runway shorter, and the dangerous rung is the middle one, where a weak verifier launders trust into something that looks like evidence.</figcaption>
</figure>

The trap sits in the middle of the gradient. A weak verifier is worse than no verifier, because no verifier at least keeps you honest: you know you are trusting the searcher, and you review like it. A weak verifier launders that trust into something that looks like evidence. I have watched a green test suite wave a change into production that took the service down within the hour; the tests verified precisely the cases the tests could see. Mathematics ran that experiment at scale once. Calculus operated for 150 years on foundations Bishop Berkeley rightly mocked in 1734 as "ghosts of departed quantities", verified only by physics, and the cracks stayed invisible exactly until questions arrived that physics could not referee.

So before raising any agent's autonomy, one concrete question: what, precisely, would catch it being wrong? If the honest answer is "me, skimming", the budget is zero and the model's brilliance changes nothing. Mathematics needed 2,300 years to stop trusting the searcher. Your agents arrive untrusted on day one. All that's left to build is the thing they answer to.

---

*The Verification Changelog, part 5 of 5.*  
[← The Most Productive Failure](/posts/the-most-productive-failure/)
