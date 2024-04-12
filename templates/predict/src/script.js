const submitButton = document.getElementById('submitB');
const closeButton = document.getElementById('closebutton');


function show() {
    
}

 // Function to display dialogue box
 function showSubmitDialogue() {
    // var dialog = document.querySelector('dialog');
    // dialog.showModal();

    var dialogue = document.getElementById('dialogue');
    dialogue.style.display = 'block';
}

// Close dialogue box
document.getElementById('closebutton').addEventListener('click', function () {
    var dialog = document.querySelector('dialog');
    dialog.close();
});

// Submit form event
document.getElementById("myForm").addEventListener("submit", function (event) {
    // Prevent default form submission
    event.preventDefault();
    // Call function to display dialogue box
    showSubmitDialogue();


    ///api calll





});

function closeDialogue() {
    document.getElementById("dialogue").style.display = "none";
}
