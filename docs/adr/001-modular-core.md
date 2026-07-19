# ADR-0001: Modular Core

## Status

Accepted

## Context

Alan is intended to evolve into a flexible assistant platform.

A monolithic architecture would make future extensions difficult and tightly couple all features together.

## Decision

Alan will use a modular architecture based on a central Core and independent components. The Core will coordinate capabilities but will not directly implement domain-specific actions.

## Consequences

Pros:

- easier extension of the system;
- replaceable components;
- clearer separation of responsibilities.

Cons:

- higher initial complexity;
- more design work required before implementation.