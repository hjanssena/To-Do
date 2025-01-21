const newEntryForm = document.querySelector('#new_entry');
const newTagForm = document.querySelector('#new_tag');
const prompter = document.querySelector('#prompter');
const newEntryBtn = document.querySelector('#newEntryBtn');
const newTagBtn = document.querySelector('#newTagBtn');
const closePromptBtn = document.querySelectorAll('#closePrompt');

newEntryBtn.addEventListener('click', () => {
    newTagForm.style.display = 'none';
    newEntryForm.style.display = 'block';
    prompter.style.display = 'flex';
    console.log('a');
});

newTagBtn.addEventListener('click', () => {
    newTagForm.style.display = 'block';
    newEntryForm.style.display = 'none';
    prompter.style.display = 'flex';
    console.log('a');
});

for (let btn of closePromptBtn) {
    btn.addEventListener('click', () => {
        newTagForm.style.display = 'none';
        newEntryForm.style.display = 'none';
        prompter.style.display = 'none';
    });
}

