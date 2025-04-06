
# 📊 State Transition Diagrams - Personalised Meal Planner

All diagrams use `stateDiagram

---

## 1. 👤 User Account

```mermaid
stateDiagram-v2
    [*] --> Registered
    Registered --> Active: Email Verified
    Registered --> Suspended: Violation Detected
    Active --> Suspended: User Misconduct
    Active --> Deleted: User Deletes Account
    Suspended --> Active: Admin Reinstates
    Suspended --> Deleted: Admin Deletes Account
    Deleted --> [*]
```

---

## 2. 🥗 Meal Plan

```mermaid
stateDiagram-v2
    [*] --> Draft
    Draft --> Published: User Saves Plan
    Published --> Updated: User Edits Plan
    Updated --> Published: User Saves Edits
    Published --> Archived: Plan Expired or Archived
    Archived --> [*]
```

---

## 3. 📋 Recipe

```mermaid
stateDiagram-v2
    [*] --> Created
    Created --> Reviewed: User Submits Recipe
    Reviewed --> Approved: Admin Approves
    Reviewed --> Rejected: Admin Rejects
    Approved --> Archived: No Longer Recommended
    Rejected --> Archived
    Archived --> [*]
```

---

## 4. 🛒 Grocery List

```mermaid
stateDiagram-v2
    [*] --> Generated
    Generated --> Modified: User Edits List
    Modified --> Saved: User Saves List
    Saved --> Archived: After Meal Plan Completion
    Archived --> [*]
```

---

## 5. 🍽️ Meal Preference

```mermaid
stateDiagram-v2
    [*] --> Set
    Set --> Updated: User Updates Preferences
    Updated --> Set: Save Changes
```

---

## 6. 💳 Subscription

```mermaid
stateDiagram-v2
    [*] --> Trial
    Trial --> Active: User Subscribes
    Active --> Suspended: Payment Failed
    Suspended --> Active: Payment Resolved
    Active --> Canceled: User Cancels
    Canceled --> [*]
```

---

## 7. 🧬 Dietary Profile

```mermaid
stateDiagram-v2
    [*] --> Incomplete
    Incomplete --> Completed: User Provides Info
    Completed --> Updated: User Updates Profile
    Updated --> Completed: Save Updates
```

---

## 8. 📦 Order (Optional)

```mermaid
stateDiagram-v2
    [*] --> Created
    Created --> Paid: Payment Successful
    Paid --> Delivered: Delivery Completed
    Paid --> Canceled: User Cancels Before Delivery
    Delivered --> Archived
    Canceled --> Archived
    Archived --> [*]
```



