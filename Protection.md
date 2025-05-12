# PROTECTION.md

## Branch Protection Rules for `main`

We have enforced the following rules on the `main` branch to maintain code quality and team collaboration:

### 1. Require Pull Request Reviews
Only reviewed changes are allowed to be merged into `main`. This prevents unreviewed code from affecting production.

### 2. Require Status Checks
CI workflows (such as automated testing) must pass before merging. This ensures that the code meets quality and performance standards.

### 3. Disable Direct Pushes
Direct pushes are disabled to enforce the use of pull requests. This helps maintain a proper audit trail and encourages code reviews.

---

These rules promote:
- Team collaboration
- Cleaner Git history
- Reduced risk of bugs reaching the production environment

![image](https://github.com/user-attachments/assets/28d91b85-e690-496f-b570-dcd748d36c64)

