//Prompts*************************************************************
const newEntryForm = document.querySelector('#new_entry');
const newTagForm = document.querySelector('#new_tag');
const userPanel = document.querySelector('#user_panel');
const prompterBg = document.querySelector('#prompter');
const newEntryBtn = document.querySelector('#newEntryBtn');
const newTagBtn = document.querySelector('#newTagBtn');
const userPanelBtn = document.querySelector('#user_panel_btn')
const closePromptBtn = document.querySelectorAll('#closePrompt');

//All attributes are strings
function prompt(newTag, newEntry, usrPanel, prompter) {
    requestAnimationFrame(() => {
        if (prompter == 'flex') {
            newTagForm.style.display = newTag;
            newEntryForm.style.display = newEntry;
            userPanel.style.display = usrPanel;
            prompterBg.style.display = prompter;
            setTimeout(() => {
                prompterBg.style.transition = "opacity 0.25s";
                prompterBg.style.opacity = 1;
            }, 15)
        }
        else {
            prompterBg.style.transition = "opacity 0.25s";
            prompterBg.style.opacity = 0;
            setTimeout(() => {
                newTagForm.style.display = newTag;
                newEntryForm.style.display = newEntry;
                userPanel.style.display = usrPanel;
                prompterBg.style.display = prompter;
            }, 260)
        }
    });
}

newEntryBtn.addEventListener('click', () => {
    prompt('none', 'block', 'none', 'flex');
});

newTagBtn.addEventListener('click', () => {
    prompt('block', 'none', 'none', 'flex');
});

userPanelBtn.addEventListener('click', () => {
    prompt('none', 'none', 'block', 'flex');
});

for (let btn of closePromptBtn) {
    btn.addEventListener('click', () => {
        prompt('none', 'none', 'none', 'none');
    });
}

//********************************************************************

//Wrong password toast************************************************
const alertToast = document.querySelector('#liveToast')
const toastContent = document.querySelector('#toastContent')
if (alertToast.textContent.trim() == 'Wrong password, please verify.') {
    const toastBootstrap = bootstrap.Toast.getOrCreateInstance(alertToast)
    toastBootstrap.show();
    prompt('none', 'none', 'block', 'flex');
}

//Task sorting********************************************************
const deadlineBtn = document.querySelector('#deadlineFilter')
const dateBtn = document.querySelector('#dateFilter')
const taskContainer = document.querySelector('#task_container')
let tag_id = 0;
let sort_data;
const tasksArray = Array.from(document.querySelectorAll(".task_entry"))

function sortFilterTasks() {
    // Store initial positions before filtering
    const positions = new Map();
    tasksArray.forEach(task => {
        const rect = task.getBoundingClientRect();
        positions.set(task, { left: rect.left, top: rect.top });
    });

    // Separate visible and hidden items
    const visibleTasks = [];
    const hiddenTasks = [];

    tasksArray.forEach(task => {
        if (task.getAttribute('data-tag') == tag_id || tag_id == 0) {
            visibleTasks.push(task);
        }
        else {
            hiddenTasks.push(task);
        }
    });

    visibleTasks.sort((a, b) => {
        const dateA = Date.parse(a.getAttribute(sort_data));
        const dateB = Date.parse(b.getAttribute(sort_data));
        return dateA - dateB;
    });

    // Fadeout filtered tasks
    tasksArray.forEach(task => {
        task.setAttribute('pointer-events', 'none'); //Lock interaction on all tasks

        requestAnimationFrame(() => {
            task.style.transition = "opacity 0.2s";
            task.style.opacity = visibleTasks.includes(task) ? "1" : "0";
        });
    });

    //Change positions in DOM
    setTimeout(() => {
        visibleTasks.forEach(task => taskContainer.appendChild(task));
        hiddenTasks.forEach(task => taskContainer.appendChild(task));
    }, 200);

    //Animate movement
    tasksArray.forEach(task => {
        setTimeout(() => {
            const rect = task.getBoundingClientRect()
            const oldPos = positions.get(task);

            const deltaX = oldPos.left - rect.left;
            const deltaY = oldPos.top - rect.top;
            task.style.transform = `translate(${deltaX}px, ${deltaY}px)`;

            requestAnimationFrame(() => {
                task.style.transition = "transform 0.4s ease";
                task.style.transform = "translate(0, 0)";
            });
            visibleTasks.includes(task) ? task.setAttribute('pointer-events', 'all') : null; //Unlock interactions with only visible tasks
        }, 200);
    });
}

deadlineBtn.addEventListener('click', () => {
    sort_data = 'data-deadline';
    sortFilterTasks();
});
dateBtn.addEventListener('click', () => {
    sort_data = 'data-creation';
    sortFilterTasks();
});

//*********************************************************************

//Tag filtering********************************************************

const allTags = document.querySelectorAll('#tag_btn')

for (let tag_btn of allTags) {
    tag_btn.addEventListener('click', () => {
        tag_id = tag_btn.getAttribute('data-id');
        sortFilterTasks();
    });
}

//*********************************************************************