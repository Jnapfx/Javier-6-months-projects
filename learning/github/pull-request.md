
# Weekly Report – Pull Request Workflow

### Objective
This week, I learned how to create and manage a **Pull Request (PR)** on GitHub. The goal was to understand the collaborative workflow where changes are proposed, reviewed, and merged into a main project repository.

---

### Steps Completed

1. **Repository Setup**
   - Created a local directory and cloned the remote GitHub repository.
   - Verified the connection between the local machine and the remote repository.

   ```bash
   git clone https://github.com/Jnapfx/Zahra-DAE-projects.git
   cd Zahra-DAE-projects
   ```

2. **File Creation and Commit**
   - Added a test file: `testing-pull-request.md`.
   - Staged and committed the changes with a clear commit message.

   ```bash
   git add testing-pull-request.md
   git commit -m "testing pull request"
   git push --all
   ```

3. **Pull Request Creation**
   - Opened a Pull Request from the contributor’s branch (`zahrashefa318:main`) to the owner’s repository (`Jnapfx:main`).
   - GitHub automatically detected the new commit and displayed the proposed change.

4. **Review and Merge**
   - The Pull Request was reviewed and discussed in the **conversation tab**.
   - The repository owner (Jnapfx) confirmed and merged the contribution into the `main` branch.
   - The status changed from **Open** to **Merged**, showing `+1 -0` which indicated **one line/file added** and **no deletions**.

5. **Collaboration Evidence**
   - Screenshots captured the entire process:
     - PR creation.
     - Review comments.
     - Successful merge.

---

### Key Learnings

- **Pull Requests** allow structured collaboration: contributors suggest changes, while maintainers review and approve them.
- GitHub provides clear visual indicators of changes (`+ additions / - deletions`).
- PR conversations encourage communication between team members before merging.
- This workflow simulates real-world teamwork in software development, ensuring quality control and version tracking.

---

### Reflection

At the beginning, I focused on learning the technical commands (`git add`, `git commit`, `git push`). Later, I understood the collaborative value of Pull Requests: they are not just about pushing code but about **communication, review, and approval**.

By completing this exercise, I gained confidence in contributing to repositories and learned the essential GitHub workflow that professional development teams use every day.

---

📅 Report Date: 2025-09-11
