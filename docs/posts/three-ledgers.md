In May 2026, Uber's COO said the quiet part out loud. After 95% of Uber's engineers had adopted AI coding tools and the company had burned through its entire annual AI budget in four months, Andrew Macdonald admitted: *"It's very hard to draw a line between one of those stats and 'Okay, now we're actually producing 25% more useful consumer features.'"* Uber capped spending at [$1,500 per engineer per month](https://techcrunch.com/2026/06/02/uber-caps-employee-ai-spending-after-blowing-through-budget-in-four-months/).

The story traveled fast, usually as a cautionary tale: adoption is high, value is unproven, rein it in. I think that reading is wrong. Or more precisely: it books three very different kinds of value onto a single ledger and then acts surprised when the ledger disappoints.

Around the same time, the research organization METR reported something quietly remarkable. It had to [abandon its randomized-controlled-trial design](https://metr.org/blog/2026-02-24-uplift-update/) for measuring AI coding productivity, because developers refuse to work without AI. Not permanently, not on principle. They refuse *temporarily, for a paid study*. The control group has structurally eroded.

Both data points usually get filed under "AI productivity is in trouble." I read them differently: they are a story about how we account for value, not about whether it exists. I keep three separate ledgers.

## Ledger 1: Developer experience

Take the METR finding and read it as an economist would. When people decline paid study participation rather than give up a tool, that is revealed preference, the strongest evidence format there is. Whatever the productivity statistics say, working with AI assistance feels so much better that going back is a downgrade nobody accepts voluntarily. Even for money.

The business consequence has nothing to do with feature velocity: AI tooling went from differentiator to hygiene factor in under two years. You no longer provide it to go faster. You provide it because not providing it costs you people, and replacing a senior engineer runs one to two annual salaries once you count search, ramp-up and lost context. If your tooling budget is smaller than one avoided departure, this ledger alone is already positive.

This value never shows up in a feature-output metric. It shows up in retention curves and recruiting funnels, exactly where nobody looks when asking "what did the AI budget buy us?"

(Yes, there is a darker reading of the same data point: dependency, skill atrophy. It deserves its own essay. Note, though, that it doesn't change the budget math. Once a tool is the expected standard, withholding it is not an available move.)

## Ledger 2: Capability expansion

The second ledger is the one Macdonald's metric cannot see, by construction. "25% more useful consumer features" assumes AI contributes more of the same, faster. But a substantial share of what AI enables are features that could not have been built before: document-intelligence pipelines, conversational interfaces over domain data, agents that watch and act.

These features have a peculiar accounting property. They never appear as an *increase* in feature velocity, because before AI they couldn't even enter the backlog. The counterfactual isn't "shipped slower." It's "never proposed." Measuring them with a velocity ruler is a category error, like judging electricity by how much faster it made candle production.

This ledger doesn't need to be faster. It needs to be possible. Its currency is new product surface.

## Ledger 3: Efficiency

And yes, the third ledger, the one everybody stares at: speed, capacity, quality. Here honesty is due. The mid-2026 evidence is genuinely mixed. Self-reported gains keep climbing ([METR's respondents](https://metr.org/blog/2026-05-11-ai-usage-survey/) report 3x speed and predict more), measured value gains sit much lower, and a study of 300,000+ verified AI-generated commits found [over 100,000 introduced issues](https://arxiv.org/html/2603.28592v2) still alive months later. Security pass rates of generated code have been [stuck around 55%](https://www.veracode.com/blog/spring-2026-genai-code-security/) for a year. That's a training problem, not a capability problem, and it won't fix itself with the next model generation.

So the honest position: efficiency gains are real in specific, verifiable use cases and absent in others, and most organizations (mine included) cannot yet say in advance which is which. This ledger needs measurement discipline. Baselines before rollouts. Outcome metrics rather than activity proxies. And the humility to let the answer be "not here, not yet."

## Why the ledgers must not be merged

The Uber story is what happens when all three ledgers get booked onto ledger 3. The tell is the incentive design: Uber ranked teams on a leaderboard by tool usage. Goodhart's law with a budget line. The moment consumption becomes the target, consumption is what you get, and the missing "value link" may say more about the incentive than about the technology.

The governance failure was not the cap. Caps are ordinary financial hygiene; every organization caps cloud spend, and a spending guardrail on inference tokens is no different. The failure was rewarding consumption and then being surprised that consumption didn't correlate with outcomes. Cap as backstop: sound. Consumption as KPI: the wrong turn.

There is a subtler trap on the cost side. A cap treats the symptom (spend) rather than the cause (wasteful usage patterns). Long-lived agent sessions, for instance, re-bill their entire accumulated context on every turn, so costs grow roughly quadratically with session length, and the same work done in scoped, fresh sessions can cost orders of magnitude less. Tooling that makes efficient usage the default beats both the cap and the appeal to discipline. Structure beats willpower, in cost management as everywhere else.

## The maintenance corollary

One more reframe, because it follows directly. A widely shared line this summer warned that if you write code twice as fast, you had better halve your maintenance costs, or you're signing up for permanent debt servitude. Dramatic. And it dresses up ordinary capacity planning as a doom condition.

If you double your engineering output, whether by hiring or by AI, you must scale the share of capacity you invest in maintenance accordingly. Nobody frames a doubled team as "debt servitude"; they plan run/change ratios. The same applies to AI-augmented output, with one honest asterisk. New hires maintain their own code and carry its context. AI output grows the code base while human context stays flat, so the maintenance share needs to be deliberately *higher*. Or maintenance itself needs to scale with AI.

Which it can. The properties that make AI code cheap to produce also make AI remediation tractable: static analyzers and dependency scanners provide machine-checkable verifiers, and verifier-gated agentic loops can work down exactly the debt class that AI generation creates most, the mechanical 90%. Not uniformly (access-control and design flaws have no scanner and still need humans), but enough to restore the symmetry. If AI increases the flow of code, let AI also increase the flow of maintenance, gated by deterministic checks.

## Keeping the books

Developer experience is a hygiene factor now; its value shows up in retention, and it's binary: you provide the tools or you leak talent. Capability expansion is invisible to velocity metrics by construction; judge it by new product surface. Efficiency is real but conditional; measure it per use case, with baselines, and never with consumption leaderboards.

Cap your spend like you cap your cloud bill, as a backstop. Plan the maintenance share deliberately and let verifier-gated loops carry part of it. And next time someone cites the Uber story as proof that AI coding doesn't pay, ask them two questions: which ledger did you look at, and who designed the incentive?
