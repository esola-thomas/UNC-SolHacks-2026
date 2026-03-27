---
name: "\U0001F393 Certification Voucher Submission"
about: Submit your completed Copilot Learning Lab for a Microsoft Certification voucher
title: ''
labels: ''
assignees: ''

---

body:
  - type: markdown
    attributes:
      value: |
        ## 🎟️ Microsoft Certification Voucher Submission

        Complete this form after finishing the Copilot Learning Lab exercises.
        Vouchers are awarded **first come, first served** — limited quantity available!

  - type: input
    id: full-name
    attributes:
      label: Full Name
      description: "Your full name as it appears in university records."
      placeholder: "e.g., Jane Doe"
    validations:
      required: true

  - type: input
    id: email
    attributes:
      label: UNC Email Address
      description: "Must be a valid @unc.edu or @cs.unc.edu email."
      placeholder: "e.g., janedoe@unc.edu"
    validations:
      required: true

  - type: input
    id: github-username
    attributes:
      label: GitHub Username
      description: "Your GitHub username (we'll verify your fork)."
      placeholder: "e.g., janedoe"
    validations:
      required: true

  - type: input
    id: fork-url
    attributes:
      label: Forked Repository URL
      description: "Paste the URL of YOUR fork of the UNC-SolHacks-2026 repo."
      placeholder: "https://github.com/YOUR_USERNAME/UNC-SolHacks-2026"
    validations:
      required: true

  - type: dropdown
    id: certification
    attributes:
      label: Preferred Certification Exam
      description: "Which Microsoft certification voucher are you requesting?"
      options:
        - "AZ-900: Azure Fundamentals"
        - "AI-900: Azure AI Fundamentals"
        - "DP-900: Azure Data Fundamentals"
        - "SC-900: Security, Compliance, and Identity Fundamentals"
        - "No preference"
    validations:
      required: true

  - type: checkboxes
    id: exercises-completed
    attributes:
      label: Exercises Completed
      description: "Check the exercises you completed in your fork. **You must complete at least 3 exercises to qualify.**"
      options:
        - label: "01 — Autocomplete (completed functions with Copilot)"
          required: false
        - label: "02 — Writing Tests (wrote tests for Calculator class)"
          required: false
        - label: "03 — Refactoring (refactored messy code with Copilot)"
          required: false
        - label: "04 — Documentation (generated docstrings with Copilot)"
          required: false
        - label: "05 — Debugging (found and fixed all 5 bugs)"
          required: false
        - label: "06 — Build an API (completed the FastAPI endpoints)"
          required: false
        - label: "Starter Project (built something original)"
          required: false

  - type: textarea
    id: favorite-exercise
    attributes:
      label: "What was your favorite exercise and why?"
      description: "A sentence or two about what you enjoyed or learned."
      placeholder: "e.g., I liked the debugging exercise because Copilot found bugs I missed..."
    validations:
      required: true

  - type: textarea
    id: what-you-built
    attributes:
      label: "What did you build or modify? (optional)"
      description: "If you built something in the Starter Project or extended an exercise, briefly describe it."
      placeholder: "e.g., I built a student grade tracker that calculates GPA..."
    validations:
      required: false

  - type: checkboxes
    id: confirmations
    attributes:
      label: Submission Confirmations
      description: "Please confirm the following:"
      options:
        - label: "I am a current UNC student"
          required: true
        - label: "I forked the repository to my own GitHub account"
          required: true
        - label: "I completed at least 3 exercises using GitHub Copilot"
          required: true
        - label: "My forked repo is public so organizers can verify my work"
          required: true
        - label: "I understand vouchers are first come, first served and limited in quantity"
          required: true
