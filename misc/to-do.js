var prompt = require('prompt-sync')();
var fs = require('fs');

// Load todos from file
var todos;
try {
    var todoData = fs.readFileSync('to-doFile.txt', 'utf8');
    todos = JSON.parse(todoData);
} catch (err) {
    // If the file doesn't exist or can't be read for some other reason, start with an empty list of todos
    todos = [];
}

// Main menu
while (true) {
    console.log('\n');
    console.log('1. View To-dos');
    console.log('2. Add To-do');
    console.log('3. Remove To-do');
    console.log('4. Sort To-dos');
    console.log('5. Get a Random To-do');
    console.log('6. View By Category');
    console.log('7. View By Priority');
    console.log('8. View Done To-dos');
    console.log('9. Mark a To-do as Completed');
    console.log('10. Quit');
    console.log('\n');

    var choice = prompt('Please choose an option: ');

    // View To-dos
    if (choice == '1') {
        console.log('\nHere are your todos:');
        for (var i = 0; i < todos.length; i++) {
            console.log((i+1) + '. ' + todos[i].task + ' - Category: ' + todos[i].category + ' - Priority: ' + todos[i].priority + ' - Done: ' + todos[i].done);
        }
    } 
    // Add To-do
    else if (choice == '2') {
        var newTodo = prompt('Enter a new todo: ');
        var category = prompt('Enter a category: ');
        var priority = prompt('Enter a priority (1-5): ');
        todos.push({task: newTodo, category: category, priority: parseInt(priority), done: false});
        fs.writeFileSync('to-doFile.txt', JSON.stringify(todos));
    } 
    // Remove To-do
    else if (choice == '3') {
        var index = prompt('Enter the number of the to-do to remove: ');
        if (!isNaN(index) && index > 0 && index <= todos.length) {
            todos.splice(index-1, 1);
            fs.writeFileSync('to-doFile.txt', JSON.stringify(todos));
        } else {
            console.log("Invalid input. Please enter a valid to-do number to remove.")
        }
    } 
    // Sort To-dos
    else if (choice == '4') {
        console.log('1. Sort alphabetically');
        console.log('2. Sort by length');
        console.log('3. Sort by priority');
        var sortChoice = prompt('Choose a sorting option: ');
        if (sortChoice == '1') {
            todos.sort((a, b) => a.task.localeCompare(b.task));
        } else if (sortChoice == '2') {
            todos.sort((a, b) => a.task.length - b.task.length);
        } else if (sortChoice == '3') {
            todos.sort((a, b) => a.priority - b.priority);
        } else {
            console.log("Invalid input. Please choose a valid sorting option.")
        }
        fs.writeFileSync('to-doFile.txt', JSON.stringify(todos));
    }
    // Get a Random To-do
    else if (choice == '5') {
        var randomTodo = todos[Math.floor(Math.random() * todos.length)];
        console.log('Your random todo is: ' + randomTodo.task);
    }
    // View by Category
    else if (choice == '6') {
        var category = prompt('Enter the category to view: ');
        var filteredTodos = todos.filter(todo => todo.category === category);
        console.log('\nHere are your todos in category ' + category + ':');
        for (var i = 0; i < filteredTodos.length; i++) {
            console.log((i+1) + '. ' + filteredTodos[i].task);
        }
    }
    // View by Priority
    else if (choice == '7') {
        var priority = prompt('Enter the priority to view (1-5): ');
        var filteredTodos = todos.filter(todo => todo.priority === parseInt(priority));
        console.log('\nHere are your todos with priority ' + priority + ':');
        for (var i = 0; i < filteredTodos.length; i++) {
            console.log((i+1) + '. ' + filteredTodos[i].task);
        }
    }
    // View Done To-dos
    else if (choice == '8') {
        var doneTodos = todos.filter(todo => todo.done);
        console.log('\nHere are your done todos:');
        for (var i = 0; i < doneTodos.length; i++) {
            console.log((i+1) + '. ' + doneTodos[i].task);
        }
    }
    // Mark a To-do as Completed
    else if (choice == '9') {
        var index = prompt('Enter the number of the to-do to mark as completed: ');
        if (!isNaN(index) && index > 0 && index <= todos.length) {
            todos[index-1].done = true;
            fs.writeFileSync('to-doFile.txt', JSON.stringify(todos));
            console.log("Todo marked as completed.");
        } else {
            console.log("Invalid input. Please enter a valid to-do number to mark as completed.")
        }
    }
    // Quit
    else if (choice == '10') {
        console.log("Goodbye!");
        break;
    }
    else {
        console.log("Invalid choice. Please enter a number between 1 and 10.");
    }
}