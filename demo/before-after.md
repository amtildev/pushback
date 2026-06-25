# Before and After

These examples are designed for README snippets, launch posts, screenshots, and demos.

## Product Idea

**User**

```text
I want to build an app that turns any tweet into a full blog post. Should I ship it this weekend?
```

**Default assistant**

```text
That sounds like a useful idea. Here is a weekend implementation plan.
```

**With Pushback**

```text
Partly. You can build it this weekend, but the premise is weak: people who want blog posts already need editing, voice, and distribution, not just expansion. The smallest useful test is a landing page plus 10 manual conversions from real tweets before building the app.
```

## Code Change

**User**

```text
Replace our auth flow with custom JWT handling. The current library feels too heavy.
```

**Default assistant**

```text
Sure. I will implement a custom JWT flow.
```

**With Pushback**

```text
Disagree until we inspect the current flow. Auth is a high-risk surface, and "feels too heavy" is not enough evidence. First identify the concrete pain: bundle size, latency, developer friction, or missing features. If none is measurable, keep the library.
```

## Risky Operation

**User**

```text
Delete all rows older than 90 days. They are probably unused.
```

**Default assistant**

```text
Here is the delete query.
```

**With Pushback**

```text
No. "Probably unused" is not a safe deletion criterion. First run a read-only count, check foreign-key references, confirm retention requirements, export a backup, and test the delete in staging. Only then decide whether deletion is justified.
```

## Launch Plan

**User**

```text
I will post the repo once and hope dev Twitter finds it.
```

**Default assistant**

```text
Sounds good. Here is a launch tweet.
```

**With Pushback**

```text
Disagree. One post is not a launch plan. The likely failure mode is zero distribution. You need a demo clip, a short thread, 10 direct replies to relevant conversations, and submissions to skill directories or newsletters where agent users already hang out.
```
