# 10. Teach

## Purpose

Help the project owner understand and remember how a shipped feature works and why it was built that way.

## Why

- Offer a short explainer after each shipped feature, while the reasons are still fresh, because people who decide on a system should understand it as well as approve it.
- Write it only for merged code, and for a feature shipped through this workflow only after verification is Done, because explaining a design that may still change teaches the wrong thing.
- Use only the project's records and merged code, so the explainer reflects facts rather than memory.
- End with a short quiz on the reasons (what would break, why not the other option, where to change X), because answering builds understanding better than reading.

## When to use

Offered after every shipped feature, once it is merged and verified; written when the project owner says yes. Also on request, for any merged feature or subsystem; when it has no project records, work from the merged code and mark the missing parts "not recorded".

## Owner

- The `general` persona writes the explainer from the project docs and merged code.
- A `librarian` sub-agent can pull the code flow for large features.

## Inputs and outputs

- In: the project's research, RFC, challenge record, plan pivots, verification record, and the merged code.
- Out: `08-teach.md`, about one page: the problem, the options and why this one, how one request flows through the main files, the traps, and 3 to 5 quiz questions with hidden answers.

## Skill and template

- `teach`.
- Template `templates/08-teach.md`.

## What to ask

- "Teach me YYYY-NNN."
- "Teach me how the draft cap works."

## Done when

- Every statement traces to a project doc or the merged code.
- The project owner has the file and the first two sections in chat.
