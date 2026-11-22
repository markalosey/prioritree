# THE COMPOSITION — INCREMENTS + PLACEMENTS + APPLICATION ORDER (part c of the set)

## INCREMENTS

- **synthesize/ux-design** — owner togo · gate G-UX-DESIGN-BRIEF · stage pipeline · steps: [synthesize (semantic, togo, gate)]
- **build/service** — owner jikko · gate G-SERVICE · stage build · steps: [build (semantic, jikko, gate); floor-green (deterministic: make dev && make test && make lint && make typecheck at the prioritree root, gate)] · pipeline: {brief_gate: G-SERVICE-BRIEF, packets: [discover/service, understand/service], synthesize_increment: synthesize/service}
- **build/web** — owner jikko · gate G-WEB · stage build · steps: [build (semantic, jikko, gate); floor-green (deterministic: the make floor, gate)] · pipeline: {brief_gate: G-WEB-BRIEF, packets: [discover/web, understand/web], synthesize_increment: synthesize/web}
- **build/lifecycle** — owner jikko · gate G-LIFECYCLE · stage build · steps: [build (semantic, jikko, gate); targets-green (deterministic: the make floor + the lifecycle targets' live read-backs, gate)] · pipeline: {brief_gate: G-LIFECYCLE-BRIEF, packets: [discover/lifecycle, understand/lifecycle], synthesize_increment: synthesize/lifecycle}
- **close/retro** — owner shinko · gate G-CLOSE · stage close · steps: [retro (semantic, hansei, assessment); records-synthesis (semantic, togo, assessment); records-landing (semantic, shinko, assessment); done-call (semantic, shinko, assessment)]

## UNGATED PACKETS (placements — shinko dispatches; evidence under .junro/evidence/Q-ux-surface/)

- **THE CENSUS (FIRST, findings unassumed)**: census/ground (tansa: the existing FastAPI server, the tech notes, the current web state) · census/error-shape (shindan: the existing API's current error shape — the ThreePart gap map, R5's census clause) · census/mechanism (rikai: how the existing server fronts the core's five ops today)
- **THE DESIGN LANE (after the census)**: design/flows (suisen: the UX flows) · design/cqrs-mapping (keisan: the CQRS op-mapping + the HTMX wire's lanes, cited back to R2) · design/presentation (suisen: the tally presentation) · design/adversarial (hyoka: the design drafts attacked) · design/blind-walk (moho: the designed flows walked blind)
- **PER-UNIT LEGS**: discover/<unit> (tansa) + understand/<unit> (rikai) before each brief · validate/<unit> (kensho) at each build gate

## APPLICATION ORDER (the engine's mechanics — the composition model)

1. Opening: add-gate G-COMPOSITION, G-UX-DESIGN-BRIEF, G-CLOSE; compose-stage pipeline/build/close; add-increment synthesize/ux-design, close/retro → the collaborator validates → the census fires.
2. The build units ride the build-add at their turns (service first — the web fronts it; then web; lifecycle when the service stands): each build-add auto-stamps synthesize/<unit> + G-<UNIT>-BRIEF; the rich build gates mint before the adds; no build dispatch until its brief gate is green. Units beyond the ruled set compose at their turns as the design/census earn them.
