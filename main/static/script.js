const newEntryForm = document.querySelector('#new_entry');
const newTagForm = document.querySelector('#new_tag');
const userPanel = document.querySelector('#user_panel');
const prompter = document.querySelector('#prompter');
const newEntryBtn = document.querySelector('#newEntryBtn');
const newTagBtn = document.querySelector('#newTagBtn');
const userPanelBtn = document.querySelector('#user_panel_btn')
const closePromptBtn = document.querySelectorAll('#closePrompt');

newEntryBtn.addEventListener('click', () => {
    newTagForm.style.display = 'none';
    newEntryForm.style.display = 'block';
    userPanel.style.display = 'none';
    prompter.style.display = 'flex';
});

newTagBtn.addEventListener('click', () => {
    newTagForm.style.display = 'block';
    newEntryForm.style.display = 'none';
    userPanel.style.display = 'none';
    prompter.style.display = 'flex';
});

userPanelBtn.addEventListener('click', () =>{
    newTagForm.style.display = 'none';
    newEntryForm.style.display = 'none';
    userPanel.style.display = 'block';
    prompter.style.display = 'flex';
});

for (let btn of closePromptBtn) {
    btn.addEventListener('click', () => {
        newTagForm.style.display = 'none';
        newEntryForm.style.display = 'none';
        userPanel.style.display = 'none';
        prompter.style.display = 'none';
    });
}

const alertToast = document.querySelector('#liveToast')
const toastContent = document.querySelector('#toastContent')
if (alertToast.textContent.trim() == 'Wrong password, please verify.'){
    const toastBootstrap = bootstrap.Toast.getOrCreateInstance(alertToast)
    toastBootstrap.show();
    newTagForm.style.display = 'none';
    newEntryForm.style.display = 'none';
    userPanel.style.display = 'block';
    prompter.style.display = 'flex';
}