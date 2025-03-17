### Use Case 1: Select Meal Plan

Actor: User Description: The user selects a personalized meal plan based on dietary preferences.

Precondition: User is logged in using email address and password.

Postcondition: The Meal plan is saved to the user’s profile.

Basic Flow:

The user navigates to the meal plan section.

The user selects a plan based on dietary needs.

The system saves the selection.

Alternative Flow:

If the plan is unavailable, the system suggests an alternative.

### Use Case 2: Set Dietary Preferences

Actor: User Description: The user defines dietary restrictions and preferences.

Precondition: The User is logged in.

Postcondition: Preferences are saved and applied to meal recommendations.

Basic Flow:

The user enters dietary preferences.

The system updates user profile settings.

The meal recommendations are adjusted accordingly.

Alternative Flow:

If an invalid preference is entered, the system prompts for correction.

### Use Case 3: Generate Shopping List

Actor: User Description: The user generates a shopping list based on the selected meal plan.

Precondition: The user has a saved meal plan.

Postcondition: The Shopping list is generated and saved.

Basic Flow:

The user navigates to the shopping list section.

The user selects the meal plan period.

The system generates a list of required ingredients.

The user saves or downloads the list.

Alternative Flow:

If ingredients are unavailable, the system suggests substitutes.

### Use Case 4: Log Meal Consumption

Actor: User Description: The user logs consumed meals for tracking purposes.

Precondition: The user has a selected meal plan.

Postcondition: The meal log is updated in the system.

Basic Flow:

The user navigates to the meal log section.

The user selects a consumed meal.

The system records the meal consumption.

Alternative Flow:

If a meal is not listed, the system allows manual entry.

### Use Case 5: Receive Nutrition Insights

Actor: User Description: The user receives insights based on logged meals.

Precondition: The user has logged at least one meal.

Postcondition: The nutrition insights are displayed.

Basic Flow:

The user accesses the insights section.

The system analyzes logged meals.

The system presents nutrition breakdown and health suggestions.

Alternative Flow:

If no meals are logged, the system prompts the user to start tracking meals.

### Use Case 6: Manage Recipes

Actor: Admin Description: The admin adds, updates, or removes recipes from the system.

Precondition: The admin is logged in by entering the email address and password.

Postcondition: The Recipe database is updated.

Basic Flow:

The admin navigates to the recipe management section.

The admin selects add, update, or delete.

The system updates the recipe database.

Alternative Flow:

If an error occurs, the system prompts the admin to retry.

### Use Case 7: Monitor User Engagement

Actor: Admin Description: Admin monitors user activity and engagement metrics.

Precondition: Admin is logged in.

Postcondition: Engagement data is retrieved and analyzed.

Basic Flow:

The admin accesses the analytics dashboard.

The system retrieves user activity data.

The admin reviews engagement statistics.

Alternative Flow:

If no data is available, the system notifies the admin.

### Use Case 8: Sync with Calendar

Actor: System Description: The System syncs meal plans with an external calendar.

Precondition: User has a selected meal plan.

Postcondition: The Meal plan is synced with the calendar.

Basic Flow:

The system checks for upcoming meals.

The system syncs meal schedules with the user’s calendar.

Alternative Flow:

If calendar sync fails, the system notifies the user.
