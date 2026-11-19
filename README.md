# Priori-tree

Priori-tree is a generalized prioritization system: for any list and comparison operator, run the pairwise permutations, store the votes, tally — the output list is in a superior order than sizing individual items, because discernment between two items is easy (for humans and LLMs) while absolute sizing is not.

The comparator class is both human AND LLM — both vote through the same vote interface; the tally is a pure function of the stored votes.

> Priori-tree is a generalized prioritization system based on the concept that LLM and Humans are great at discerning the difference between two items but not great at sizing an item. That is a simplification. Consider: a human is great at determining that a basketball is larger than a grapefruit. But not great as identifying the exact dimensions of a grapefruit or a basketball. By taking a list and running through the pairwise permutations for any given comparision operator. Storing the votes, then tallying. we get a list out that is in a superior order than trying to size individual items.
>
> — the collaborator's Q-purpose ruling, 2026-11-19 (verbatim)

## Architecture

All four forms, one layered architecture, library-first (the collaborator's Q-setup-arch ruling, 2026-11-19):

- **Library — `src/prioritree`:** the pure-logic core (items, comparison operator, pair scheduling, votes, tally) at the bottom of the stack. Data plane = pure logic: stateless scoring/ranking core, votes are data in/out, no DB at birth.
- **CLI:** wraps the core.
- **API service (FastAPI):** serves the core.
- **Web app:** fronts the service (the human comparator's vote surface).

## Status at birth

The setup builds the skeleton only — the core library is the product effort's first increment. This tree carries the skeleton: the `src/prioritree` namespace, the smoke test, and the tooling floor (uv, ruff, pyright, pytest; the Makefile floor `dev`/`test`/`lint`/`typecheck`). CI is deferred — git hooks and local gates stand in at birth.
