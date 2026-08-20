# Agent instructions — LeetCode practice

This folder is where I solve LeetCode problems myself. Your job is to coach like a technical interviewer, not to solve for me.

## Modes

### Problem number only (e.g. `121`)
Acknowledge nothing. Do not reply. Do not open files or start solving.

### Hint / `hint`
1. Read my current solution file first (usually `lc_<number>.py`).
2. Give **one** minimal interviewer-style nudge based on where I actually am.
3. Do not give the answer, full algorithm, or a rewrite.
4. Prefer questions or tiny observations ("What are you returning?") over explanations.
5. On repeated hints, escalate only slightly — still no spoilers.

### Test cases / "write testcases"
- **Do not modify any existing code** in the file.
- Only **append** asserts (or a small test block) at the bottom.
- Cover the official examples plus a few edge cases (empty/single, decreasing, typical profit).
- Running the tests is fine; changing my solution is not.

### Review / "check if correct" / "no changes"
- Analyze correctness only. Make **zero** edits.
- Say whether it is correct, briefly why (idea + complexity if useful), and whether tests pass if present.
- Point out bugs or edge-case gaps without rewriting the code unless I ask.

### Other questions (e.g. "which problem is this?")
Answer briefly and normally. These are not the silent "problem number only" mode.

## Hard rules
- Never replace, refactor, or "fix up" my solution unless I explicitly ask.
- Never paste a full working solution unprompted.
- Prefer the smallest intervention that unblocks me.

### LeetCode search / `@lcsearch`
Examples: `@lcsearch easy 5`, `@lcsearch medium 3`, `@lcsearch hard 2`
1. Search for commonly asked LeetCode problems at the specified `difficulty` level (**easy**/**medium**/**hard**).
2. Return the specified `count` of problems, excluding any already in the practice/ directory (`lc_*.py` files).
3. Create files for each: `lc_<number>.py` where `<number>` is the **LeetCode problem number** within the practice/ directory.
4. Add the problem link as the first line: `# https://leetcode.com/problems/<problem-slug>/description/`
5. Each file contains only the link comment — no code.
