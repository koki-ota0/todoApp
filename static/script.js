// Auto-refresh the page after adding a new todo
var addForm = document.getElementById('addForm');
addForm.addEventListener('submit', function(event) {
    event.preventDefault();
    var todoInput = document.getElementById('todoInput');
    var todo = todoInput.value.trim();
    if (todo !== '') {
        fetch('/add', {
            method: 'POST',
            body: new URLSearchParams({
                todo: todo
            })
        }).then(function() {
            // Clear the input field and reload the page after a short delay
            todoInput.value = '';
            setTimeout(function() {
                location.reload();
            }, 100);
        });
    }
});

// Get the filter value from local storage if available
var filterSelect = document.getElementById('filterSelect');
var storedFilter = localStorage.getItem('filter');
if (storedFilter) {
    filterSelect.value = storedFilter;
}

function applyFilter() {
    var filter = filterSelect.value;
    localStorage.setItem('filter', filter); // Store the filter value in local storage

    var todoList = document.getElementById('todoList');
    var todoItems = todoList.getElementsByTagName('li');

    // Convert HTMLCollection to an array for easy sorting
    var todoArray = Array.from(todoItems);

    todoArray.sort(function(a, b) {
        var aChecked = a.classList.contains('checked');
        var bChecked = b.classList.contains('checked');

        if (filter === 'all') {
            // Sort by unchecked items first, then checked items
            if (aChecked && !bChecked) {
                return 1;
            } else if (!aChecked && bChecked) {
                return -1;
            }
        }

        // Preserve the original order for other filter options
        return 0;
    });

    // Reorder the list items
    todoArray.forEach(function(todoItem) {
        todoList.appendChild(todoItem);
    });

    // Update visibility based on the selected filter
    for (var i = 0; i < todoItems.length; i++) {
                        var todoItem = todoItems[i];
        if (filter === 'all') {
            todoItem.style.display = 'block';
        } else if (filter === 'checked' && !todoItem.classList.contains('checked')) {
            todoItem.style.display = 'none';
        } else if (filter === 'unchecked' && !todoItem.classList.contains('unchecked')) {
            todoItem.style.display = 'none';
        } else {
            todoItem.style.display = 'block';
        }
    }
}

function toggleCheck(checkbox, index) {
    fetch(`/check/${index}`, {
        method: 'POST',
        body: JSON.stringify({ checked: checkbox.checked }),
        headers: {
            'Content-Type': 'application/json'
        }
    }).then(() => {
        // Refresh the page after a short delay to allow the server to update the data
        setTimeout(function() {
            location.reload();
        }, 100);
    });
}

function deleteTodo(index) {
    if (confirm("Are you sure you want to delete this todo?")) {
        fetch(`/delete/${index}`, {
            method: 'POST'
        }).then(() => {
            // Refresh the page after a short delay to allow the server to update the data
            setTimeout(function() {
                location.reload();
            }, 100);
        });
    }
}