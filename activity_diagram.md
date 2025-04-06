
# 🔄 Activity Workflow Modeling - Personalised Meal Planner

 Workflows are broken down into 8 main activities.

---

## 1. 👤 User Registration

```mermaid
%%{init: {'flowchart': {'useMaxWidth': true}} }%%
flowchart TD
    UserStart([Start]) --> FillForm[User: Fill Registration Form]
    FillForm --> SubmitForm[User: Submit Form]
    SubmitForm --> Validate[System: Validate Input]
    Validate -->|Valid| SendEmail[System: Send Verification Email]
    Validate -->|Invalid| ShowError[System: Show Error Message]
    SendEmail --> ConfirmEmail[User: Click Verification Link]
    ConfirmEmail --> Activate[System: Activate Account]
    Activate --> RegEnd([End])
```

📝 *This diagram addresses the need for secure onboarding by validating inputs and confirming emails before account activation.*

---

## 2. 🛒 Generate Grocery List

```mermaid
%%{init: {'flowchart': {'useMaxWidth': true}} }%%
flowchart TD
    Start([Start]) --> SelectPlan[User: Select Meal Plan]
    SelectPlan --> FetchRecipes[System: Retrieve Recipes]
    FetchRecipes --> ExtractIngredients[System: Extract Ingredients]
    ExtractIngredients --> RemoveDuplicates[System: Remove Duplicate Items]
    RemoveDuplicates --> GenerateList[System: Compile Grocery List]
    GenerateList --> DisplayList[User: Display to User]
    DisplayList --> End([End])
```

📝 *Streamlines ingredient management ensuring accurate, duplicate-free grocery lists, reducing user workload.*

---

## 3. 🧬 Update Dietary Profile

```mermaid
%%{init: {'flowchart': {'useMaxWidth': true}} }%%
flowchart TD
    Start([Start]) --> ViewProfile[User: View Current Profile]
    ViewProfile --> EditProfile[User: Make Changes]
    EditProfile --> ValidateInput[System: Validate Inputs]
    ValidateInput -->|Valid| SaveChanges[System: Save to DB]
    ValidateInput -->|Invalid| ShowError[System: Show Error Message]
    SaveChanges --> End([End])
```

📝 *Ensures dietary needs are correctly captured and validated before updating profile.*

---

## 4. 📋 Submit Recipe

```mermaid
%%{init: {'flowchart': {'useMaxWidth': true}} }%%
flowchart TD
    Start([Start]) --> EnterRecipe[User: Enter Recipe Details]
    EnterRecipe --> Submit[User: Submit Recipe]
    Submit --> Review[Admin: Review Recipe]
    Review -->|Approved| Approve[Admin: Mark as Approved]
    Review -->|Rejected| Reject[Admin: Mark as Rejected]
    Approve --> NotifyUser[System: Notify User]
    Reject --> NotifyUser
    NotifyUser --> End([End])
```

📝 *Aligns with the moderation process to maintain recipe quality and notify users transparently.*

---

## 5. 🥗 Create Meal Plan

```mermaid
%%{init: {'flowchart': {'useMaxWidth': true}} }%%
flowchart TD
    Start([Start]) --> SelectPreferences[User: Select Preferences]
    SelectPreferences --> SuggestMeals[System: Suggest Meals]
    SuggestMeals --> CustomizePlan[User: Customize Meal Plan]
    CustomizePlan --> SavePlan[User: Save Plan]
    SavePlan --> End([End])
```

📝 *Addresses user flexibility with customizable, system-suggested plans.*

---

## 6. 💳 Subscription Workflow

```mermaid
%%{init: {'flowchart': {'useMaxWidth': true}} }%%
flowchart TD
    Start([Start]) --> ChoosePlan[User: Choose Subscription Plan]
    ChoosePlan --> EnterPayment[User: Enter Payment Details]
    EnterPayment --> ValidatePayment[System: Validate Payment Info]
    ValidatePayment -->|Success| ActivatePlan[System: Activate Plan]
    ValidatePayment -->|Failure| ShowError[System: Payment Failed]
    ActivatePlan --> End([End])
    ShowError --> End
```

📝 *Ensures robust validation before enabling paid features, addressing financial reliability.*

---

## 7. 🛠️ Admin Reinstates User

```mermaid
%%{init: {'flowchart': {'useMaxWidth': true}} }%%
flowchart TD
    Start([Start]) --> ViewSuspended[Admin: View Suspended Users]
    ViewSuspended --> SelectUser[Admin: Select a User]
    SelectUser --> VerifyCase[Admin: Verify Reason for Suspension]
    VerifyCase -->|Valid| Reinstate[Admin: Reinstate User]
    VerifyCase -->|Invalid| RejectRequest[Admin: Reject Reinstatement]
    Reinstate --> NotifyUser[System: Notify User]
    RejectRequest --> NotifyUser
    NotifyUser --> End([End])
```

📝 *Ensures fair decision-making for reinstatements with appropriate admin verification.*

---

## 8. 🧾 Generate Report

```mermaid
%%{init: {'flowchart': {'useMaxWidth': true}} }%%
flowchart TD
    Start([Start]) --> ChooseType[User: Choose Report Type]
    ChooseType --> SetFilters[User: Set Date/Filters]
    SetFilters --> Generate[System: Generate Report]
    Generate -->|Success| ViewReport[User: View Report]
    Generate -->|Failure| ShowError[System: Show Error Message]
    ViewReport --> End([End])
    ShowError --> End
```

📝 *Empowers users with insights and monitoring of progress through dynamic reports.*

---
